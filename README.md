# Spartamarket\_DRF

중고거래 마켓 구현을 위한 백엔드 API 개발 프로젝트입니다. Django Rest Framework(DRF)를 기반으로 구현되었으며, 사용자 인증 방식으로 JWT의 Bearer Token을 사용하였습니다. API 는 RESTful API 로 설계했습니다.

## **프로젝트 정보**

- **프로젝트명**: Spartamarket\_DRF
- **개발자**: 박성진
- **개발기간**: 2024년 12월 23일 – 2024년 12월 29일
- **사용 언어 및 프레임워크**: Python, Django Rest Framework
- **인증 방식**: JWT (Bearer Token)
- **커뮤니티 툴**: Postman, Figma, draw\.io

---

## 설치 및 실행

### 요구 사항

- Python 3.x
- Django 4.x
- MySQL 또는 SQLite (기본 DB는 SQLite)

### 설치 방법

1. 리포지토리 클론:

    ```bash
    git clone https://github.com/yourusername/orange-market.git
    ```

2. 가상 환경 설정 (선택 사항):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. 종속성 설치:

    ```bash
    pip install -r requirements.txt
    ```

4. 데이터베이스 마이그레이션:

    ```bash
    python manage.py migrate
    ```

5. 서버 실행:

    ```bash
    python manage.py runserver
    ```
---

## **주요 기능**

### **회원 관리 API**

#### **회원가입**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/accounts/`
- **Method**: `POST`
- **조건**:
  - 필수 입력: username, 비밀번호, 이메일, 이름, 닉네임, 생일
  - 선택 입력: 성별, 자기소개
- **검증**:
  - username과 이메일은 유일해야 함
  - 이메일 중복 검증 기능 지원
- **구현**: 데이터 검증 후 저장

#### **로그인**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/accounts/login/`
- **Method**: `POST`
- **조건**: 사용자명과 비밀번호 입력 필요
- **검증**: 사용자명과 비밀번호가 데이터베이스 기록과 일치해야 함
- **구현**: 성공 시 JWT 토큰 발급, 실패 시 적절한 에러 메시지 반환

#### **로그아웃**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/accounts/logout/`
- **Method**: `POST`
- **조건**: 로그인 상태 필요
- **구현**: 로그아웃 시 쿠키 정보에서 access 및 refresh 토큰 삭제

#### **프로필 조회**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/accounts/<str:username>`
- **Method**: `GET`
- **조건**: 로그인 상태 필요
- **검증**: 로그인한 사용자만 자신의 프로필 조회 가능
- **구현**: 사용자 정보를 JSON 형태로 반환

#### **회원정보 수정**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/accounts/<str:username>`
- **Method**: `PUT`
- **조건**:
  - 이메일, 이름, 닉네임, 생일 필수 입력
  - 성별, 자기소개 생략 가능
- **검증**:
  - 로그인한 사용자만 수정 가능
  - username과 이메일은 중복 불가
- **구현**: 데이터 검증 후 업데이트

#### **비밀번호 변경**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/accounts/password/`
- **Method**: `PUT`
- **조건**:
  - 기존 패스워드와 변경할 패스워드는 상이해야 함
- **검증**:
  - 패스워드 규칙 준수 검증
- **구현**: 검증 후 패스워드 업데이트

#### **회원 탈퇴**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/accounts`
- **Method**: `DELETE`
- **조건**: 로그인 상태에서 비밀번호 재입력 필요
- **검증**: 입력된 비밀번호가 기존 비밀번호와 일치해야 함
- **구현**: 검증 후 계정 삭제

#### **팔로우/팔로우 취소**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/accounts/admin/follow/`
- **Method**: `POST`
- **조건**: 본인 외 다른 유저에게만 사용 가능
- **검증**: 로그인 필요
- **구현**: 검증 후 해당 유저와 요청 유저 간 follow ManyToManyField 업데이트

---

