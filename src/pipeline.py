from spark_session import create_spark_session
from read_data import read_csv_data
from transformations import final_transformation
from utils import (
    print_title,
    display_summary,
    save_as_csv,
    save_as_parquet
)


def main():

    # Create Spark Session
    spark = create_spark_session()

    # Input and Output Paths
    input_file = "../data/input/sales.csv"
    csv_output = "../data/output/csv_output"
    parquet_output = "../data/output/parquet_output"

    # Read CSV File
    print_title("Reading Input Dataset")

    sales_df = read_csv_data(spark, input_file)

    # Display Original Dataset
    print_title("Original Dataset")

    display_summary(sales_df)

    # Apply Transformations
    print_title("Applying Transformations")

    transformed_df = final_transformation(sales_df)

    # Display Processed Dataset
    print_title("Processed Dataset")

    display_summary(transformed_df)

    # Save as CSV
    print_title("Saving CSV Output")

    save_as_csv(transformed_df, csv_output)

    # Save as Parquet
    print_title("Saving Parquet Output")

    save_as_parquet(transformed_df, parquet_output)

    print_title("Pipeline Executed Successfully")

    spark.stop()


if __name__ == "__main__":
    main()