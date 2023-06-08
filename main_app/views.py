from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from .models import Child, Book, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .data import data
from .forms import ReviewForm


# Create your views here.
# data = data()

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):

    books = Book.objects.all()
    return render(request, 'main_app/book_index.html',{'books': books})

def books_detail(request,book_id):
    books = Book.objects.filter(id=book_id)
    review = Review.objects.filter(book=book_id)
    review_form = ReviewForm()
    return render(request, 'main_app/book_detail.html',{'book': books.all, 'review_form': review_form, 'review':review })


@login_required
def children_index(request):
    children = Child.objects.all()
    return render(request, 'children/index.html', {
        'children': children
    })

# @login_required
# def children_detail(request, child_id):
#     child = Child.objects.get(id=child_id)
#     books = Book.objects.filter(user=request.user)
#     return render(request, 'children/detail.html', {
#         'child': child,
#         'books': books
#     })

@login_required
def children_detail(request, child_id): 
    
    tu={'D': [1,2,3], 
        'E': [4,5,6],
        'F': [7,8,9,10,11,12,13]}
    letterHoldingAge=""
    
    child = Child.objects.get(id=child_id)
    
    for t in tu:
        if(child.age_group in tu[t]):
            letterHoldingAge=t
            
    print(child.age_group)
    print(letterHoldingAge)        
    
    id_list = child.books.all().values_list('id')
    books_child_doesnt_have = Book.objects.filter(age_group=letterHoldingAge)
    print(books_child_doesnt_have)

      

    return render(request, 'children/detail.html', {
        'child': child,
        'books': books_child_doesnt_have
    })




class ChildCreate(CreateView):
    model = Child
    fields = ['name', 'age_group']
    success_url = '/children'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# def add_child(request, user_id):
#   form = ChildForm(request.POST)
#   if form.is_valid():
#     new_child = form.save(commit=False)
#     new_child.user_id = user_id
#     new_child.save()
#   return redirect('detail', user_id=user_id)


class ChildUpdate(UpdateView):
    model = Child
    fields = ['age_group']

class ChildDelete(DeleteView):
    model = Child
    success_url = '/children'

@login_required
def assoc_book(request,child_id, book_id):
    Child.objects.get(id=child_id).books.add(book_id)
    return redirect('detail', child_id=child_id)

@login_required
def disassoc_book(request, child_id, book_id):
    Child.objects.get(id=child_id).books.remove(book_id)
    return redirect('detail', child_id=child_id)

class BookList(LoginRequiredMixin,ListView):
  model = Book

# class BookDetail(LoginRequiredMixin,DetailView):
#   model = Book

@login_required
def add_review(request, book_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.book_id = book_id
        new_review.save()
    return redirect('books_detail', book_id=book_id)

def signup(request):
    print(request)
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again. Go home.'
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

