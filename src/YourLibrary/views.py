from django.shortcuts import render, HttpResponse
from YourLibrary.forms import SignupForm
from django.views.generic import TemplateView
#from datetime import datetime


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse('<h2>You have been registered</h2>')

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', context={'form': form})


class HomeView(TemplateView):
    template_name = 'index.html'
    title = 'default'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
