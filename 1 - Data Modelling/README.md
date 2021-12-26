# Project: Data Modeling with Postgres

This project models user activity data for a music streaming app called Sparkify. It creates a **Postgres relational database** and **ETL pipeline** to build up **Fact and Dimension tables** and insert data into new tables.


## ETL Pipeline
### etl.py
ETL pipeline builder

1. `process_data`
	* Wrap the ETL processing for a specific file type: `process_song_file` and `process_log_file`
2. `process_song_file`
	* Process the song files. Extract and insert artist data and song data into the respective database tables
3. `process_log_file`
	* Process the log files. Extract and insert time, user and songplay data into the respective database tables

### create_tables.py
Creating Fact and Dimension table schema

1. `create_database`
2. `drop_tables`
3. `create_tables`

### sql_queries.py
Helper SQL query statements for `etl.py` and `create_tables.py`

1. `*_table_drop`
2. `*_table_create`
3. `*_table_insert`
4. `song_select`


## Database Schema
### Fact table
```
songplays
	- songplay_id 	PRIMARY KEY
	- start_time 	REFERENCES time (start_time)
	- user_id	REFERENCES users (user_id)
	- level
	- song_id 	REFERENCES songs (song_id)
	- artist_id 	REFERENCES artists (artist_id)
	- session_id
	- location
	- user_agent
```

### Dimension table
```
users
	- user_id 	PRIMARY KEY
	- first_name
	- last_name
	- gender
	- level

songs
	- song_id 	PRIMARY KEY
	- title
	- artist_id	REFERENCES artists (artist_id)
	- year
	- duration

artists
	- artist_id 	PRIMARY KEY
	- name
	- location
	- latitude
	- longitude

time
	- start_time 	PRIMARY KEY
	- hour
	- day
	- week
	- month
	- year
	- weekday
```