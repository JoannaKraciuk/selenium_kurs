import xlrd
from page_object_patern.utils.search_data import SearchData
class ExcelReader:

    @staticmethod
    def get_data():
        wb = xlrd.open_workbook("../utils/Dane3.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchData(sheet.cell_value(i, 0), sheet.cell_value(i, 1))
            data.append(search_data)
        return data




