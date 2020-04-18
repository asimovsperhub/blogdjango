from django.urls import path

from comment import views

urlpatterns=[
    path('comment/<int:id>',views.comment,name='comment'),
]