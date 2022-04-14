import requests
import json
from json import dumps
from kafka import KafkaProducer
from datetime import datetime
from requests.auth import HTTPBasicAuth
    
res = requests.get('http://localhost:8080/job/kafka/10/wfapi/',auth=HTTPBasicAuth('gayatriw','ZW8r9gdV'))

# print(res.text)
print(type(res.text)) # to check the data type
j_object = json.loads(res.text)
print(type(j_object))
# print(j_object)
def write_json(new_data, filename='test.json'):
    # with open(filename,'r') as f:
    #     print(type(new_data))
    #     json_object = json.loads(new_data)
    #     print(type(json_object))
    #     f.write(json_object)
        
        # data["pipeline_data"].append(new_data)
    with open(filename, 'w') as file:
        json.dump(j_object, file)
write_json(res.text)


f = open('test.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
# for i in :
def build_info():
    build_name = data['name']
    build_status = data['status']
    pipeline_startime=datetime.fromtimestamp(data['startTimeMillis']//1000).isoformat()
    pipeline_endtime=datetime.fromtimestamp(data['endTimeMillis']//1000).isoformat()
    
    build_pipeline_data = {"Build_name":build_name,"Build_status":build_status ,"pipeline_starttime":pipeline_startime,"pipeline_endtime":pipeline_endtime}
    return(build_pipeline_data)

# info=build_info()
# print(info)
topicName = 'myTopic'

producer = KafkaProducer(bootstrap_servers = ['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
# producer = KafkaProducer()

producer.send(topicName, value=build_info())
producer.flush()



