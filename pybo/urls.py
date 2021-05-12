from django.urls import path

from . import views

app_name = 'pybo'  # 네임스페이스 추가하기

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),  # URL 별칭 사용하기
    path('answer/create/<int:question_id>/',
         views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

    # 제네릭 뷰 테스트
    # path('', views.IndexView.as_view()),
    # path('<int:pk>/', views.DetailView.as_view()),
    #
]
