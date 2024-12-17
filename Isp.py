""" 
4. Interface Segregation Principle (ISP)

Definition
The Interface Segregation Principle states that no client should be forced to depend on methods it does not use. Instead of having large, general-purpose interfaces, it's better to have multiple smaller, specific interfaces tailored to the needs of different clients.

Why It Matters
Maintainability: Smaller interfaces are easier to understand and maintain.
Flexibility: Changes to one interface do not affect unrelated clients.
Reusability: Clients can implement only the interfaces that are relevant to them.
Decoupling: Reduces the dependencies between classes, leading to a more modular and flexible design.

Exercise : Task:
Refactor the following Python code to adhere to the Interface Segregation Principle (ISP).
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

    @abstractmethod
    def scan_document(self, document):
        pass

class OldPrinter(Printer):
    def print_document(self, document):
        print(f"Printing document: {document}")

    def scan_document(self, document):
        # OldPrinter cannot scan documents
        raise NotImplementedError("OldPrinter cannot scan documents.")

"""

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class OldPrinter(Printer):
    def __init__(self):
        pass
    def print_document(self, document):
        print("This is the printed document {}".format(document))

class NewScanner(Scanner):
    def __init__(self):
        pass
       
    def scan_document(self, document):
        print("This is the scanned document {}".format(document))
        

