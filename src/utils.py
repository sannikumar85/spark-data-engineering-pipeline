import os


def print_title(title):
    """
    Prints a formatted title.
    """

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def display_dataframe(df, rows=10):
    """
    Displays DataFrame records.
    """

    print_title("Data Preview")

    df.show(rows, truncate=False)


def display_schema(df):
    """
    Displays DataFrame schema.
    """

    print_title("Data Schema")

    df.printSchema()


def display_record_count(df):
    """
    Displays total number of records.
    """

    print_title("Total Records")

    print(df.count())


def display_column_names(df):
    """
    Displays all column names.
    """

    print_title("Column Names")

    for column in df.columns:
        print(column)


def save_as_csv(df, output_path):
    """
    Saves DataFrame as CSV.
    """

    (
        df.write
        .mode("overwrite")
        .option("header", True)
        .csv(output_path)
    )

    print(f"\nCSV saved successfully at:\n{os.path.abspath(output_path)}")


def save_as_parquet(df, output_path):
    """
    Saves DataFrame as Parquet.
    """

    (
        df.write
        .mode("overwrite")
        .parquet(output_path)
    )

    print(f"\nParquet saved successfully at:\n{os.path.abspath(output_path)}")


def display_summary(df):
    """
    Displays complete DataFrame information.
    """

    display_schema(df)

    display_record_count(df)

    display_column_names(df)

    display_dataframe(df)