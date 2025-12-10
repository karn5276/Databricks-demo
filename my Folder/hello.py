from pyspark.sql.functions import randstr

df = spark.range(1).select(randstr(100).alias("random_text"))
display(df)