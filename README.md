# Wedibooks Project 📚
>
>[시현 영상](https://youtu.be/lOiYYq0XvAc)

### [팀명] : Wedibooks (위디북스)

- [Redibooks](https://ridibooks.com/) 웹 사이트를 모티브로 한 팀 프로젝트
- 짧은 프로젝트 기간동안 개발에 집중해야하므로 디자인/기획 부분만 클론했습니다.
- 개발은 초기 세팅부터 전부 직접 구현했으며, 실제 사용할 수 있는 서비스 수준으로 개발한 것입니다.

## 개발 기간 및 인원
- 개발기간 : 2021/11/01 ~ 2021/11/12
- 개발 인원 : Front-End 4명, Back-End 2명
- 담당 분야 : Back-End 개발

## github repository
- [Front-End Repository](https://github.com/wecode-bootcamp-korea/26-1st-Wedibooks-frontend.git)

- [Back-End Repository](https://github.com/wecode-bootcamp-korea/26-1st-Wedibooks-backend.git)

## 적용 기술 및 역할
### 적용 기술
> - Back-End : Django, Python, MySQL, JWT, bcrypt, AWS(EC2, RDS)
> - Common : Git, Github, Slack, Trello, dbdiagram, postman

### 역할 분담
#### 이용건
> Product
- 메인페이지 추천 도서, 신간 도서, 상위 평점 도서 필터링 리스트
- 카테고리별 도서 리스트 조회

#### 한화연
> 회원가입 / 로그인 기능 구현
- bcrypt 암호화, 회원가입, 로그인 유효성 검사
- JWT access token 전송
- Login Decorator

> Product
- 도서별 상세정보 조회 API

> Review
- 데코레이터, 정규식을 이용한 도서별 리뷰 등록 API
- 평점 계산 및
- 도서별 리뷰 리스트 API

## ERD
<img width="1020" alt="스크린샷 2022-01-12 오후 3 32 26" src="https://user-images.githubusercontent.com/89324683/149076101-105fb441-6c59-428f-8573-be5853f9ec69.png">

# Reference
- 이 프로젝트는 Redibooks 사이트를 참조하여 학습 목적으로 만들어 졌습니다.
- 실무수준의 프로젝트이지만, 학습용으로 만들어 졌기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제가 될 수 있습니다.
