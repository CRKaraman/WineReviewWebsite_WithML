from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'reviews'
#型指定可能
urlpatterns = [
    path('review/', views.review_list,name = 'review_list'),
    path('wine/', views.wine_list, name='wine_list'),
    path('wine/<int:wine_id>/',views.wine_detail,name = 'wine_detail'),
    path('wine/<int:wine_id>/<int:review_id>',views.review_detail_of_wine,name = 'review_detail_of_wine'),
    path('wine/<int:wine_id>/add_review', views.add_review, name='add_review'),
    path('user/<username>/',views.user_review_list, name = 'user_review_list'),
    path('recommendation/',views.user_recommendation_list, name = 'user_recommendation_list')
]
