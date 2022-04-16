from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomRegisterForm

# Create your views here.
def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user is added, Please log-in to start it!"))
            return redirect(register)
    else:
        register_form = CustomRegisterForm()
    context = {'register_form_info': register_form,
                'registration_text': 'Registration'}

    return render(request, 'register.html', context)
