
TIP
```
html 에서 ! + TAB 시 html 기본포맷 자동완성
포맷터 설정 후 Alt+Shift+F 시 자동 포맷팅 (딕셔너리 정렬)
```

```bash
[Django 공식 사이트] (https://docs.djangoproject.com/en/4.2/)
[DRF 공식 사이트](https://www.django-rest-framework.org/)
[JWT 공식 사이트](https://jwt.io/)
<VS Code 단축키> https://demun.github.io/vscode-tutorial/shortcuts/

<터미널 명령어>
conda create -n venv python=3.12.7
pip install django==4.2

<DRF 관련>
pip install django-seed # settings.py의 INSTALLED_APPS에 추가 ("django_seed",)
python manage.py seed <앱이름> --number=20
pip install psycopg2
pip install djangorestframework # settings.py의 INSTALLED_APPS에 추가 ("rest_framework",)
pip freeze > requirements.txt
pip install djangorestframework-simplejwt #JWT 설치 + settings.py 추가
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

django-admin startproject OrangeMarket
python manage.py startapp accounts >> 이후 settings.py 에 앱 등록
python manage.py runserver
python manage.py createsuperuser
python manage.py changepassword <username>
python manage.py collectstatic
 >> settings.py 에 아래 구문 추가
    STATICFILES_DIRS = [BASE_DIR / "static"]
    STATIC_ROOT = BASE_DIR / "static/"

<DB 구조에 변경이 있을 때(model 수정 시)>
1. python manage.py makemigrations
2. python manage.py migrate

<Shell 문법으로 DB 수정>
pip install django-extensions >> 이후 settings.py 에 앱 등록
pip install ipython
pip freeze > requirements.txt
python manage.py shell_plus

<DB 활성화>
Ctrl+Shift+P 이후 선택

<이미지 처리 패키지 설치>
pip install pillow
```

```python
Shell 문법으로 DB 수정하기.

1. 매니저를 통한 Article 객체 생성 (DB 추가)
Article.objects.create(title='third title', content='마지막 방법임')
Article.objects.all()

2. DB 조회 구문 (단일 조회)
Article.objects.get(id=1)
Article.objects.get(content='my_content')

3. 조건 조회
Article.objects.filter(id__gt=2) # 2보다 큰 id 모두 조회
Article.objects.filter(id__in=[1,2,3]) # 1,2,3에 속하는 id 조회
Article.objects.filter(content__contains='my') # my가 포함된 content 조회

4. 특정 DB 수정/삭제
article = Article.objects.get(id=1)
article.title = 'updated title'
article.save() // article.delete()

5_1. 코멘트 추가
python manage.py shell_plus
article = Article.objects.get(pk=14)
Comment.objects.create(content="first commit", article=article)

5_2. 코멘트 추가
python manage.py shell_plus
article = Article.objects.get(pk=14)
comment = Comment()
comment.article = article
comment.content = "second commit"
comment.save()

6. article -> comment 역참조 (_set 사용 or related name 으로 별명 설정)
article.comment_set.all()
```


```
<HTTP 상태코드>

200 OK
- 성공 - 에러없이 요청이 성공.
201 Created
- 요청이 성공했고 새로운 데이터가 만들어짐.
202 Accepted
- 요청은 정상적이나 아직 처리가 완료되지 않음.
204 No Content
- 요청은 성공적으로 처리했으나 전송할 데이터(Response Body)가 없음.
 400 Bad Request
- 클라이언트의 요청이 잘못되었음.
- 서버는 해당 요청을 처리하지 않음.
401 Unauthorized
- 클라이언트가 인증이 되지 않았거나 인증정보가 유효하지 않음.
403 Forbidden
- 서버에서 요청을 이해했으나 금지된 요청.
- 요청에 대한 자원이 있으나 수행할 권한이 없음.
404 Not Found
- 요청한 자원을 찾을 수 없음.
500 Internal Server Error
- 요청에 대해 서버가 수행하지 못하는 상황.
- 서버가 동작하지 않는다는 포괄적인 의미가 내포됨.
503 Service Unavailable
- 서버가 요청을 처리할 준비가 되지 않았음.
- 서버가 다운되었거나 일시적으로 중단된 상태.
```
---
```
<URI의 구조> - https://www.aidenlim.dev:80/path/to/resource/?key=value#docs

- `https://`
- Scheme(Protocol)
    - 브라우저가 사용하는 프로토콜입니다.
    - http, https, ftp, file, …
        
