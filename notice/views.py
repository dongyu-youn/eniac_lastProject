from django.shortcuts import render

from notice.models import Article


# Create your views here.


def notices(request):
    notice_list = Article.objects.all()
    context = {'notice_list': notice_list}
    return render(request, 'notice/notice.html', context)

def notice_detail(request, article_id):
    notice = Article.objects.get(id=article_id)
    context = {'notice': notice,
               'request': request}
    return render(request, 'notice/noticeDetail.html', context)