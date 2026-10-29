class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Create objects
s1 = Student("Rahul", 20)
s2 = Student("Priya", 21)

# Call the method copilot
s1.display()
s2.display()