import os


print("Welcome to Automatic Potato GitHub User Information Collector")
print(" 		  Developed By:- Shubham Yadav")
print("")
print("")
# Prompt the user for their GitHub username
user_name = input("Enter GitHub username: ")

# Modify the URL with the provided username
url = f"curl https://api.github.com/users/{user_name}"

# Execute the command using the OS module
os.system(url)
