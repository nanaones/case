## REST API 기능 


### 회사명 자동완성
회사명의 일부만 들어가도 검색됩니다.    

### 태그명으로 회사 검색  

관련된 회사가 검색됩니다.    
다국어로 검색이 가능합니다.    
일본어 태그로 검색을 해도 한국 회사가 노출이 됩니다.    
동일한 회사는 한번만 노출됩니다.      

---

### How to start
* standAlone  
별도 DB가 없으므로 Docker-compose 로 실행을 권장합니다.

```shell script
$ python3 -m pip install -r requirements.txt
$ python3 init.py
$ gunicorn --access-logfile ./log/logaccess_log --error-logfile ./log/error_log -b 0.0.0.0:80 -t 4 main:app

```

* docker-compose

```shell script
$ docker-compose up --build

```

* test
```shell script
$ python3 test.py
```


---

# API 명세서

## GET `<serverAddress>:80/company`
저장되어있는 회사의 전체의 정보를 리턴합니다.
- in Docker-compose  
http://localhost:80/company

## GET `<serverAddress>:80/company/<id:int>`
저장되어있는 id번째 회사의 정보를 리턴합니다.
- in Docker-compose  
http://localhost:80/company/(id:int)

## GET `<serverAddress>:80/tag`
저장되어있는 태그의 정보를 리턴합니다.
- in Docker-compose  
http://localhost:80/tag

## GET `<serverAddress>:80/tag/<id:int>`
저장되어있는 id번째 태그의 정보를 리턴합니다.
- in Docker-compose  
http://localhost:80/tag/(id:int)

## GET `<serverAddress>:80/search/company?companyName=<str>`
companyName 이 포함된 회사의 이름을 모두 리턴합니다.
- in Docker-compose  
http://localhost:80/search/company?companyName=(str)

## GET `<serverAddress>:80/search/tag?tagName=<str>`
tagName 로 태그되어있는 모든 회사들을 리턴합니다.
- in Docker-compose  
http://localhost:80/search/tag?tagName=(str)

## DELETE `<serverAddress>:80/company/<id:int>?tagName=<str>`
<id:int> 번째 회사의 tagName을 삭제합니다.
- in Docker-compose  
http://localhost:80/company/(id:int)?tagName=(str)

## POST `<serverAddress>:80/company/<id:int>?tagName=<str>`
<id:int> 번째 회사의 tagName을 추가합니다.  
- in Docker-compose  
http://localhost:80/company/(id:int)?tagName=(str)


---
## DB 

### Docker Compose   
![](/img/table.png)


총 7개의 테이블로 구성되어있습니다.

![](/img/table_detail.png)

---

## Tool Architecture Design

### Docker - Compose

1. python API Server
2. PostgreSQL
3. prometheus
4. prometheus - exporter [PostgreSQL]
5. Grafana

