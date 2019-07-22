from django.shortcuts import render
from django.http import HttpResponse
from main.forms import UserCreateForm
from main.models import User
import re

# Create your views here.
def homepage(request):
	
	if request.method == "POST":
		email = request.POST["Email"]
		password = request.POST["Password"]

		print("*"*50)
		print(email)
		print(request.POST["new"])
		print(password)
		
		#check if email format is valid
		if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
			print("Email is valid")
		else:
			print("Email is invalid")

		# hashing the password again
		####

		# check if user already exists
		if len(User.objects.raw('SELECT * FROM main_user WHERE mail="' + email + '";')) != 0:
			print("User already exists.")
		print("*"*50)


		if False:
			User.objects.raw('INSERT INTO main_user (mail, password, data) VALUES ()')
		
	return render(	request=request,
					template_name="index.html",
					context={"user_create":UserCreateForm})