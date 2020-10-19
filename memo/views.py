from django.shortcuts import render
from .models import Usermemo,Memo
from django.http import HttpResponseRedirect
from user.models import User
from .forms import MemoCreateForm
from django.urls import reverse,reverse_lazy
# Create your views here.

# 메모리스트
def MemoListView(request):

    memo_list = Usermemo.objects.filter(userNUM = request.user).order_by('-memoNUM')
    context = {} #템플릿에 보낼 변수 지정
    context['memolist'] = memo_list # Usermemo 값들은 'memolist'로 저장

    return render(request,"list.html",context)

    
def MemoHomeView(request):
    
    if request.method == "POST": # POST로 들어오면
        form = MemoCreateForm(request.POST) # 들어온 값들을 MemoCreateForm에 넣어 객체생성

        if form.is_valid():
            form.save() # 저장

            # 폼에 넣은 값 변수로 저장
            title = request.POST.get('title')
            contents = request.POST.get('contents')
            
            if Memo.objects.filter(title=title, contents=contents).order_by('-memodate'):
                memo = Memo.objects.filter(title=title, contents=contents).order_by('-memodate')[0]
            else:
                memo = Memo.objects.filter(title=title, contents=contents).order_by('-memodate') # title과 contents가 같지만 가장 최신 데이터 객체
            username = request.user

            # print(memo.memodate) # 변수확인
            # print(memo.title)
            # print(memo.contents)
            # print(memo.pk)
            
            # usermemo테이블에 userNUM, memoNUM 저장하기
            usermemo = Usermemo() # Usermemo객체 생성
            usermemo.userNUM = username 
            usermemo.memoNUM_id = memo.pk
            usermemo.save() 

            return HttpResponseRedirect('/memo/') # 저장후 리다이렉트할 url 지정

    else:
        form = MemoCreateForm() # POST가 아니면 그냥 폼만 보여줌

    memo_list = Usermemo.objects.filter(userNUM = request.user).order_by('-memoNUM') # 지금 접속중인 user것만 최신순으로 가져와!!

    # print(request.user) # 장고가 로그인할때 session정보를 통해 request.user에 username을 저장한다

    context = {} #템플릿에 보낼 변수 지정
    context['memolist'] = memo_list # Usermemo 값들은 'memolist'로 저장
    context['form'] = form # Form 값들은 'form'으로 저장


    return render(request,"home.html",context)

# ----------------------------------------------------------------------------------------------------------
