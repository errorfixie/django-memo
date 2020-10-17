from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from .models import Usermemo,Memo
from user.models import User
from django.views.generic import ListView, FormView, DetailView, DeleteView, UpdateView, CreateView
from .forms import MemoCreateForm
from django.urls import reverse,reverse_lazy
# Create your views here.

# 메모리스트
class MemoListView(ListView):
    model = Usermemo
    template_name = 'list.html'
    context_object_name='memolist'

    
def MemoHomeView(request):
    
    if request.method == "POST": # POST로 들어오면
        form = MemoCreateForm(request.POST) # 들어온 값들을 MemoCreateForm에 넣어 객체생성
        form.save() # 저장

        return HttpResponseRedirect('/memo/') # 저장후 리다이렉트할 url 지정

    else:
        form = MemoCreateForm() # POST가 아니면 그냥 폼만 보여줌

    memo_list = Usermemo.objects.all() ## Usermemo모델에서 모든 항목가져와서 객체 만듬

    context = {} #템플릿에 보낼 변수 지정
    context['memolist'] = memo_list # Usermemo 값들은 'memolist'로 저장
    context['form'] = form # Form 값들은 'form'으로 저장


    return render(request,"home.html",context)

# ----------------------------------------------------------------------------------------------------------


# 메모상세
class MemoDetailView(DetailView):
    model = Usermemo
    template_name = 'memo/memodetail.html'
    
    

# 메모등록
class MemoCreateView(CreateView):
    form_class = MemoCreateForm
    template_name = 'home.html'

    def get_success_url(self):
        return reverse('memo:create')
    


# 메모수정
class MemoUpdateView(UpdateView):
    form_class = MemoCreateForm
    template_name ='memo/update.html'
    model = Memo

    def get_success_url(self):
        return reverse('memo:detail',args=[self.object.pk])

# 메모삭제
class MemoDeleteView(DeleteView):
    pass
