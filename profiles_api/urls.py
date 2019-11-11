from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Hello-Viewset',views.ProfileViewSet,base_name='Hello-ViewSet')
router.register('profile',views.UserProfileViewset)
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view',views.ProfileAPIView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),

]
