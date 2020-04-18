from django.urls import path

from blog import views

urlpatterns=[
    path('',views.index),
    path('index/',views.index),
    path('blog/',views.blog,name='index'),
    path('blog/<int:id>/',views.blog_single,name='blog_single'),
    path('category/<int:id>/',views.categorys,name='category'),
    path('search/',views.search,name='search'),
    path('regroup/',views.regroup),
    path('regroup/<str:tag>',views.tag)
]