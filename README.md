# Password_Manager

A deployed version of this password manager can be found here: https://niklasziermann.pythonanywhere.com/password

This password_manager is a project I used for learning django as well as how to work with passwords.

**DO NOT DEPLOY OR USE THIS TO ACTUALLY STORE YOUR PASSWORDS! **

**THIS PROJECT EXISTS FOR LEARNING PURPOSES ONLY!** 



## How it works

To guarantee the secure transmission of login details multiple layers of hashing are used.

1. 500 iterations of PBKDF2-SHA256 **on the password** with the users email used as a salt 

   (**client-side** JavaScript)

   The resulting hash will later be used as a key to en-/decrypt the users password-vault.

2. 500 iterations of PBKDF2-SHA256 **on the key** with the users email used as a salt 

   (**client-side** JavaScript)

   This hash can then be send to the server

3. 100000 iterations of PBKDF2-SHA256 **on the hash** with the users email used as a salt 

   (**server-side** Python)

   Now the hash can be securely saved to the database or be compared to the database entry to log in and send the user his encrypted vault.

When the encrypted vault then returns to the user it will be AES decrypted and all entries get displayed on screen. 

*Note: The number of iterations should be changed according to the performance of the server the software runs on if a project like this was to be deployed at any point in time.*



## What I learned

- Password security
- Encryption and Hashing Techniques
- How to use Django Forms



## Contributors

Niklas Ziermann



## Copyright

**© Niklas Ziermann 2019**
