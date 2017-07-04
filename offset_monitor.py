from datadog import statsd
from kafka import KafkaConsumer, TopicPartition
import time

from offset_monitor_config import config as config

while True:
    for topic in config["topics"]:
        consumer = KafkaConsumer(**config["kafka_consumer_config"])
        partitions = consumer.partitions_for_topic(topic)
        if partitions is not None: 
            for p in partitions:
                tp = TopicPartition(topic, p)
                consumer.assign([tp])
                consumer.seek_to_end(tp)
                last_offset = consumer.position(tp)
                print("topic: %s partition: %s  last: %s " % (topic, p,  last_offset ))

    time.sleep(config["poll_period_seconds"])

consumer.close(autocommit=False)