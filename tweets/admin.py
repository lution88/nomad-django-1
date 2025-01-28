from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import Like, Tweet


class ElonMuskFilter(SimpleListFilter):
    title = "Elon Musk Mentions"
    parameter_name = "elon_musk"

    def lookups(self, request, model_admin):
        return (
            ("yes", "elon musk 포함"),
            ("no", "elon musk no 포함"),
        )

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.filter(payload_icontains="Elon Musk")
        else:
            return queryset.exclude(payload_icontains="Elon Musk")
        return queryset


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "payload",
        "user",
        "created_at",
        "updated_at",
        "likes",
    )
    list_filter = (
        ElonMuskFilter,
        "created_at",
        "payload",
        "user",
    )

    search_fields = ("created_at",)

    def likes(self, tweet):
        return tweet.likes.count()


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tweet",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
