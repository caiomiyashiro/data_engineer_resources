# Project: Spark and Data Lake
This project builds an **ETL pipeline** for a **data lake**. The data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in the app. We loaded data from S3, process the data into analytics tables using **Spark**, and load them back into S3.


## Project Structure

```
Spark and Data Lake
|____etl.py              # ETL builder
|____dl.cfg              # AWS configuration file
```

## How to Run

1. Code was executed using AWS - EMR clusters. 

2. etl.py and dl.cfg was uploaded to EMR server and executed with `spark-submit`
2.a. AWS credentials were added to dl.cfg

## ELT Pipeline
### etl.py
ELT pipeline builder

1. `process_song_data`
	* Load raw data from S3 buckets to Spark stonealone server and process song dataset to insert record into _songs_ and _artists_ dimension table

2. `process_log_data`
	* Load raw data from S3 buckets to Spark stonealone server and Process event(log) dataset to insert record into _time_ and _users_ dimensio table and _songplays_ fact table
