
<!-- ! + TAB 시 html 기본포맷 자동완성 -->

```bash
<Django 공식 문서> https://docs.djangoproject.com/en/4.2/
<VS Code 단축키> https://demun.github.io/vscode-tutorial/shortcuts/

<터미널 명령어>
conda create -n venv python=3.12.7
pip install django==4.2

<DRF 관련>
pip install django-seed # settings.py의 INSTALLED_APPS에 추가 ("django_seed",)
pip install psycopg2
pip install djangorestframework # settings.py의 INSTALLED_APPS에 추가 ("rest_framework",)
pip freeze > requirements.txt

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