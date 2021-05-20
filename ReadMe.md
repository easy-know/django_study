### Python 및 Django Study

---

### 📌 개발 기간

##### 기간: 2021. 05. 03 ~ 2021. 05. 21



### 📌 개발 준비

- 파이썬 설치

  1. 공식 홈페이지에서 [Download] 메뉴를 누르고 환경에 맞는 파일 설치
  2. 설치 과정에서 파이썬 경로 추가
  3. 설치 확인
     - CMD: python -V

- 장고 개발 환경 준비

  1. 가상 환경 생성

     - python -m venv [가상 환경 이름]

  2. 가상 환경 진입

     - cd .venvs\[가상 환경 이름]\Scripts\
     - activate

     ✅ 가상 환경에서 벗어나기: deactivate

     ✅ 가상 환경에 간단히 진입하기(https://wikidocs.net/72377)

  3. 장고 설치(가상 환경에서)

     - pip install django

- 장고 프로젝트 생성 (가상 환경에서)

  1. 장고 프로젝트 생성하기
     - django-admin startproject config .

- 개발 서버 구동하기 웹 사이트에 접속하기

  1. 개발 서버 구동하기
     - python [manage.py](http://manage.py) runserver
  2. 개발 서버 종료하기
     - Ctrl + C
