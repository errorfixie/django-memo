from django.shortcuts import render
from django.http import HttpResponse
from .models import Usermemo,Memo
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .forms import MemoCreateForm
# Create your views here.

# 메모리스트
class MemoListView(ListView):
    model = Usermemo
    template_name = 'list.html'
    context_object_name='memolist'


class MemoHomeListView(ListView):
    model = Usermemo
    template_name = 'home.html'
    context_object_name='memolist'

# 메모상세
class MemoDetailView(DetailView):
    model = Usermemo
    template_name = 'memo/memodetail.html'


# 메모등록
class MemoCreateView(CreateView):
    form_class = MemoCreateForm
    template_name = 'memo/memocreate.html'

    def get_success_url(self):
        return reverse('memo:detail', args=[self.object.pk])

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
