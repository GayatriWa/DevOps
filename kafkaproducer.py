from kafka import KafkaProducer
import os
bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()
ack = producer.send(topicName, b'Hello World!!!!!!!!',b'JOB_NAME')
metadata = ack.get()
print(metadata.topic)
print(metadata.partition)
print(metadata.JOB_NAME)