### **상품 관리 API**

#### **상품 등록**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/`
- **Method**: `POST`
- **조건**:
  - 로그인 상태 필요
  - 제목, 내용, 상품 이미지 필수 입력
- **구현**: 새 상품 등록 및 DB 저장

#### **상품 목록 조회**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products`
- **Method**: `GET`
- **조건**: 로그인 상태 불필요
- **구현**:
  - 모든 상품 목록을 페이지네이션으로 반환
  - 제목, 유저명, 내용으로 필터링 가능

#### **상품 세부목록 조회**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/<int:productId>`
- **Method**: `GET`
- **조건**: 로그인 상태 불필요
- **구현**:
  - 상품에 대한 세부정보 노출

#### **상품 수정**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/<int:productId>`
- **Method**: `PUT`
- **조건**:
  - 로그인 상태 필요
  - 작성자만 수정 가능
- **검증**:
  - 요청자가 해당 게시글 작성자인지 확인
- **구현**: 입력된 정보로 기존 상품 데이터 업데이트

#### **상품 삭제**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/<int:productId>`
- **Method**: `DELETE`
- **조건**:
  - 로그인 상태 필요
  - 작성자만 삭제 가능
- **검증**:
  - 요청자가 해당 게시글 작성자인지 확인
- **구현**: 데이터베이스에서 해당 상품 삭제

#### **상품 검색**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/search/?q=Deep`
- **Method**: `GET`
- **조건**: 로그인 상태 불필요
- **구현**: 입력한 검색어(예시:Deep)를 API뷰에 쿼리 파라미터로 저장 후 db.model의 Q 클래스를 활용하여 상품목록 필터링

#### **페이지네이션 및 필터링**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/?page=2&sort=likes`
- **Method**: `DELETE`
- **조건**: 상품 목록 조회 시 적용
- **구현**:
  - 제목, 유저명, 내용으로 필터링하는 쿼리 생성 (sort)
  - page 쿼리값은 rest_framework의 PageNumberPagination 기능을 적용하여 상품목록 조회 시 페이지네이션으로 반환하도록 설정


#### **상품 좋아요/좋아요 취소 기능**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/<int:productID>/like/`
- **Method**: `POST`
- **조건**: 로그인 상태 필요
- **구현**:
  - 상품 모델에 like_users 이름의 ManytoMany 필드 추가 (상품 - 유저 객체 연결)
  - 상품 모델에 like_count 이름의 PositiveInteger 필드 추가 (기본값 : 0)
  - 좋아요 클릭 시 상품과 해당 유저 관계를 DB에 저장 및 like_count 값 변경
  - 동일한 엔드포인트로 같은 요청이 반복될때마다 관계형 DB 를 탐색하여 좋아요/취소 기능 반복

#### **카테고리 기능**

- **조건**:
  - Admin 계정만 카테고리 생성 가능
  - 일반 유저는 상품 등록 시 카테고리 연결 가능
- **구현**:
  - Category 모델 생성
  - 상품 모델에 categories 이름의 ManytoMany 필드 추가 (상품 - Category 객체 연결)
  - 상품 등록/수정 시 상품과 입력받은 카테고리 관계를 DB에 저장

#### **해시태그 기능**

- **조건**:
  - 모든 해시태그는 중복값이 없어야 함
  - 대소문자 구분 없이 동일하게 처리 (예: Apple, aPple, applE는 동일)
- **구현**:
  - Hashtag 모델 생성
  - 상품 Model에 hastags 이름의 ManytoMany 필드 추가 (상품 - Hashtag 객체 연결)
  - 유저가 상품 등록 시 해시태그를 추가하는 입력필드 추가 (hashtags_input)
  - 해당 raw input값을 utils.py 의 parse 함수를 사용해 리스트 형태로 변환
  - 상품 Model에 hashtag를 처리하는 add_hashtag 및 remove_hastag 메서드 생성
  - API 뷰함수에서 상품에 대한 등록, 수정이 이루어질때 해당 메서드를 적절히 사용

