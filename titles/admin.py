from django.contrib import admin
from .views import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)