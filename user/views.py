from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView

from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request, 'home.html')


class UserJoinView(CreateView):
    pass