- `www.aidenlim.dev`
- Host(Domain name)
    - 요청을 처리하는 웹 서버입니다.
    - IP 주소를 바로 사용할 수 있지만 도메인 이름을 받아서 사용하는 것이 일반적입니다.
        
- `:80`
- Port
    - 리소스에 접근할 때 사용되는 일종의 문(게이트)입니다.
    - HTTP: 80 / HTTPS: 443이 표준 포트입니다.
        
- `/path/to/resource/`
- Path
    - 웹 서버에서의 리소스 경로입니다.
    - 웹 초기에는 실제 물리적인 위치를 나타냈으나 현재는 추상화된 형태를 표현합니다.
        
- `?key=value`
- Query(Identifier)
    - 웹 서버에 제공하는 추가적인 변수입니다.
    - `&`로 구분되는 Key=Value 형태의 데이터입니다.
        
- `#docs`
- Fragment(Anchor)
    - 해당 자원 안에서의 특정 위치 (북마크)를 나타냅니다.
    - HTML 문서의 특정 부분을 보여주기 위한 방법입니다.
```

```
<쿼리셋(QuerySet)>
Django의 **쿼리셋(QuerySet)**은 데이터베이스로부터 가져온 객체 목록을 표현하는 데이터 구조입니다. 쉽게 말해, 쿼리셋은 데이터베이스에서 원하는 레코드(데이터 행)들을 가져오고, 이를 Python 객체 형태로 다룰 수 있게 해주는 것입니다.

<쿼리셋의 특징>

1. 데이터베이스의 레코드를 Python 객체로 표현
Article.objects.all() 같은 호출은 데이터베이스에서 Article 테이블의 모든 레코드를 가져와 쿼리셋에 담습니다.

2. 지연 평가(Lazy Evaluation):
쿼리셋은 즉시 데이터베이스에 쿼리를 실행하지 않고, 데이터가 실제로 필요할 때 실행됩니다.
예: list(articles)처럼 데이터를 명시적으로 사용할 때 데이터베이스에서 데이터를 가져옵니다.

3. 체이닝 가능:
여러 필터나 정렬을 메서드 체이닝으로 연결하여 원하는 결과를 점진적으로 만들어낼 수 있습니다.
예: Article.objects.filter(category="tech").order_by("-published_date")

# 모든 Article 객체 가져오기
articles = Article.objects.all()
print(articles)  # <QuerySet [<Article: Article 1>, <Article: Article 2>, ...]>

# 특정 조건 필터링
tech_articles = Article.objects.filter(category="tech")
print(tech_articles)  # <QuerySet [<Article: Tech Article 1>, <Article: Tech Article 2>]>

# 개수 세기
count = Article.objects.count()
print(count)  # 10 (예: 총 10개의 Article)

# 첫 번째 Article 가져오기
first_article = Article.objects.first()
print(first_article)  # <Article: Article 1>

# 리스트 형태로 변환
articles_list = list(articles)
print(articles_list)  # [<Article: Article 1>, <Article: Article 2>, ...]

<쿼리셋의 "실제 데이터" 예시>
articles = Article.objects.all()라고 했을 때, articles는 Python 리스트처럼 동작합니다. 하지만 실제로는 데이터베이스에서 가져온 객체들의 모음입니다.

articles의 데이터 구조:
<QuerySet [
    <Article: Article(title="First Post", published_date="2024-01-01")>,
    <Article: Article(title="Second Post", published_date="2024-01-02")>,
    <Article: Article(title="Tech News", published_date="2024-01-03")>
]>

