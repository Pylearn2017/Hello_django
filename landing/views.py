from django.shortcuts import render


def landing(request):
	name = 'Vlad'
	return render(request, 'landing/landing.html', locals())