---
### **댓글 관리 API**

#### **댓글 조회**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/<int:productID>/comments/`
- **Method**: `GET`
- **조건**: 로그인 상태 필요
- **구현**:
  - 특정 상품에 해당하는 엔드포인트로 접근 시 댓글 조회

#### **댓글 생성**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/<int:productID>/comments/`
- **Method**: `POST`
- **조건**: 로그인 상태 필요
- **구현**:
  - body의 "content" 키값에 댓글 내용을 작성해서 요청

#### **댓글 수정**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/comments/<int:comment_pk>/`
- **Method**: `PUT`
- **조건**:
  - 로그인 상태 필요
  - 해당 유저가 댓글 작성자와 일치하는지 검증
- **구현**:
  - body의 "content" 키값에 댓글 내용을 작성해서 요청
  - 댓글 모델에 FK로 연결된 작성자(유저)와 해당 유저의 일치여부 검증 후 수정

#### **댓글 삭제**

- **Endpoint**: `http://127.0.0.1:8000/api/v1/products/comments/<int:comment_pk>/`
- **Method**: `DELETE`
- **조건**:
  - 로그인 상태 필요
  - 해당 유저가 댓글 작성자와 일치하는지 검증
- **구현**:
  - 댓글 모델에 FK로 연결된 작성자(유저)와 해당 유저의 일치여부 검증 후 삭제
---

## **ERD 및 설계 도구**

- **ERD 설계**: draw\.io
- **디자인 시안**: Figma
- **API 테스트**: Postman






## API 명세

[Postman API 문서 바로가기](https://web.postman.co/workspace/My-Workspace~1a4d4709-027e-4866-8258-a950a43470db/documentation/40621952-a418c3b2-e038-4306-91cd-4d7c66c407e6)

## 트러블슈팅

1. DELETE 요청 시 405 에러 발생
```
("http://127.0.0.1:8000/api/v1/products/comments/21) 해당 url 로 DELETE 요청 시, 아래 에러 발생
405 : Method GET not allowed.

원인 : url 의 마지막부분에 "/"가 없어서 GET 요청에 대한 처리 불가능
해결 : 마지막 부분에 "/" 를 추가하여 해결 (http://127.0.0.1:8000/api/v1/products/comments/21/)
```
2. 회원가입 시 타입에러
```
에러내용 : (TypeError at /api/v1/accounts/
Response.__init__() got an unexpected keyword argument 'status')
 - Response 를 잘못된 라이브러리에서 import 해서 발생
 (이전) from requests import Response
 (수정) from rest_framework.response import Response
 ```

3. 로그아웃 테스트 후 재차 로그인 시 접근 권한 에러 (401)
 - 로그아웃 시 사용자의 refresh 토큰을 블랙리스트에 등록하는 방식으로 토큰 무효화를 구현했는데, 재차 로그인할 때 토큰정보를 요구하는 상황이 발생
 (원인) 로그아웃 시 쿠키 정보에 포함된 토큰이 삭제되지 않아 서버가 해당 토큰을 인식하는 과정에서 인증 거부로 로그인 시 새로운 토큰 자체가 발급되지 않음
 (수정) 로그아웃 시, 해당 유저의 refresh 토큰을 블랙리스트에 등록하는 방식 대신 쿠키에 남아있는 access 와 refresh 토큰을 삭제하는 방식으로 구현하고, 회원가입 및 로그인 시 새 토큰을 발급받는 방식으로 수정

4. 아래의 경우 DB 삭제가 되지 않는다.
 - shell_plus 로 ORM이 실행중인 경우
 - 서버가 실행중인 경우

5. Article 모델에 author_id 필드를 추가하고 자동할당 시, POST 에서는 정상적으로 숫자값이 입력되는데 DB 에는 NULL 로 저장되는 현상
(원인) Article 모델에 실제로 추가되는 필드는 index가 아닌 User 객체이고, DB에 저장되는 컬럼명은 해당 객체의 id (author_id)를 자동으로 생성하여 저장하는 구조
(해결) Article 모델에 작성자 정보를 "author" 로 저장해서 해결

6. 댓글 작성자 (author) 에 대한 입력이 없어 발생하는 에러
 - author 외래키를 read_only 로 설정 후 serializer 저장 시 (author = request.user) 로 같이 선언하여 해결
 ```py
 # 이전 코드
 serializer.save(article=article)
 # 변경 코드
 serializer.save(article=article, author=request.user)
 ```

7. 상품, 댓글 작성자가 CustomUser 모델 형식의 외래키로 연결되어있어 각 게시글에 대한 작성자명(닉네임) 정보 관리가 어려운 문제.
(수정) 상품과 댓글의 author를 유저모델의 외래키 대신 해당 글을 작성한 유저의 닉네임으로 입력되도록 디커플링하는 방법을 생각했지만, 추후 글 작성자가 개인정보를 수정했을 때, 닉네임만으로는 해당 게시글의 작성자를 특정하기 어려운 이슈가 있어 디커플링 대신 author_nickname 컬럼을 상품,댓글 모델에 추가하는 방식으로 개선

8. Hash 태그 기능 추가 시 사용자로부터 받는 raw_input에 대한 데이터 처리 문제
1) 시리얼라이즈에서만 raw_input 필드를 임시로 추가하여 파싱 후 Many-to-Many 필드에 저장 (동적 관리)
2) 모델 필드(DB)에 raw_input 값에 대한 정보를 명시적으로 추가하여 관리
(선택방안) 추후 유저가 게시글 수정 시, 이전 해시태그 입력내용 중 파싱과정에서 입력 실수로 인해 누락된 정보가 발생할 가능성이 있기에, 유저 편의성을 고려하여 이전 입력내용을 저장하는 2번방식 선택

