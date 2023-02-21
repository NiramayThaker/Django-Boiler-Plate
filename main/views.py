from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def home(request):
	return HttpResponse("Home")

def sign_up(request):
	form = RegistrationForm()

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)

			return redirect("home")

	context = {'form': form}
	return render(request, 'registration/signup.html', context=context)
