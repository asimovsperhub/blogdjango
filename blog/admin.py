from django.contrib import admin

# Register your models here.


from blog.models import Blog, Tag, Category

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Category)