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
	
	print(request.COOKIES)
	csrfToken = request.COOKIES['csrftoken']

	if request.method == "POST":
		response = HttpResponse()	#data that will be send back to the client

		print("*"*50)
		email = request.POST["Email"]
		password = request.POST["Password"]
		request_type = request.POST["type"]	#wether the user registers("new"), logs in("existing") or modifies their vault("change")
		if request_type == "new" or request.POST["type"] == "change":
			data = request.POST["Vault"]
			print(data)
		print(email)
		print(request.POST["type"])
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
			print(len(User.objects.filter(mail=email)))
			if len(User.objects.filter(mail=email)) != 0:
				if request_type == "new":
					print("User already exists.")
					response.write("User already exists.")
				elif request.POST["type"] == "change":
					print("Updating Vault")
					modifiedUser = User.objects.get(mail=email)
					modifiedUser.data = data
					modifiedUser.save()
					response.write("Vault updated!")
				else:
					print("Username right, testing login")
					storedPassword = User.objects.filter(mail=email)[0].password
					if storedPassword == password:
						print("Password right, loging in")
						response.write("Vault:" + User.objects.filter(mail=email)[0].data)
					else:
						print("Password wrong!")
						response.write("Password wrong!")

			else:
				if request_type == "new":
					print("creating new user")
					newUser = User(mail=email, password=password, data=data)
					newUser.save()
					response.write("User created!")
				else:
					print("user doesnt exist yet")
					response.write("User doesnt exist yet!")
		
		else:
			print("Email is invalid")
			response.write("Email is invalid")

		return response
		print("*"*50)
		
	return render(	request=request,
					template_name="index.html",
					context={"user_create":UserCreateForm, "csrfToken":csrfToken})

def prf(p,s):
	return HMAC.new(p,s,SHA512).digest()
