from django.urls import path,include
from gpt import views
urlpatterns = [
    path("",views.chat,name='index' ),
    path("chat/",views.chat, name ='chat')
]