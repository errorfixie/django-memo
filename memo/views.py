from django.shortcuts import render, redirect
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

        # 폼에 넣은 값 변수로 저장
        contents = request.POST.get('contents')
        # print(title,contents)

        # title, contents
        # 그냥 공백일경우
        # 하나만 공백일 경우
        # print(contents)
            
        if contents: # 하나만 공백일 경우
            if "\n" in contents: 
                try: # split 된다면 엔터로 한번 나눠서, 들어온 contents중 첫줄은 title, 두번째줄부터는 contents로 변수저장
                    title, contents =  contents.split("\n",1)
                except: #title이 공백일 경우
                    title, contents = None, contents
                
            elif "\n" not in contents: # contents가 공백일 경우
                title, contents = contents, None
                
        else: # 그냥 공백일 경우
            title, contents = None, None

        # print(request.POST)
        if request.POST.get('pk'): # pk값이 있으면 메모데이터를 수정
            pk = request.POST.get('pk')
            post_memo = Memo.objects.get(pk=pk)
            # print(title, contents)
            # print(post_memo)
            post_memo.title = title
            # print(post_memo.title)
            # print(post_memo.contents)
            post_memo.contents = contents
            post_memo.save() # 새로운 값으로 수정

            return HttpResponseRedirect('/memo/?pk={}'.format(pk)) # 수정완료 후 해당페이지로

        else: 
            ##pk값이 없으면 새로운 저장 = > 새로 저장안하려면 else문 지우면됨
            
            # print(title, contents)
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

                
                if Memo.objects.order_by('-memodate'): #가장 최신 데이터 객체
                    memo = Memo.objects.order_by('-memodate')[0]

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

                    return HttpResponseRedirect('/memo/?pk={}'.format(memo.pk)) 

                #데이터가 아무것도 없어서 memo가 None이면 그냥 리다이렉트
                
                return HttpResponseRedirect('/memo/') # 저장후 리다이렉트할 url 지정 
            

    else:
        if not request.GET: # get으로 아무것도없으면
            form = MemoCreateForm() # POST가 아니면 그냥 폼만 보여줌
        # print(request.GET)
        else: #get으로 무엇인가 받으면
            pk = request.GET.get('pk')
            # print(pk)
            memo_pk = Memo.objects.get(id=pk)
            # print(memo_pk.title)
            # print(memo_pk.contents)
            contents = memo_pk.title + "\n" + memo_pk.contents
            # print(contents)
            GET = {}
            # POST[title] = memo_pk.title
            GET['contents'] = contents
            form = MemoCreateForm(GET)

            context['pk_memodate'] = memo_pk.memodate
            context['pk_memoupdate'] = memo_pk.memoupdate # 수정날짜, 저장날짜 템플릿에 보내기
            context['pk'] = pk
    memo_list = Usermemo.objects.filter(userNUM = request.user).order_by('-memoNUM') # 지금 접속중인 user것만 최신순으로 가져와!!

    # print(request.user) # 장고가 로그인할때 session정보를 통해 request.user에 username을 저장한다

    
    
    context['memolist'] = memo_list # Usermemo 값들은 'memolist'로 저장
    context['form'] = form # Form 값들은 'form'으로 저장


    return render(request,"home.html",context)

@login_required 
def MemoDeleteView(request): # 삭제기능 => pk값을 받아 구현할 것인지 아니면 request에 pk값이 없으면 최근데이터부터 삭제 있으면 그 데이터삭제
    if request.POST.get('pk'): # 포스트방식으로 pk값을 받으면
        pk = request.POST.get('pk')
        memo = Memo.objects.get(pk=pk)
        memo.delete()
        return redirect('memo:homelist')
    # pk값을 받지 않고 그냥 호출된다면
    if Usermemo.objects.filter(userNUM = request.user).order_by('-memoNUM'):
        usermemo = Usermemo.objects.filter(userNUM = request.user).order_by('-memoNUM')[0]
        memo_id = usermemo.memoNUM_id
        memo = Memo.objects.get(pk=memo_id)
        memo.delete()
        return redirect('memo:homelist')
    return redirect('memo:homelist') # 리스트가 없다면 그냥 리다이렉트

@login_required 
def MemoCreateView(request):
    memo = Memo()
    # memo.pk
    # print(memo.pk)
    memo.save()

    memo = Memo.objects.order_by('-memodate')[0]

    usermemo = Usermemo()
    usermemo.userNUM = request.user
    usermemo.memoNUM_id = memo.pk
    usermemo.save()

    return HttpResponseRedirect('/memo/?pk={}'.format(memo.pk))
# ----------------------------------------------------------------------------------------------------------
