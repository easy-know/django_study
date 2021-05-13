from django.urls import path

from . import views

app_name = 'pybo'  # 네임스페이스 추가하기

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),  # URL 별칭 사용하기
    path('answer/create/<int:question_id>/',
         views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/',
         views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         views.answer_delete, name='answer_delete'),
    path('comment/create/question/<int:question_id>/',
         views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/',
         views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/',
         views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/',
         views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/',
         views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/',
         views.comment_delete_answer, name='comment_delete_answer'),
    # 제네릭 뷰 테스트
    # path('', views.IndexView.as_view()),
    # path('<int:pk>/', views.DetailView.as_view()),
    #
]
