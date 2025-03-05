from django.urls import path
from .views import get_users, add_user, login_user, forget_pass, answer_sec_question,update_password

urlpatterns = [
    path('users/', get_users, name= 'get_users'),
    path('users/signup',add_user , name= 'add_user'),
    path('users/login', login_user, name= "login"),
    path('users/forget_pass', forget_pass, name= "forget_pass"),
    path('users/answer_sec_question', answer_sec_question, name= "answer_sec_question"),
    path('users/update_password', update_password, name= "update_password")
]


