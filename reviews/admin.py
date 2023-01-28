from django.contrib import admin
from .models import Review


class BadOrGoodFilter(admin.SimpleListFilter):
    title = "Good(rating > 3) or Bad(rating <= 3)"
    parameter_name = "good_or_bad"

    def lookups(self, request, models_admin):
        return (
            ("good", "Good"),
            ("bad", "Bad"),
        )

    def queryset(self, request, queryset):
        good_or_bad = self.value()
        if good_or_bad == "good":
            return queryset.filter(rating__gt=3)
        elif good_or_bad == "bad":
            return queryset.filter(rating__lte=3)
        else:
            return queryset


class WordFilter(admin.SimpleListFilter):
    title = "Word filters"
    parameter_name = "word"

    def lookups(self, request, models_admin):
        return (
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        )

    def queryset(self, request, queryset):
        word = self.value()
        if word:
            return queryset.filter(payload__contains=word)
        else:
            return queryset


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        BadOrGoodFilter,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
