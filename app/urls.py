from django.conf.urls import url

from app. views import home
urlpatterns = [
	url('',home, name='home')

]