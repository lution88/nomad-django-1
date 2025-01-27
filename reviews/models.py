from django.db import models

from common.models import CommonModel


class Review(CommonModel):
    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    # 유저가 남기는 텍스트: 리뷰 - payload
    payload = models.TextField(max_length=250)
    rating = models.PositiveIntegerField()  # 리뷰 평점

    def __str__(self):
        return f"{self.user} / {self.rating}⭐️"
