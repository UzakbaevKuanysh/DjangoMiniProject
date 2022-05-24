from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns


from lolo.views import  BookViewSet, BookViewSet_detail, JournalViewSet, JournalViewSet_detail
app_name = 'lolo'




book = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = BookViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})

journal = JournalViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
journal_detail = JournalViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})

urlpatterns = [
    
    path('book', book, name ='book'),
    path('book/<int:pk>', book_detail, name="book_detail"),

    path('journal', journal, name ='journal'),
    path('journal/<int:pk>', journal_detail, name="journal_detail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)