


config = {
    # see parameter list here: http://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
    "kafka_consumer_config": {
        "group_id": "datadog.offset.monitor",        
        "client_id": "datadog.offset.monitor", 
        "bootstrap_servers": ['localhost:9092']
    },
    "topics": ['test-svend-1', 'test-svend-2', 'test-svend-3'],
    "poll_period_seconds": 10
}
