from django.urls import path
from . import views
from .views import TeamList, TeamDetail, profile_list, SelectForm

urlpatterns = [
    path('',views.start, name='start'),
    path('home/', TeamList.as_view(), name='home'),
    path('team/<int:pk>',TeamDetail.as_view(), name='detail'),
    path('profile/<int:pk>', profile_list, name='profile'),
    path('find/',SelectForm.as_view(), name='find'),
]