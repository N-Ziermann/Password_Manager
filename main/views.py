from django.shortcuts import render
from django.http import HttpResponse
from main.models import User
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512, HMAC
from base64 import b64encode
import re

def homepage(request):
	
	if request.method == "POST":
		response = HttpResponse()	# data that will be send back to the client
		email = request.POST["Email"]
		password = request.POST["Password"]
		request_type = request.POST["type"]	# wether the user registers("new"), logs in("existing") or modifies their vault("change")
		if request_type == "new" or request.POST["type"] == "change":
			data = request.POST["Vault"]


		
		#check if email format is valid
		if re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
			# hashing the password again
			hashedPasswordBytes = PBKDF2(password, bytes(email, 'utf-8'), dkLen=64, count=100000, prf=prf)
			# turn hashed password into string to store in db
			hashedPassword = b64encode(hashedPasswordBytes).decode('utf-8')
			# check if user already exists
			if len(User.objects.filter(mail=email)) != 0:
				if request_type == "new":
					response.write("User already exists.")
				elif request.POST["type"] == "change":
					modifiedUser = User.objects.get(mail=email)
					modifiedUser.data = data
					modifiedUser.save()
					response.write("Vault updated!")
				else:
					storedPassword = User.objects.filter(mail=email)[0].password
					if storedPassword == hashedPassword:
						response.write("Vault:" + User.objects.filter(mail=email)[0].data)
					else:
						response.write("Password wrong!")

			else:
				if request_type == "new":
					newUser = User(mail=email, password=hashedPassword, data=data)
					newUser.save()
					response.write("User created!")
				else:
					response.write("User doesn't exist yet!")
		
		else:
			response.write("Email is invalid")

		return response
		
	return render(	request=request,
					template_name="index.html")


def prf(p,s):	# used to tell the PBKDF2 function which algorithm to use
	return HMAC.new(p,s,SHA512).digest()
