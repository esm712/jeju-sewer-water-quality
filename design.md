1. API를 요청하고 데이터를 가져온다.(실시간 수질데이터 API 사용)
2. xml 규격을 json 규격으로 변경한다.
2. json 데이터를 database에 저장한다.(SQLite database 사용)
3. database의 데이터를 json 파일로 저장한다.(jeju_water_quality.json 사용)
4. js 파일에서 json파일을 사용하여 차트를 그린다.(char.js 사용)

## 왜 데이터베이스를 사용하는가?
> 프로젝트에서 차트를 그리기위해서는 누적 데이터가 필요하기 때문에(단발적인 실시간 데이터를 누적할 필요성이 있음)

