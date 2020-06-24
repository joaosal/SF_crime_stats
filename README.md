# Kafka and Spark Streaming Integration

## Overview
In this project, you will be provided with a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and you will provide statistical analyses of the data using Apache Spark Structured Streaming. You will draw on the skills and knowledge you've learned in this course to create a Kafka server to produce data, and ingest data through Spark Structured Streaming.

### How to Run?

Install Confluent Platform

or

Modify the Zookepeer and Server .properties

#### Run Kafka Producer server
`python kafka_server.py`

#### Run the kafka Consumer server 
`python kafka_consumer.py`

#### Submit Spark Streaming Job
`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local data_stream.py`

### kafka consumer console output
![Kafka Consumer Console Output](https://github.com/joaosal/SF_crime_stats/blob/master/kafka-console-consumer-out.png)

### Streaming progress reporter
![Progress Reporter](https://github.com/joaosal/SF_crime_stats/blob/master/spark-streaming-progress-report.png)


### Output
![output](https://github.com/joaosal/SF_crime_stats/blob/master/output.png)


### Questions
1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

ANS ->  maxOffsetsPerTrigger limit the number of records to fetch per trigger, this means that for each trigger or fetch process Kafka will get 200 records per partition.

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
ANS -> maxRatePerPartition to set the maximum number of messages per partition per batch.
I have to set up different values in order to have a proper rate of messages, it is more trial and error


