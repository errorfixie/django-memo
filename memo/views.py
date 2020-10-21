from django.shortcuts import render
from .models import Usermemo,Memo
from django.http import HttpResponseRedirect
from user.models import User
from .forms import MemoCreateForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

# 메모리스트
@login_required # 로그인일때만 실행가능
def MemoListView(request):

    memo_list = Usermemo.objects.filter(userNUM = request.user).order_by('-memoNUM')
    context = {} #템플릿에 보낼 변수 지정
    context['memolist'] = memo_list # Usermemo 값들은 'memolist'로 저장

    return render(request,"list.html",context)

@login_required
def MemoHomeView(request):
    
    context = {} #템플릿에 보낼 변수 지정
    context['now'] = datetime.datetime.now()

    if request.method == "POST": # POST로 들어오면
        # print(request.POST)
        # 폼에 넣은 값 변수로 저장
        contents = request.POST.get('contents')
        # print(title,contents)


        title, contents = contents.split("\n",1) # 엔터로 한번 나눠서, 들어온 contents중 첫줄은 title, 두번째줄부터는 contents로 변수저장
        # print("내용 :" ,contents)
        # print("제목 :",title)
        # request.POST['title'] = title
        # request.POST['contents'] = contents

        POST = {} # request.POST는 바꿀수없어서 새로 딕셔너리 만들었다.
        POST['csrfmiddlewaretoken'] = request.POST['csrfmiddlewaretoken']
        POST['title'] = title
        POST['contents'] = contents 
        # print(title,contents)
        form = MemoCreateForm(POST) # 들어온 값들을 MemoCreateForm에 넣어 객체생성
        # print(POST)
        
        if form.is_valid(): # 유효성검사
            form.save() # 저장

            
            if Memo.objects.filter(contents=contents).order_by('-memodate'): #contents가 같지만 가장 최신 데이터 객체
                memo = Memo.objects.filter(contents=contents).order_by('-memodate')[0]

                username = request.user

                # print(memo.memodate) # 변수확인
                # print(memo.title)
                # print(memo.contents)
                # print(memo.pk)
                # print(memo)
                # usermemo테이블에 userNUM, memoNUM 저장하기
                usermemo = Usermemo() # Usermemo객체 생성
                usermemo.userNUM = username 
                usermemo.memoNUM_id = memo.pk

                usermemo.save() 

                return HttpResponseRedirect('/memo/') 

            #데이터가 아무것도 없어서 memo가 None이면 그냥 리다이렉트
            return HttpResponseRedirect('/memo/') # 저장후 리다이렉트할 url 지정 
            

    else:
        form = MemoCreateForm() # POST가 아니면 그냥 폼만 보여줌

    memo_list = Usermemo.objects.filter(userNUM = request.user).order_by('-memoNUM') # 지금 접속중인 user것만 최신순으로 가져와!!

    # print(request.user) # 장고가 로그인할때 session정보를 통해 request.user에 username을 저장한다

    
    
    context['memolist'] = memo_list # Usermemo 값들은 'memolist'로 저장
    context['form'] = form # Form 값들은 'form'으로 저장


    return render(request,"home.html",context)

# ----------------------------------------------------------------------------------------------------------
