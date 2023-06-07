from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('children/', views.children_index, name='index'),
    path('children/<int:child_id>/', views.children_detail, name='detail'),
    path('children/create/', views.ChildCreate.as_view(), name='child_create'),
    # path('children/<int:user_id>/add_child', views.add_child, name='add_child'),
    path('children/<int:child_id>/assoc_book/<int:book_id>', views.assoc_book, name='assoc_book'),
    path('children/<int:child_id>/disassoc_book/<int:book_id>', views.disassoc_book, name='disassoc_book'),
    path('children/<int:pk>/update/', views.ChildUpdate.as_view(), name='child_update'),
    path('children/<int:pk>/delete/', views.ChildDelete.as_view(), name='child_delete'),
    path('books/', views.books_index, name='books_index'),
    path('books/', views.BookList.as_view(), name='books_index'),
    # path('books/<int:pk>/', views.BookDetail.as_view(), name='books_detail'),
    path('books/<int:book_id>/', views.books_detail, name='books_detail'),
    
    path('books/<int:book_id>/add_review/', views.add_review, name='add_review'),
    
    path('accounts/singup', views.signup, name='signup'),
    

]