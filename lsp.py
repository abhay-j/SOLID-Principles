""" 
3. Liskov Substitution Principle (LSP)

Definition
Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. In other words, subclasses should enhance or specialize the behavior of the base classes without altering their expected functionalities.

Why It Matters
Reliability: Ensures that derived classes behave predictably when used in place of base classes.
Maintainability: Simplifies code maintenance by adhering to consistent behavior across class hierarchies.
Reusability: Facilitates the reuse of components without unintended side effects.


Task:
Refactor the following Python code to adhere to the Liskov Substitution Principle (LSP).

class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")

def make_bird_fly(bird: Bird):
    bird.fly()

# Usage
bird = Bird()
bird.fly()  # Output: Flying

penguin = Penguin()
penguin.fly()  # Raises NotImplementedError

"""

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass
        
class Pegion(Bird):
     def move(self):
         self.fly()
     def fly(self):
         print("pegion flies swiftly")

class Penguin(Bird):
    def move(self):
        self.walk()
    def walk(self):
        print("penguins walk")    

def printMovement(bird : Bird):
    bird.move()

birds = [Penguin(), Pegion()]

for bird in birds:
    printMovement(bird)