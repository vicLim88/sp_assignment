import matplotlib.pyplot as plot
from numpy import nan
from utils.file.pandas_excel import pandasFileService
from utils.printing.print_header import print_header_with_stars


def subset_column_task_3() -> None:
    """
        Pick Specific Columns with values > 500k
    """
    print("*** Data in 1980 column ***")

    excel_name: str = "singstats_maritalstatus"
    mydf_excel_obj: pandasFileService = pandasFileService()
    mydf = mydf_excel_obj.get_excel_file(excel_name)[["1980"]]
    print(mydf)
    print(" ")

    # Filtering Number of rows more than 500k using boolean indexing
    r_more_than_500k, c_more_than_500k = mydf[mydf['1980'] > 500000].shape
    print(f"Number of rows more than 500k is {r_more_than_500k}")

    # Filtering Number of rows less than 500k using boolean indexing
    r_less_than_500k, c_less_than_500k = mydf[mydf['1980'] < 500000].shape
    print(f"Number of rows less than 500k is {r_less_than_500k}")


def subset_column_task_4() -> None:
    """
        Pick Specific Columns that starts with character 201
    """
    excel_name: str = "singstats_maritalstatus"
    mydf_excel_obj: pandasFileService = pandasFileService()
    df_2010_and_after = mydf_excel_obj.get_excel_file(excel_name).filter(regex='^201.')
    print(df_2010_and_after)


def subset_row_task_3() -> None:
    csv_name: str = "rainfall-monthly-total"
    mydf_excel_obj: pandasFileService = pandasFileService()
    df_rainfall = mydf_excel_obj.get_csv_file(csv_name)

    df_rainfall_more_than_300 = df_rainfall[df_rainfall['total_rainfall'] > 300].sort_values(by=["total_rainfall"])
    df_rainfall_more_than_300.plot(kind="bar")
    plot.xticks(rotation=45)
    plot.show()


def subset_row_task_4() -> None:
    excel_name: str = "singstats_maritalstatus"
    mydf_excel_obj: pandasFileService = pandasFileService()
    mydf = mydf_excel_obj.get_excel_file(excel_name)

    original_dataset_msg: str = " First 10 rows of original dataset "
    removed_na_dataset_msg: str = " Remaining dataset after dropping columns with missing data "

    print_header_with_stars(original_dataset_msg)
    print(mydf.head(10))
    print("\n")

    print_header_with_stars(removed_na_dataset_msg)
    mydf_2 = mydf.replace("-", nan)
    print(mydf_2.dropna(axis="columns").head(10))


if __name__ == '__main__':
    # subset_column_task_3()
    # subset_column_task_4()
    # subset_row_task_3()
    subset_row_task_4()
