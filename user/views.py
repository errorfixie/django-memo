from django.shortcuts import render,reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
import requests


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


def KakaoSignInView(request):
    REST_API_KEY = "d9af7226a651272501b0326813ee20f8"
    REDIRECT_URI = "http://127.0.0.1:8000/kakao/login/callback"
    return HttpResponseRedirect(
        "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={}&redirect_uri={}".format(REST_API_KEY,REDIRECT_URI)
        )

class KakaoException(Exception):
    pass

def KakaoLoginCallback(request):
    
    if request.GET.get('error'): #에러가 나면 로그인페이지로 돌아가
        error = request.GET.get('error')
        return HttpResponseRedirect(reverse("login"))

    code = request.GET.get('code')
    REST_API_KEY = "d9af7226a651272501b0326813ee20f8"
    REDIRECT_URI = "http://127.0.0.1:8000/kakao/login/callback"

    token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={code}"
        )

    token_response_json = token_request.json()
    access_token = token_response_json.get('access_token')

    
    profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"}
            )

    profile_request_json = profile_request.json()
    user = profile_request_json.get('kakao_account')
    # print(profile_request_json)
    # print(user.get('profile').get('nickname'),user.get('email'))
    user_nickname, user_email = user.get('profile').get('nickname'), user.get('email')

    # 카카오 유저정보 바탕으로 장고db에 저장~~

    return HttpResponseRedirect(reverse("login"))