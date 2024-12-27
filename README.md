# spartamarket_DRF
Django 와 RESTful API 를 활용한 중고거래 마켓 DRF 구현

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

5. 포스트맨에서 POST 등 요청 시에 자동으로 역슬래시 붙히는 기능이 있어서 url 이랑 postman 경로 설정에 역슬래시 모두 삭제 필요

 ## 코드 리뷰

3. 로그아웃 기능 구현 중 예상되는 문제 (토큰 무효화 방법 사용 시)
(문제) 유저가 많아지고, 로그인/로그아웃이 반복될 때마다 blacklisted token정보가 DB에 계속 쌓일 가능성  
(수정) blacklisted token의 DB정보를 refresh 토큰의 유효기간을 고려하여 적절한 주기마다 지속적으로 초기화