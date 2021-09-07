from django.urls import path
from api.views import account, form

urlpatterns = [
    path('login/', account.Login.as_view(), name="login"),
    path('logout/', account.Logout.as_view(), name="logout"),
    path('register/', account.Register.as_view(), name="register"),
    path('profile/', account.Profile.as_view(), name="profile"),
    
    path('form/', form.Get.as_view(), name="Form Get"),
    path('form/create', form.Create.as_view(), name="Form Create"),
    path('form/delete', form.Delete.as_view(), name="Form Delete")
]