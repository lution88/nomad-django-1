from django.db import models

# Create your models here.
# 여기가 데이의 모양을 django 에게 알려줘야 하는 곳이다.


class House(models.Model):
    """모델을 만들 때는 설명을 적어두자
    Model Definition for Houses
    """

    # shape of data
    name = models.CharField(max_length=140)
    # price - 양수
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
