from django.urls import path
#from blogging.views import stub_view, list_view
from blogging.views import list_view, detail_view

# urlpatterns = [path('', stub_view, name="blog_index"),
#               path('posts/<post_id>/', stub_view, name="blog_detail")]

#urlpatterns = [path('', list_view, name="blog_index"),
#               path('posts/<int:post_id>/', stub_view, name="blog_detail"),]

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]