from django.urls import path
from . import views

urlpatterns = [
    # path('article',views.article_list),
    # path('articleno/<int:pk>',views.specificArticle)
    path('article',views.ArticleAPIView.as_view()),
    path('articleno/<int:id>',views.ArticleDetailAPIView.as_view()),
    path('generic/article/<int:id>/',views.GenericAPIView.as_view()),
]
