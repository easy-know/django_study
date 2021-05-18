from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Answer, Question

'''
annotate 함수는 Question 모델의 기존 필드인
author, subject, content, create_date, modify_date, voter에 질문의 추천 수에
해당하는 num_voter 필드를 임시로 추가해 주는 함수이다.

order_by 함수에 두 개 이상의 인자가 전달되는 경우 1번째 항목부터 우선순위를 매긴다.
즉, 추천 수가 같으면 최신순으로 정렬한다.
'''


def index(request):
    """
    pybo 목록 출력
    """
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

   # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count(
            'answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # page와 kw가 추가되었다.
    context = {'question_list': page_obj, 'page': page,
               'kw': kw, 'so': so}  # <------ so 추가

    return render(request, "pybo/question_list.html", context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    page = request.GET.get('page', '1')  # 페이지

    question = get_object_or_404(Question, pk=question_id)
    answer_list = Answer.objects.filter(question_id=question_id).annotate(
        num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    paginator = Paginator(answer_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question': question, 'answer_list': page_obj, 'page': page}
    return render(request, 'pybo/question_detail.html', context)
