import os
import json
class Json_data:

    def __init__(self):
        self.file_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'login_data.json')


    def  all_json_data(self):
        lsit_json_data=[]
        with open(self.file_path,encoding='utf-8') as file:
            json_data=json.load(file)
            for  item in json_data:
                login_data = item.get('login_data')
                code = item.get('code')
                msg = item.get('msg')
                case_name = item.get('case_name')
                lsit_json_data.append((login_data,code,msg,case_name))
        return lsit_json_data



new_json_data=Json_data()
all_data=new_json_data.all_json_data()
print(all_data)

