import pandas as pd

from os import getcwd
from typing import List


class pandasFileService:
    def __init__(self):
        self.dataframe_csv = None
        self.dataframe_xls = None
        self.list_of_worksheets = None
        self.current_dir: str = getcwd()

    '''
        # Load excel data into file service
    '''

    def get_excel_file(self, excel_file_name: str, index_col: int = 0) -> pd.DataFrame:
        self.dataframe_xls = pd.read_excel(
            io=f"{self.current_dir}/dataset/{excel_file_name}.xlsx",
            index_col=index_col
        )
        self.list_of_worksheets: List[str] = self.dataframe_xls.keys().to_list()
        return self.dataframe_xls

    def get_list_of_worksheet(self) -> List[str]:
        assert type(self.list_of_worksheets) is not None
        return self.list_of_worksheets

    def get_csv_file(self, csv_file_name: str, index_col: int = 0) -> pd.DataFrame:
        self.dataframe_csv = pd.read_csv(
            filepath_or_buffer=f"{self.current_dir}/dataset/{csv_file_name}.csv",
            index_col=index_col
        )
        return self.dataframe_csv
