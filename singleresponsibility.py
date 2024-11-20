""" 
Single Responsibility Principle (SRP)

Definition
Single Responsibility Principle states that a class should have only one reason to change, meaning it should have only one job or responsibility.

Why It Matters
Maintainability: Easier to understand and modify.
Reusability: Components can be reused in different contexts.
Testability: Simplifies unit testing by isolating functionalities. 
"""

""" 
Task:
Refactor the following Python class to adhere to the Single Responsibility Principle.

Implement Dependency Injection: Enhance flexibility and testability by injecting dependencies.
Adopt Clear Naming Conventions: Ensure class names precisely reflect their responsibilities.
Explore Data Classes: Use Python's @dataclass for cleaner and more efficient data handling.
Prepare for Future Principles: As you progress through the SOLID principles, these foundational steps will serve you well.



class UserManager:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def save_user(self):
        # Logic to save user to the database
        print(f"Saving user {self.username} to the database.")

    def send_welcome_email(self):
        # Logic to send a welcome email
        print(f"Sending welcome email to {self.email}.")
        
        
Solution :  
class UserManager:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def save_user(self):
        print(f"Saving user {self.username} to the database.")

class GreetUser:
    def __init__(self, email):
        self.email = email
    
    def send_welcome_email(self):
         print(f"Sending welcome email to {self.email}.")
        

"""
from dataclasses import dataclass

#Explore Data Classes: Use Python's @dataclass for cleaner and more efficient data handling.
@dataclass
class User:
    username: str
    emil : str

#Implement Dependency Injection: Enhance flexibility and testability by injecting dependencies.
class DBConnector:
    def save_user(self, username):
        print(f"Saving user {self.username} to the database.")
        
class EmailService:
    def send_email(self, email):
        print(f"Sending welcome email to {self.email}.")




class UserManager:
    def __init__(self, dbconnector : DBConnector):
        self.dbconnector = dbconnector
    
    def save_user(self, user : User):
        self.dbconnector.save_user(user.username)

class WelcomeEmailSender:  
    def send_welcome_email(self, user : User):
         print(f"Sending welcome email to {user.email}.")
       

        
        