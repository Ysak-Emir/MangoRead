from django.contrib import admin
from mango.models import *



class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "mango", "text", "time_create", "user")
    list_display_links = ("id", "user")
    search_fields = ("user",)
    list_per_page = 3


class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "profile_picture")
    list_display_links = ("id", "title")
    search_fields = ("title", "year", )
    list_per_page = 12


admin.site.register(Genres)
admin.site.register(GenreType)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Card, CardAdmin)


