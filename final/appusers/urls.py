from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns


from appusers.views import  AppUserViewSet, AppUserViewSet_detail
app_name = 'lolo'




appuser= AppUserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
appuser_detail = AppUserViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})



urlpatterns = [
    
    path('', appuser, name ='appusers'),
    path('<int:pk>', appuser_detail, name="appuser_detail")

]
urlpatterns = format_suffix_patterns(urlpatterns)