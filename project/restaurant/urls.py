from django.conf.urls import url
from restaurant import views

# urlpatterns = [
#     url(r'^booking/$', views.booking, name='booking     ')
# ]

urlpatterns = [
    url('booking/', views.BookListView.as_view(), name='booking'),
    url(r'^Create-table/$', views.create_tables, name='create_tables'),
    url(r'^Book-table/$', views.book_table, name='book_table'),
    url(r'^existing-time-check/$', views.existing_time_check, name='existing_time_check'),
]