<쿼리셋 원리>
1.매니저(Manager):
objects는 모델에 기본적으로 제공되는 Manager입니다.
이 매니저를 통해 데이터베이스와의 상호작용이 이루어집니다.

2. 매니저 메서드 호출:
all(), filter(), exclude() 같은 메서드는 SQL 쿼리를 생성하고 결과를 쿼리셋으로 반환합니다.

3. SQL 실행:
데이터를 실제로 사용할 때, 쿼리셋이 데이터베이스에 SQL을 실행해 결과를 가져옵니다.

Django에서 쿼리셋이 실행하는 SQL을 보려면 다음과 같은 방법을 사용할 수 있습니다:

# SQL 확인
from django.db import connection
articles = Article.objects.all()
print(articles.query)  # SELECT "app_article"."id", "app_article"."title", ...
```

OS 변경 시 주의사항
제어판 - 프로그램 - Windows기능 켜기/끄기 - Linux용 Windows 하위 시스템

```
재시작 시 Windows OS 관련 일부설정이 초기화되면서
 PowerShell 접근권한이 Retriced(default값)으로 변경된다.
 이를 다시 수정가능으로 변경해줘야 한다

해결방법 :
1. Get-ExecutionPolicy
2. Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
3. Y
```

view 처리방식 (HTTP, Json, DRF)
```
def json_01(request):
    articles = Article.objects.all()
    json_res = []

    for article in articles:
        json_res.append(
            {
                "title": article.title,
                "content": article.content,
                "created_at": article.created_at,
                "updated_at": article.updated_at,
            }
        )
    return JsonResponse(json_res, safe=False)

def json_02(request):
    articles = Article.objects.all()
    res_data = serializers.serialize("json", articles)
    return HttpResponse(res_data, content_type="application/json")

