import re
from typing import Dict, List

class LoginForm:
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 15

    def __init__(self):
        self.errors: List[str] = []

    def validate_email(self, email: str) -> bool:
        if not email:
            self.errors.append("Email is required.")
            return False
        
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            self.errors.append("Invalid email format. Please try again.")
            return False
    
        return True
    
    def validate_password(self, password: str) -> bool:
        if not password:
            self.errors.append("Password is required.")
            return False
        
        if len(password) < self.MIN_PASSWORD_LENGTH:
            self.errors.append(f"Password has to be a minimum of {self.MIN_PASSWORD_LENGTH}")
            return False
        
        if len(password) > self.MAX_PASSWORD_LENGTH:
            self.errors.append(f"Password has to be a maximum of {self.MAX_PASSWORD_LENGTH}")
            return False
        
        pattern = r'[A-Z]'
        if not re.match(pattern, password):
            self.errors.append("Password must contain at least one upper case letter.")
            return False

        return True
    
def main():
    print("=" * 50)
    print("Login Form")
    print("=" * 50)

    form = LoginForm()

    #get the user input for the email
    email = input("\nEmail: ").strip()

    #get the user input for the password
    password = input("\nPassword: ").strip()

    #validate the email and the password
    email_valid = form.validate_email(email)
    password_valid = form.validate_password(password)

    if email_valid and password_valid:
        print("\nLogin Successful!")
    else:
        print("\nLogin Failed. Validation error.")
        for errors in form.errors:
            print(f"- {errors}")


print("=" * 50)

if __name__ == "__main__":
    main()