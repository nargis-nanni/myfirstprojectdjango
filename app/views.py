from django.shortcuts import render
from app.models import Blog
from app.forms import  BlogForm
	
def home(request):
	
	form = BlogForm()	

	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()
	all_blog = Blog.objects.all()

	a='angy'
	k='kajal'
	x=[a,k]
	return render(request, 'happy.html', {'form':form,'blogs':all_blog})


