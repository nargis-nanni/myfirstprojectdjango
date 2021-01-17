from django.contrib import admin
from app.models import Blog

class BlogAdmin(admin.ModelAdmin):
	class Meta:
		model=Blog
		fields='__all__'

admin.site.register(Blog, BlogAdmin)