import xml.etree.ElementTree as ET

def xml_to_json(xml_data, fields):
    root = ET.fromstring(xml_data)
    json_data = []
    
    for list_item in root.findall('.//list'):
        entry = {}
        for field in fields:
            field_name, *field_type = field.split()
            value = list_item.find(field_name).text

            # 필드 타입이 float으로 지정된 경우 변환
            if field_type and field_type[0] == 'REAL':
                entry[field_name] = float(value)
            else:
                entry[field_name] = value
        json_data.append(entry)
    
    return json_data