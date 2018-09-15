import xlwings as xl

work_book = xl.Book('fish.xlsx')
data_range = work_book.sheets('fish1').range('b3:c228')
data = data_range.value

with open('data.actorId', 'w') as dst:
    dst.writelines('<actor>')
    dst.writelines('\n')
    for id_str in data:
        actor_id = str(int(id_str[0]))
        actor_str = id_str[1]
        format_str = '<actor id = "{}" str = "{}"/>'.format(actor_id, actor_str)
        dst.write('\t')
        dst.write(format_str)
        dst.write('\n')
    dst.writelines('</actor>')


