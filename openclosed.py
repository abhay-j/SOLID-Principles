""" 
Definition
Open/Closed Principle states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.e able to add new func This means you should btionality without changing existing code.

Why It Matters
Maintainability: Reduces the risk of introducing bugs when extending functionality.
Scalability: Facilitates adding new features without altering existing, stable code.
Reusability: Encourages designing components that can be extended and reused in various contexts.

Task:
Refactor the following Python code to adhere to the Open/Closed Principle.
"""

# class Notification:
#     def __init__(self, message, method):
#         self.message = message
#         self.method = method

#     def send(self):
#         if self.method == "email":
#             self.send_email(self.message)
#         elif self.method == "sms":
#             self.send_sms(self.message)
    
#     def send_email(self, message):
#         print(f"Sending email with message: {message}")
    
#     def send_sms(self, message):
#         print(f"Sending SMS with message: {message}")

# # Usage
# notification1 = Notification("Hello via Email!", "email")
# notification1.send()

# notification2 = Notification("Hello via SMS!", "sms")
# notification2.send()

from abc import ABC, abstractmethod

class Notifier(ABC):
    
    @abstractmethod
    def send(self):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Sending email with message: {message}")

class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Sending sms with message: {message}")
        

class Notification:
    def __init__(self , notifier : Notifier):
        self.notifier = notifier
    
    def send_notification(self, message):
        self.notifier.send(message)

email_notifier = EmailNotifier()
notification1 = Notification(email_notifier)
notification1.send_notification("Hey this is Abhay via Email!")


sms_notifier = SMSNotifier()
notfication2 = Notification(sms_notifier)
notfication2.send_notification("Hey this is Abhay vis sms")
    


# email_message = EmailNotifier("Hey this is abhay")
# email_message.send()

# sms_message = SMSNotifier("Hey my name is abhay")
# sms_message.send()
    