from django.shortcuts import render, redirect
import os

# Create your views here.
def index(request):
   name = os.environ['NAME']
   title = os.environ['TITLE']
   website_name = os.environ['WEBSITE_NAME']
   email = os.environ['EMAIL']
   phone = os.environ['PHONE']
   profile_url = os.environ['PROFILE_URL']
   context = {
      'name': name,
      'title': title,
      'website_name': website_name,
      'email': email,
      'phone': phone,
      'profile_url': profile_url,
   }

   return render(request, 'index.html', context)   