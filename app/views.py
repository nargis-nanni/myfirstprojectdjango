from django.shortcuts import render
from app.models import Blog
from app.forms import  BlogForm
def home(request):
	form = BlogForm()
	

	
	all_blog = Blog.objects.all()

	a='angy'
	k='kajal'
	x=[a,k]
	return render(request, 'happy.html', {'form':form})


