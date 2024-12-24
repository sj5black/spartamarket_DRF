# spartamarket_DRF
Django 와 RESTful API 를 활용한 중고거래 마켓 DRF 구현

# 트러블슈팅
```
("http://127.0.0.1:8000/api/v1/products/comments/21) 해당 url 로 DELETE 요청 시, 아래 에러 발생
405 : Method GET not allowed.

원인 : url 의 마지막부분에 "/"가 없어서 GET 요청에 대한 처리 불가능
해결 : 마지막 부분에 "/" 를 추가하여 해결 (http://127.0.0.1:8000/api/v1/products/comments/21/)
```