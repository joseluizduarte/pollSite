from django.urls import path
from . import views

app_name = 'poll'
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:question_id>',views.question_detail,name='detail'),
    path('<int:question_id>/vote',views.vote,name='vote'),
    path('<int:question_id>/results',views.results,name='results'),
    path('suggestion',views.suggestion,name='suggestion'),
    path('random',views.randomQuestion,name='randomQuestion'),
]
