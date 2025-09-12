#validation-password
username = input("Enter Your Username:")
password = input("Enter Your Password:")
confirm = input("Enter Confirm Password:")


if username.strip() == "":
    print("Please Enter Your Username:")
elif password =="" or confirm == "":
    print("Password OR Confirm Password is Required!")

elif password != confirm:
    print("Access Denied Password is not match!")

else: 
    print("Access Granted", username.strip())
