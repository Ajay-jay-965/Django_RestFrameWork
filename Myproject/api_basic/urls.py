from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='viewset')
router.register('generic', ArticleGenericViewSet, basename='genericviewset')
router.register('model', ArticleModelViewSet, basename='modelviewset')

urlpatterns = [
    # path('api/', article_list),
    path('api/', ArticleAPIView.as_view()),
    # path('api/<int:pk>/', article_detail),
    path('api/<int:id>/', ArticleDetails.as_view()),
    path('generic/api/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('viewset/', include(router.urls)),
    # path('viewset/', include(router.urls)),


]
