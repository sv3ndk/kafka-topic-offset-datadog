
config = {
    # see valid parameters here: http://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
    "kafka_consumer_config": {
        "group_id": "datadog.offset.monitor",        
        "client_id": "datadog.offset.monitor", 
        "bootstrap_servers": ['localhost:9092']
    },

    # see valid parameters here: http://datadogpy.readthedocs.io/en/latest/#datadog.dogstatsd.base.DogStatsd
    "datadog_client_config": {
        "host": "localhost"
    },

    # set of topics to monitor
    "topics": ['test-svend-1', 'test-svend-2', 'test-svend-3'],

    # wait period between each offset poll 
    "poll_period_seconds": 10,

    # name of the datadog metric 
    "metric_name": "kafka.broker.topic.latest.offset"
}

