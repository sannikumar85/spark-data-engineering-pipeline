from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType
)


def get_sales_schema():
    """
    Returns the schema for the sales dataset.
    """

    schema = StructType([
        StructField("Order_ID", StringType(), True),
        StructField("Customer_Name", StringType(), True),
        StructField("Category", StringType(), True),
        StructField("Product", StringType(), True),
        StructField("Quantity", IntegerType(), True),
        StructField("Price", DoubleType(), True),
        StructField("City", StringType(), True)
    ])

    return schema


def read_csv_data(spark, file_path):
    """
    Reads a CSV file using the predefined schema.
    """

    df = (
        spark.read
        .option("header", True)
        .schema(get_sales_schema())
        .csv(file_path)
    )

    return df


def read_parquet_data(spark, file_path):
    """
    Reads a Parquet file.
    """

    df = spark.read.parquet(file_path)

    return df


def display_dataset_info(df):
    """
    Displays dataset information.
    """

    print("\n========== Dataset Preview ==========\n")
    df.show(5, truncate=False)

    print("\n========== Schema ==========\n")
    df.printSchema()

    print("\n========== Total Records ==========\n")
    print(df.count())


if __name__ == "__main__":

    from spark_session import create_spark_session

    spark = create_spark_session()

    csv_file = "../data/input/sales.csv"

    sales_df = read_csv_data(spark, csv_file)

    display_dataset_info(sales_df)

    spark.stop()