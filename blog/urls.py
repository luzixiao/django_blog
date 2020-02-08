from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # 第一个参数是网址，第二个参数是处理函数， 第三个参数是处理函数的别名
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>', views.category, name='category'),
    path('tags/<int:pk>', views.tag, name='tag'),
]
