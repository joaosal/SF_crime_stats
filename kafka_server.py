import producer_server


def run_kafka_server():
	# TODO get the json file path
    input_file = "police-department-calls-for-service.json"

    # TODO create a Producer Server
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="police-department-calls-sf",
        bootstrap_servers="localhost:9092",
        client_id="None"
    )

    if producer.bootstrap_connected():
        print("Connected to Kafka")

    return producer


def feed():
    producer = run_kafka_server()
    try:
        producer.generate_data()
    except:
        producer.counter = 0
        producer.flush()
        producer.close()



if __name__ == "__main__":
    feed()
