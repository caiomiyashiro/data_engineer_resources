from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("lowersongs").getOrCreate()

    log_songs = ["Despacito", "Tiro conmigo", "Babacito"]

    dist_log_songs = spark.sparkContext.parallelize(log_songs)
    results = dist_log_songs.map(lambda x: x.lower()).collect()
    print(f"""{results}""")

    spark.stop()
