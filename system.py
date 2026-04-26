from pyscript import display, document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! My name is {self.name}. I am from section {self.section}, and my favorite subject is {self.favorite_subject}."

classmates = [
    Classmate('Kelsey Medina', 'Sapphire', 'Physical Education'),
    Classmate('Euan Martinez', 'Sapphire', 'Math'),
    Classmate('Adrianna Garces', 'Sapphire', 'TLE'),
    Classmate('Harvey Dolor', 'Sapphire', 'Science'),
    Classmate('Aaron Dee', 'Sapphire', 'English'),
]

def show_classmates(event):
    document.getElementById("output").innerHTML = "" 
    display(" Classmate List:", target="output")
    for c in classmates:
        display(c.introduce(), target="output")


def add_classmate(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if name and section and subject:
        new_classmate = Classmate(name, section, subject)
        classmates.append(new_classmate)
        display(f"{name} has been added successfully!", target="output")
    else:
        display("Please fill in all fields.", target="output")
