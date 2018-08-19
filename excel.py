import xlwings as xl

work_book = xl.Book(r'test.xlsx')
data_range = work_book.sheets('sheet1').range('b1')
data_range.value = [1, 2, 3, 1,1,1,1,1,1]
work_book.save()


