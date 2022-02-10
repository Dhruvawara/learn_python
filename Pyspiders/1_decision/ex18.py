"""
check username and password
"""
username = input("Username:")
password = input("Password:")
if username == "DHRUVA":
    if password == "DHRUVA":
        print("Valid details")
    else:
        print("Invalid password")
else:
    print("Invalid details")
