from django.urls import  path
from Books.views import *

urlpatterns = [
    path('',homepage,name="home_page"),
    path('product/<str:id>',product_page,name="product_page"),
    path('preview_pdf/<str:pdf_id>', preview_pdf, name="preview_pdf"),
    path('register/',register, name='register'),
    path('login/',login_view, name='login'),
    path('logout/',LogoutUser, name='logout'),
    path('book/create/', book_create_view, name='book_create'),
    path('author/create/', create_author, name='create_author'),


]
