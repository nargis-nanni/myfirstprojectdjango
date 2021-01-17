from django.shortcuts import render
from app.models import Blog
from app.forms import  BlogForm
	
def home(request):
	blog = Blog.objects.all()

	return render(request, 'happy.html',  {'blogs': blog}
)

	

	

  
