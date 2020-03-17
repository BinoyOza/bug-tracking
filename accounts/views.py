from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class UserCreateView(LoginRequiredMixin, View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/usercreate.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('index')
        else:
            form = UserCreationForm()
        return render(request, 'accounts/usercreate.html', {'form': form})
