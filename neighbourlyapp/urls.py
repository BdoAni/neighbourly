from django.urls import path
from .import views

urlpatterns=[
    #############Display Paths########
    path('', views.displayhome),
    path('dashboard', views.displaydashboard), #changed displaysuccess to displaydashboard
    #############Action Paths########
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
################################################################
    path('new', views.newtool),
    path('submit', views.submittool),
    path('edit', views.displayedittool),
    path('revise', views.revisedtool),
    path('search', views.searchtools),
    path('show', views.showalltools),
    path('display', views.thistool),
    path('accepted', views.acceptedtools), 
    path('delete/<int:tool_id>', views.deletethistool),
]