@api_view(["GET"])
def json_drf(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

DRF
```
FrontEnd : 클라이언트의 페이지 이동, 서버에 대한 요청을 처리
BackEnd : 요청된 값을 적절한 로직을 통해 serializer값과 HTTP 상태코드 반환

실제 클라이언트 웹에서 보여지는 구조.
1. 현재 클라이언트 URL
2. API의 urls.py에 선언되어있는 URL로 요청만 전송 (실제 클라 웹페이지는 변경 X)
3. API의 응답(상태코드) 확인 후 JS나 React 등에서 Redirect 된 다른 URL로 이동
```

역참조
```py
Django에서는 모델 클래스의 메타정보를 담고 있는 _meta 객체를 사용하여 모든 역참조 필드를 확인할 수 있습니다.

# Article 클래스의 역참조 필드들을 출력하는 함수
def get_reverse_related_fields(model):
    for field in model._meta.get_fields():
        if field.is_relation and field.auto_created and not field.concrete:
            print(f"역참조 필드 이름: {field.name}")
            print(f"참조하는 모델: {field.related_model.__name__}")
```

SerializerMethodField
```py
"""
MethodField로 정의된 변수명을 a라 하면,
get_a 함수를 생성해서 반환값으로 a에 설정
"""

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
```

## **02. JSON Web Token (JWT)**

### ✔️ JWT란 무엇인가요?

JWT는 다양한 장치에서 공통적으로 사용할 수 있는 **Token 기반 인증 방식** 중 하나로, 인증 데이터를 담은 토큰입니다.  
토큰 자체에 유저에 대한 간단한 정보가 포함되어 있으며, 이를 통해 인증을 처리합니다.

---

### Session & Cookie

#### ⭐ 쿠키 (Cookie)
- 웹 브라우저와 요청 및 응답 시 사용하는 데이터 조각
- 특정 도메인에 제한적이며 유효기간이 정해져 있음
- 인증(Auth) 외에도 다양한 방식으로 활용 가능

#### ⭐ 세션 (Session)
- **Stateless한 HTTP**의 특징을 보완하기 위한 방법
- 세션 DB를 이용해 유저 정보를 기억하고, **Session ID**를 쿠키에 담아 인증에 활용
- 쿠키를 사용해 세션 ID를 주고받는 방식

---

### JSON Web Token (JWT)

#### ✅ 간단 개요
- 쿠키는 웹 브라우저에서만 사용되지만, JWT는 다양한 장치에서 사용 가능
- JWT는 **랜덤한 문자열**로, 간단한 서명을 포함하며 유저 정보를 담고 있음
- JWT로 인증을 처리하면 세션 DB나 복잡한 인증 로직이 필요 없음

---

### JWT 인증 처리 방식

1. 클라이언트가 **ID/PW**를 서버로 전송
2. 서버는 **ID/PW**를 검증한 후, 유효하다면 서명 처리된 토큰을 클라이언트에 응답
3. 클라이언트는 **모든 요청 헤더에 토큰**을 포함해 서버로 전송
4. 서버는 토큰의 유효성을 검증한 뒤, 유저 신원과 권한을 확인해 요청을 처리

---

### 세션과 JWT의 차이점

| 구분   | 세션 방식                              | JWT 방식                              |
|--------|---------------------------------------|---------------------------------------|
| 데이터 | 세션 DB 필요                          | 토큰 자체에 인증 데이터 포함          |
| 처리   | 세션 DB에 저장된 데이터 확인          | 토큰 유효성만 검증                    |
| 확장성 | 상태 기반 (Stateful)                  | 무상태 기반 (Stateless)               |

---

### JWT의 장점과 단점

#### 🙆‍♂️ 장점
- 서버에서 별도의 데이터를 관리하지 않아 복잡한 처리 로직이 필요 없음
- 세션이나 DB 없이 유저 인증 가능

#### 💁‍♂️ 단점
- **로그아웃** 등 세션 관리가 어렵고, 모든 기기에서 로그아웃 처리 불가능
- 토큰이 탈취되면 보안에 취약

---

### JWT 구조

#### JWT는 `.`을 기준으로 **HEADER**, **PAYLOAD**, **SIGNATURE** 세 부분으로 구성됩니다.

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9. eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ. SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

#### 1. **HEADER**
- 토큰 타입 (예: JWT)과 서명 생성 알고리즘(예: HS256) 정보 포함

#### 2. **PAYLOAD**
- 토큰 발급자, 대상자, 만료 시간 등 여러 데이터 포함
- 유저의 최소한의 정보 저장 (예: 유저 ID 또는 PK)
- 민감한 정보는 담지 않음 (누구나 디코딩 가능)

#### 3. **SIGNATURE**
- `HEADER` + `PAYLOAD` + **비밀키**로 생성된 서명
- **유효성 검증**: 토큰이 위변조되지 않았는지 확인
- 서버는 토큰의 서명을 검증하여 유효한 요청인지 판단

---

### Access Token과 Refresh Token

#### 🔑 문제: 토큰 탈취 시 보안 문제
JWT 인증은 장점이 많지만, 탈취 시 보안에 취약합니다. 이를 해결하기 위해 **토큰 유효시간을 짧게 설정**하고, 두 종류의 토큰을 사용합니다.

#### ➡️ **Access Token**
- 인증 요청 시 헤더에 포함되는 토큰
- 만료 기한을 짧게 설정 (탈취 시 피해 최소화)

#### 🔃 **Refresh Token**
- Access Token이 만료되었을 때 새로운 Access Token을 발급받기 위한 토큰
- 더 긴 유효기간을 가짐
- 주로 클라이언트(기기)에 저장
- Refresh Token까지 만료되면 재인증 필요

#### Refresh Token 보안 강화
- Refresh Token은 DB를 이용해 관리 가능
  - 예: Blacklist 방식으로 탈취 방지

---

### 참고 사이트
- [JWT 공식 사이트](https://jwt.io/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)

Blacklist Token 설정 관련
```
<settings.py>
INSTALLED_APPS = ["rest_framework_simplejwt.token_blacklist",]
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

python manage.py migrate