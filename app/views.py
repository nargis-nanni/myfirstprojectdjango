from django.shortcuts import render

def home(request):
	n='nargis'
	a='angy'
	k='kajal'
	x=[n,a,k]
	return render(request, 'happy.html', {'b':x})
