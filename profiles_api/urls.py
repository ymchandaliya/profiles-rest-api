from django.urls import path
from profiles_api import views
urlpatterns = [
    path('',views.ProfileAPIView.as_view())

]
