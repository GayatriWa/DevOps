from kafka import KafkaProducer
import os
bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()
ack = producer.send(topicName, b'Hello World!!!!!!!!')
metadata = ack.get()
print(metadata.topic)
print(metadata.partition)

print(os.environ['JOB_NAME'])
print(os.environ['BUILD_NUMBER'])
print(os.environ['BUILD_URL'])
print(os.environ['BUILD_TAG'])
print(os.environ['BUILD_ID'])
