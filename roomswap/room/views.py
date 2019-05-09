from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View, FormView, TemplateView
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from .forms import SignUpForm
from .models import room

from .models import room

class SignUpView(View):
    template_name = 'register.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("You have been successfully registered"))

        args = {'form': form}
        return render(request, self.template_name, args)


class HomePageView(TemplateView):
    template_name = 'rooms.html'

    def get(self, request):
        rooms = room.objects.all()
        return render(request, self.template_name, {'rooms': rooms})

class DelView(View):
    template_name = 'rooms.html'

    def post(self, request):







