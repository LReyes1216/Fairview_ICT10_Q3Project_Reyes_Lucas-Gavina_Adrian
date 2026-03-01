from pyscript import display, document

def create_account(event=None): # This function is called when the "Create Account" button is clicked. It validates the username and password according to the specified criteria and displays appropriate messages.
    document.getElementById("output").innerHTML = "" # Clear previous output messages

    username = document.getElementById("username").value # Get the value of the username input field
    password = document.getElementById("password").value # Get the value of the password input field
    
    if len(username) < 7: # Check if the username is at least 7 characters long
        document.getElementById("print").innerHTML = f"Username must be at least 7 characters long."
        return

    if not any(a.isalpha() for a in password): # Check if the password contains at least one letter
        document.getElementById("print").innerHTML = f"Password must contain at least one letter."
        return
    
    if not any(a.isdigit() for a in password): # Check if the password contains at least one digit
         document.getElementById("print").innerHTML = f"Password must contain at least one digit."
         return
    if not any(a in "!@#$%^&*()-_=+[{]};:<.>/?`~" for a in password): # Check if the password contains at least one special character
         document.getElementById("print").innerHTML = f"Password must contain at least one special character."
         return
    
    if len(password) < 10: # Check if the password is at least 10 characters long
         document.getElementById("print").innerHTML = f"Password must be at least 10 characters long."
         return
    
    if username and password: # If both username and password are valid, display a success message
          # Display success message with the username
         document.getElementById("print").innerHTML = f"You have successfully created your account!"
         display(f"User: {username}", target="print2")
