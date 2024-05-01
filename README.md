
## * Description

   * ### Project name : Sparta Market 
Sparta Market Project를 DRF로 재구성

   * ### Project duration : 2024-04-12 ~ 2024-04-09
개인프로젝트2

## * Environment & Tech stack
Window 환경에서 Pycham 사용. 

Python(3.10) , Django Framework (4.2.11) , Bootstrap 사용

Database : SQLite3 


## * Prerequisite
Requirements.txt 참고

Package | Version

|----|----|----|----|

asgiref                       | 3.8.1      
backports.zoneinfo            | 0.2.1      
Django                        | 4.2.11     
django-environ                | 0.11.2     
django-seed                   | 0.3.1      
djangorestframework           | 3.15.1     
djangorestframework-simplejwt | 5.3.1      
Faker                         | 24.14.0    
pillow                        | 10.3.0     
pip                           | 24.0
psycopg2                      | 2.9.9
PyJWT                         | 2.8.0
python-dateutil               | 2.9.0.post0
setuptools                    | 68.2.0
six                           | 1.16.0
sqlparse                      | 0.5.0
toposort                      | 1.10
typing_extensions             | 4.11.0
tzdata                        | 2024.1
wheel                         | 0.41.2

## * Roadmap

- [x] 회원기능 (Accounts)
    - [x] 회원가입
    - [x] 로그인
    - [x] 토큰 Refresh
    - [x] 로그아웃
    - [x] 프로필페이지
    - [x] 프로필편집페이지
- [x] 게시글 기능 (Products)
  - [x] 게시글 CRUD(글 제목, 내용, 이미지, 가격)
  - [x] 로그인 한 경우만 게시글수정삭제가능
  - [x] 로그인 한 경우 중 작성자와 일치한 경우만 수정삭제가능


## * Use

Post Man 이미지 참고