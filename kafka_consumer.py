import config
import json

from kafka import KafkaConsumer


class KafkaConsumerConnect:
    """ Example class for work with Kafka Consumer """

    consumer = KafkaConsumer(config.KAFKA_TOPIC,
                             bootstrap_servers=config.KAFKA_SERVER,
                             auto_offset_reset='earliest',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                             )
    print("ready")

    for message in consumer:
        print(message.value)


if __name__ == "__main__":
    KafkaConsumerConnect()




