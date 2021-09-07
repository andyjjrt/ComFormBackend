from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import auth

from util.api import APIResponse

import json
import re 

class Login(View):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        username = body["username"]
        password = body["password"]
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return APIResponse.success("succeed")
        else:
            return APIResponse.error("Invalid username or password")

class Logout(View):
    def get(self, request):
        auth.logout(request)
        return APIResponse.success("succeed")

class Register(View):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        username = body["username"]
        password = body["password"]
        email = body["email"]
        if len(str(username)) < 6 or len(str(username)) > 12:
            return APIResponse.error("username must between 6 ~ 12 letters")
        if len(str(password)) < 6:
            return APIResponse.error("password must be 6 letters or more")
        if not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):   
            return APIResponse.error("invalid email")

        try:
            user = auth.models.User.objects.create_user(username, email, password)
            user.save()
            return APIResponse.success("succeed")
        except:
            return APIResponse.error()

class Profile(View):

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        if request.user.is_authenticated:
            userform = []
            for i in request.user.form_set.all():
                userform.append(i.dict())
            data = {
                "username": request.user.username,
                "email": request.user.email,
                "forms": userform
            }
            return APIResponse.success(data)
        else:
            return APIResponse.success({})