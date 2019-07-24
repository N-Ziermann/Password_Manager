from django.shortcuts import render
from django.http import HttpResponse
from main.forms import UserCreateForm
from main.models import User
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512, HMAC
from base64 import b64encode
import re
# Create your views here.
def homepage(request):
	
	if request.method == "POST":
		print("*"*50)
		email = request.POST["Email"]
		password = request.POST["Password"]
		new = request.POST["new"]
		if new == "true":
			data = request.POST["Vault"]
			print(data)
		print(email)
		print(request.POST["new"])
		print(password)
		
		#check if email format is valid
		if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
			print("Email is valid")
			
			# hashing the password again
			hashedPasswordBytes = PBKDF2("password", bytes(email, 'utf-8'), dkLen=64, count=100000, prf=prf)
			print(hashedPasswordBytes)
			# turn hashed password into string to store in db
			hashedPassword = b64encode(hashedPasswordBytes).decode('utf-8')
			print(hashedPassword)
			# check if user already exists
			if len(User.objects.raw('SELECT * FROM main_user WHERE mail="' + email + '";')) != 0:
				if new:
					print("User already exists.")
				else:
					print("Username right, testing login")
			else:
				if new:
					print("creating new user")
					
				else:
					print("user doesnt exist yet")
		
		else:
			print("Email is invalid")

		
		print("*"*50)


		if False:
			User.objects.raw('INSERT INTO main_user (mail, password, data) VALUES ()')
		
	return render(	request=request,
					template_name="index.html",
					context={"user_create":UserCreateForm})

def prf(p,s):
	return HMAC.new(p,s,SHA512).digest()
