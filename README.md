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