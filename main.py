from requestAPI import fetch_data_from_api
from formating import xml_to_json
from load_fields import load_fields_from_txt
from save_data_to_db import save_json_data_to_db
from get_data_to_db import db_to_json

def main():
    print('Starting process ...')
    xml_data = fetch_data_from_api('http://211.184.196.130/rest/JejuSewerWaterQDataService/getJejuSewerWaterQData/')
    fields = load_fields_from_txt('sewer_water_param.txt')
    json_data = xml_to_json(xml_data,fields)
    save_json_data_to_db('sewer_water_data',json_data,fields) # 클라우드 DB로 전환이 필요함
    db_to_json('sewer_water_data','sewer_water','sewer_water.json')

if __name__ == '__main__':
    main()