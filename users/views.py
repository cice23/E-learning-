from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from django.shortcuts import render, redirect
from .forms import UserCreationForm, DocumentUploadForm
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        doc_form = DocumentUploadForm(instance=request.user)
        return render(request, 'users/profile.html', {'doc_form': doc_form})

    def post(self, request):
        doc_form = DocumentUploadForm(request.POST, request.FILES, instance=request.user)
        if doc_form.is_valid():
            doc_form.save()
            return redirect('profile')
        return render(request, 'users/profile.html', {'doc_form': doc_form})
