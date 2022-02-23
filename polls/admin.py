from django.contrib import admin
from polls.models import Horse, Cat, Article
# Register your models here.

admin.site.register(Horse)
admin.site.register(Cat)
admin.site.register(Article)