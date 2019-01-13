from django.conf.urls import url
from . import views

urlpatterns = [
    # r : 뒤에 특수문자가 올수 있다는 뜻
    # ^ : 시작
    url(r'^$', views.post_list, name='post_list'),
    # post/ : url에 post/가 필요하다는 뜻
    # \d : 숫자 0 ~ 9만 가능
    # \d+ : 숫자가 하나 또는 그 이상
    # /$ : 마지막에 /으로 끝나야 한다는 뜻
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]

