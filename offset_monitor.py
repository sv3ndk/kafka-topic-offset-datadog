from datadog import statsd
from kafka import KafkaConsumer, TopicPartition
import time

from offset_monitor_config import config as config

try:

    consumers = {topic: KafkaConsumer(**config["kafka_consumer_config"])
                 for topic in config["topics"]}

    while True:
        for topic, consumer in consumers.items():
            partitions = consumer.partitions_for_topic(topic)
            if partitions is not None: 
                for partition in partitions:
                    tp = TopicPartition(topic, partition)

                    consumer.assign([tp])
                    consumer.seek_to_end(tp)
                    last_offset = consumer.position(tp)

                    name = config["metric_name"]
                    print ("{}: {}".format(name, last_offset))

                    statsd.gauge(metric=config["metric_name"], 
                                 value=last_offset,
                                 tags=["topic:{}".format(topic), 
                                       "partition:{}".format(partition) ], 
                                 sample_rate=1)


        time.sleep(config["poll_period_seconds"])

finally:
    print("exiting")
    if consumers: 
        for topic, consumer in consumers.items():
            consumer.close(autocommit=False)


            