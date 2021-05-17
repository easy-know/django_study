import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    '''
    "nl2br"은 줄바꿈 문자를 <br> 태그로 바꿔 주므로 <Enter>를 한 번만 눌러도 줄바꿈으로 인식한다. 만약 이 확장 도구를 사용하지 않으면 줄바꿈을 위해 줄 끝에 마크다운 문법인 스페이스를 2개를 연속으로 입력해야 할 것이다. "fenced_code"는 마크다운의 소스 코드 표현을 위해 적용했다
    '''
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))
