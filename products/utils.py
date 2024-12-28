import re

def parse_hashtags(input_string):
    # 해시태그 파싱 로직 (특수문자 제거 및 유효성 검사 포함)
    raw_hashtags = re.split(r'[ ,]+', input_string)  # 공백과 ','로 구분
    valid_hashtags_list = []
    for tag in raw_hashtags:
        if tag.startswith('#'):
            # _와 모든 언어(유니코드 범위 내 문자) 허용, 그 외 특수문자 제거
            cleaned_tag = re.sub(r'[^a-zA-Z0-9_\w]', '', tag[1:])
            if cleaned_tag:  # 유효한 해시태그만 추가
                valid_hashtags_list.append(f"#{cleaned_tag.lower()}")
    return valid_hashtags_list


# def add_hashtags_to_article(article, input_hashtags_list):
#     valid_hashtags = set()  # set을 사용하여 중복 해시태그 제거
#     for hashtag in input_hashtags_list:
#         hashtag = hashtag.strip()
#         if hashtag and hashtag.startswith("#"):  # '#'이 포함된 해시태그만 처리
#             valid_hashtags.add(hashtag)  # 유효한 해시태그만 set에 추가

#     # 해시태그 객체가 이미 존재하는지 한 번만 확인하고, 필요한 해시태그를 생성
#     existing_hashtags = Hashtag.objects.filter(name__in=valid_hashtags)
#     existing_hashtags_set = set(existing_hashtags.values_list('name', flat=True))

#     new_hashtags = valid_hashtags - existing_hashtags_set  # 새로 추가해야 할 해시태그
#     hashtag_objects_to_create = [Hashtag(name=hashtag) for hashtag in new_hashtags]

#     # 새 해시태그가 있으면 한 번에 추가
#     if hashtag_objects_to_create:
#         Hashtag.objects.bulk_create(hashtag_objects_to_create)

#     # 기존 해시태그 객체와 새로 생성된 해시태그 객체 연결
#     for hashtag_name in valid_hashtags:
#         hashtag_obj, created = Hashtag.objects.get(name=hashtag_name)
#         article.hashtags.add(hashtag_obj)  # Hashtag 객체를 Article에 추가