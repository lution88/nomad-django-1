from django.db import models


# DB 에 추가하지 않을 model: 재사용 model
class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Django 가 이 모델을 봐도 이걸 DB 에 저장하지 않는다

