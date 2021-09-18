# a='sdf1jk1kgh1jj1f'
# c=a.split('1')
# print(c)
# D=a.replace('1','？')
# print(D)

import os
from openpyxl  import  load_workbook

class Exel:

    def  __init__(self,file,form):
        loading_excel=load_workbook(file)
        self.excel_form=loading_excel[form]


    def read_excel_titel(self):
        titel=[]
        for  item  in  list(self.excel_form.rows)[0]:
            titel.append(item.value)
        return titel


    def  all_excel_data(self):
        all_list_data=[]
        for item in list(self.excel_form.rows)[1:]:
            list_data=[]
            for r_item  in item:
                list_data.append(r_item.value)
            all_list_data.append(dict(zip(self.read_excel_titel(),list_data)))
        return all_list_data




new_excel=Exel('excel.xlsx','case')
new_list=new_excel.all_excel_data()
print(new_list)