import config

from kafka import KafkaProducer


class KafkaProducerConnect:
    """ Example class for work with Kafka Producer """

    producer = KafkaProducer(
        bootstap_servers=config.KAFKA_SERVER,
        security_protocol="SASL_PLAINTEXT",
        sasl_mechanism="SCRAM-SHA-512",
        sasl_plain_username=config.PLAIN_USERNAME,
        sasl_plain_password=config.PLAIN_PASSWORD)

    producer.send('<topic name>', b'test message', b'key')
    producer.flush()
    producer.close()
