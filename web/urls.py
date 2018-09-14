from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    #url('', views.index, name='index'),
    url('', views.post_list, name='post_list'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
