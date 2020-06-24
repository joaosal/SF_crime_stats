from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic
        self.counter = 0

    #TODO we're generating a dummy data
    def generate_data(self):
        with open(self.input_file) as f:
            f_json = json.load(f)
            for line in f_json:
                print(f'Line: {line}')
                message = self.dict_to_binary(line)
                print(f'Message: {message}')
                # Send the correct data
                record = self.send(topic=self.topic, value=message)
                self.counter = self.counter + 1
                print(f'Record number: {self.counter} - Record: {record.get()}')
                time.sleep(0.3)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf8')
        