from pyspark.sql.functions import (
    col,
    when,
    lit,
    round
)


def select_required_columns(df):
    """
    Select only the required columns.
    """

    selected_df = df.select(
        "Order_ID",
        "Customer_Name",
        "Category",
        "Quantity",
        "Price",
        "City"
    )

    return selected_df


def filter_records(df):
    """
    Filter rows where Quantity is greater than 2.
    """

    filtered_df = df.filter(col("Quantity") > 2)

    return filtered_df


def rename_columns(df):
    """
    Rename columns for better readability.
    """

    renamed_df = (
        df.withColumnRenamed("Customer_Name", "Customer")
          .withColumnRenamed("Order_ID", "OrderID")
    )

    return renamed_df


def cast_data_types(df):
    """
    Cast Quantity and Price to required data types.
    """

    casted_df = (
        df.withColumn("Quantity", col("Quantity").cast("int"))
          .withColumn("Price", col("Price").cast("double"))
    )

    return casted_df


def add_total_amount(df):
    """
    Add a new column Total_Amount.
    """

    updated_df = df.withColumn(
        "Total_Amount",
        round(col("Quantity") * col("Price"), 2)
    )

    return updated_df


def add_order_status(df):
    """
    Add a new column Order_Status.
    """

    status_df = df.withColumn(
        "Order_Status",
        when(col("Total_Amount") >= 1000, "High Value")
        .otherwise("Regular")
    )

    return status_df


def handle_null_values(df):
    """
    Replace null values.
    """

    cleaned_df = (
        df.fillna({
            "Customer": "Unknown",
            "City": "Not Available",
            "Category": "Others",
            "Quantity": 0,
            "Price": 0.0
        })
    )

    return cleaned_df


def remove_duplicate_records(df):
    """
    Remove duplicate rows.
    """

    return df.dropDuplicates()


def sort_dataset(df):
    """
    Sort data by Total Amount.
    """

    sorted_df = df.orderBy(col("Total_Amount").desc())

    return sorted_df


def final_transformation(df):
    """
    Complete transformation pipeline.
    """

    df = select_required_columns(df)

    df = filter_records(df)

    df = rename_columns(df)

    df = cast_data_types(df)

    df = add_total_amount(df)

    df = add_order_status(df)

    df = handle_null_values(df)

    df = remove_duplicate_records(df)

    df = sort_dataset(df)

    return df