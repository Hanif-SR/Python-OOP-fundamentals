# Python-OOP-fundamentals
Understanding Python Object Oriented Programming.
For python Programming language, its OOP basic fundamentals have at least 12 key concepts which are;
1.  **Class & Object** – Creating templates and real-world instances.
2.  **Constructor** `__init__()` – Initialize attributes when object is created.
3.  **Instance Attributes** – Variables that belong to an object.
4.  **Instance Methods** – Functions inside a class using self.
5.  **Class Attributes** – Shared by all instances of a class.
6.  **Class Methods** `@classmethod`
7.  **Static Methods** `@staticmethod`
8.  **Encapsulation** – Hiding internal data `_protected` and `__private`.
9.  **Inheritance** – One class inherits from another.
10.  **Polymorphism** – One interface, many forms (e.g., method overriding).
11.  __str__ and __repr__ – Custom string display.
12.  **Object Comparison** (`__eq__()`, `__lt__()`, etc.)
note: Understanding those 12 points are important and crucial in using python libraries whether its modules or packages. 

---

### Class & Object
A **class** is a blueprint for creating objects. It defines attributes (data) and methods (behavior) that the created **objects** will have. An object is an instance of a class, representing a specific realization of that blueprint. For example;

![image](https://github.com/user-attachments/assets/a52edf39-28cd-430e-9d3c-655aeeda444a)


---

### Constructor
The `__init__()` method is the class constructor. It is automatically called when a new object is created. It is typically used to initialize instance attributes.
For example;

![image](https://github.com/user-attachments/assets/65a50711-2460-4cc9-bd75-82ec652f9f89)


--- 

### Instance and attributes
Instance attributes are variables that are unique to each object. They are usually defined in the constructor using `self.` for example;

![image](https://github.com/user-attachments/assets/01c25a9b-58b0-410d-b8b4-df163187da8e)


---

### Instance methods
Instance methods are functions defined inside a class that operate on object instances. They use `self` to access instance attributes and other methods.
For example;

![image](https://github.com/user-attachments/assets/934d1afb-ba01-4098-8ce0-5365749e3a00)


---

### Class attributes
Class attributes are shared across all instances of a class. They are defined directly inside the class body. For example;

![image](https://github.com/user-attachments/assets/ddb6e6bd-be7a-4bd1-936f-1bf94c371aa9)


---

### Class methods
Class methods are methods that affect the class itself rather than instances. They take `cls` as the first parameter and are defined using the `@classmethod` decorator.
For example;

![image](https://github.com/user-attachments/assets/66e2bb4a-21a2-4d3f-8074-b02eb5adae1c)


---

### Static methods
Static methods are functions within a class that do not modify class or instance state. They don't take `self` or `cls` and are defined with the `@staticmethod` decorator.
For example;

![image](https://github.com/user-attachments/assets/20c8755c-44a7-4ddb-beb0-1fddc5732c9d)


---

### Encapsulation
Encapsulation is the practice of restricting direct access to an object’s data. Python uses naming conventions for this:
- _protected: Intended for internal use.
- __private: Name mangled to prevent external access.
For example;

![image](https://github.com/user-attachments/assets/8107fd58-0fe3-485d-bcaf-0687a7d569b3)


---

### Inheritance
Inheritance allows one class (child) to inherit attributes and methods from another (parent).
For example;

![image](https://github.com/user-attachments/assets/6aff59c0-3dc2-40bb-851d-25070d10223e)


---

### Polymorphism
Polymorphism allows different classes to define methods with the same name, enabling them to be used interchangeably.
For example;
```
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())
```
note: example above are using two simple classes and one simple method.
For the OOP example that uses Bank as an environment, there are several polymorphism which are `send_money()`, `withdraw()`, and `deposit()`.

---

### `__str__()` and `__repr__()`
These special methods control how objects are represented as strings:
- __str__() is for human-readable string representation.
- __repr__() is for developer/debugging output.
For example;

![image](https://github.com/user-attachments/assets/331f528a-902b-464d-b7e0-d8cfe45e7617)


---

### Object comparison
Python lets you define custom logic for object comparisons using special methods:
- `__eq__()` for equality (`==`)
- `__lt__()` for less than (`<`)
- `__gt__()` for greater than (`>`)
For example;

![image](https://github.com/user-attachments/assets/fb9c2dff-1c80-4352-84a4-be4678291650)

note: From the example above the object comparison method is specifically customed to be able to compare two objects or instances.
