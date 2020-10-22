from django.shortcuts import render,reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def signup(request):

    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid(): # 유효성검사
            user = signupform.save(commit=False) # 아직 db엔 저장하지마
            user.email = signupform.cleaned_data['email']
            user.nickname = signupform.cleaned_data['nickname']
            user.save()

            return HttpResponseRedirect(
                reverse("login") #회원가입 성공 시 login페이지로 전환
            )
    elif request.method == "GET":
        signupform = SignupForm()

    context = {"form":signupform}
    return render(request, "signup.html", context )



class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('memo:memolist') # generic view에서 사용하는 reverse방식
