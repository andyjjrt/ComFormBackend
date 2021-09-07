from django.views.generic.base import View

from util.api import APIResponse
from api.models import Form as FormModel

import json

class Get(View):
    def get(self, request):
        form_id = request.GET.get('id')
        form = FormModel.objects.get(id=form_id)
        return APIResponse.success(form.dict())

class Create(View):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        title = body['title']
        description = body['description']
        if request.user.is_authenticated:
            form = FormModel(title=title, description=description, author=request.user)
            form.save()
            return APIResponse.success("succeed")
        else:
            return APIResponse.error("Please login first")

class Delete(View):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        id = body['id']
        if id == "":
            return APIResponse.error('id cannot be blank')
        if request.user.is_authenticated:
            try:
                form = FormModel.objects.get(id=id)
                if form.author == request.user:
                    form.delete()
                    return APIResponse.success("succeed")
                else:
                    return APIResponse.error("You can't delete a form that is not yours")
            except:
                return APIResponse.error()
        else:
            return APIResponse.error("Please login first")