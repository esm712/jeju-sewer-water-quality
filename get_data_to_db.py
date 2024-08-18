import sqlite3
import json

def db_to_json(db_name, table_name, json_file_name):
    # 데이터베이스 연결
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # 테이블의 모든 데이터 선택
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    # 테이블의 컬럼명 가져오기
    column_names = [description[0] for description in cursor.description]
    
    # 데이터 변환 (각 행을 딕셔너리로 변환)
    data = [dict(zip(column_names, row)) for row in rows]
    
    # JSON 파일로 저장
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    # 데이터베이스 연결 종료
    conn.close()
