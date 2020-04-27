# polls/urls.py
from django.urls import path

from . import views

app_name = 'polls'      # 앱의 이름공간을 지정
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'), (함수뷰->클래스뷰 이름 형태로 바뀜)
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'), 제네릭뷰가 포착하기로 한 이름을 pk로 바꿔줌
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]