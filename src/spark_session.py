from pyspark.sql import SparkSession


def create_spark_session():
    """
    Creates and returns a Spark Session.
    """

    spark = (
        SparkSession.builder
        .appName("Spark Assignment")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark


if __name__ == "__main__":
    spark = create_spark_session()

    print("=" * 50)
    print("Spark Session Created Successfully")
    print("=" * 50)
    print(f"Application Name : {spark.sparkContext.appName}")
    print(f"Spark Version    : {spark.version}")
    print(f"Master           : {spark.sparkContext.master}")
    print("=" * 50)

    spark.stop()