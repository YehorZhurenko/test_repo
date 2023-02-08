from django import views
from django.urls import path
from .views import PostList, PostDetail, venue_pdf

urlpatterns = [

    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('venues_pdf/<int:pk>', venue_pdf, name = 'venue_pdf'),

]
