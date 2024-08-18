import sqlite3

def save_json_data_to_db(db_name, data, fields):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    print(f"Database file location: {db_name}")

    field_definitions = ", ".join(fields)
    # 테이블이 존재하지 않으면 생성
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS sewer_water (
        {field_definitions}
    )
    ''')
    
    # 필드 이름만 추출하여 INSERT 쿼리 구성
    field_names = ', '.join([field.split()[0] for field in fields])
    placeholders = ', '.join(['?' for _ in fields])
    
    # 데이터 삽입
    for entry in data:
        cursor.execute(f'''
        INSERT INTO sewer_water ({field_names})
        VALUES ({placeholders})
        ''', tuple(entry[field.split()[0]] for field in fields))
    
    conn.commit()
    conn.close()

#         id INTEGER PRIMARY KEY AUTOINCREMENT,