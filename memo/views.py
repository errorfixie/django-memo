from django.shortcuts import render
from django.http import HttpResponse
from .models import Usermemo
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
# Create your views here.

# 메모리스트
class MemoListView(ListView):
    model = Usermemo
    template_name = 'memo/memolist.html'
    context_object_name='memolist'

# 메모상세
class MemoDetailView(DetailView):
    model = Usermemo
    template_name = 'memo/memodetail.html'


# 메모등록
class MemoCreateView(CreateView):
    pass 

# 메모수정
class MemoUpdateView(UpdateView):
    pass

# 메모삭제
class MemoDeleteView(DeleteView):
    pass
