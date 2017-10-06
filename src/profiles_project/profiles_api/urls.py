from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset', views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet,base_name='profile')
router.register('login',views.LoginViewSet,base_name='login')

urlpatterns=[
    url(r'^hello-view/',views.HelloAPIView.as_view()),
    url(r'',include(router.urls))
]
