from store.models import Book
from YourLibrary.forms import BookForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
#from django.shortcuts import render, get_object_or_404, HttpResponseRedirect



# def books(request):
#     books = Book.objects.all()
#     return render(request, 'store/books.html', context={'books':books})

class BooksView(ListView):
    model = Book
    template_name = 'store/books.html'
    context_object_name = 'books'


# def book(request, pk_book):
#     book = get_object_or_404(Book, pk=pk_book)
#     return render(request, 'store/books.html', context={'book':book})

class BookView(DetailView):
    model = Book
    template_name = 'store/books.html'
    #context_object_name = 'book'


# def new_book(request):

#     if request.method == 'POST':
#         form = BookForm(request.POST or None)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#         return HttpResponseRedirect(request.path)
#     else:
#         #if request.user.is_authenticated:
#             #init_values['name'] = request.user
#         #init_values['date'] = datetime.today()
#         init_values = {}
#         init_values['kind'] = 'Sci fi'
#         form = BookForm(initial=init_values)

#     return render(request, 'store/new_book.html', {'form': form})

class NewBookView(CreateView):
    model = Book
    template_name = 'store/new_book.html'
    form_class = BookForm
    #fields = ['title', 'kind'] -> pour ne plus utiliser le formulaire de froms.py mais directement la classe Book
    
    def get_success_url(self):
        return reverse('books_list')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Créer'
        return context


class BookEditView(UpdateView):
    model = Book
    template_name = 'store/new_book.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse('books_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Modifier'
        return context


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'store/delete_book.html'
    success_url = reverse_lazy('books_list')