9. 상품 게시글 삭제/수정 시 이전에 저장되어있던 이미지가 images 폴더에 남아있는 현상
(수정) 모델의 save, delete 메서드를 오버라이딩하여 게시글 수정, 삭제 시 이전 이미지가 삭제되도록 변경

 ## 코드 리뷰

3. 로그아웃 기능 구현 중 예상되는 문제 (토큰 무효화 방법 사용 시)
(문제) 유저가 많아지고, 로그인/로그아웃이 반복될 때마다 blacklisted token정보가 DB에 계속 쌓일 가능성  
(수정) blacklisted token의 DB정보를 refresh 토큰의 유효기간을 고려하여 적절한 주기마다 지속적으로 초기화

5. 포스트맨에서 POST 등 요청 시에 자동으로 역슬래시 붙히는 기능이 있어서 url 이랑 postman 경로 설정에 역슬래시 모두 삭제 필요
6. 로그아웃 DELETE 요청시에는 또 슬래시를 빼니깐 405 에러 발생...

7. 로그아웃에서
```py
response.delete_cookie("access")
response.delete_cookie("refresh")
```

처리를 해줘도 재로그인 시 Auth설정을 No Auth로 하면 401 에러가 발생한다.
결국 현재는 해당 ID에 맞는 유효한 access 토큰이 있어야 로그인이 가능하고, 로그인이 완료되어야 새로운 토큰이 발급된다. 즉, 로그인을 다시하면 사용 가능한 access 토큰이 2개가 되지만, 쿠키에서는 이전에 발금된 토큰이 삭제되어 유효기간이 지나면 자동으로 expire되는 구조이다.  
결국 보안을 위해서는 로그아웃 시 해당 유저의 토큰을 blacklist에 등록하여 expire 시키고, 로그인 시에 access 토큰이 없어도 id 와 비밀번호만으로 로그인이 가능한 방법을 고민해서 개선해야 한다.