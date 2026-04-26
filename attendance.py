from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

days_list = []
absences_list = []

def add_data(e):
    day = document.getElementById("day").value
    absence = document.getElementById("absence").value

    if absence == "":
        display("Please enter a number", target="log")
        return

    days_list.append(day)
    absences_list.append(int(absence))

    display(f"Added: {day} - {absence} absences", target="log", append=True)

def show_graph(e):
    if len(days_list) == 0:
        display("No data to display", target="log")
        return

    days = np.array(days_list)
    absences = np.array(absences_list)

    plt.figure()
    plt.plot(days, absences, marker='o')
    plt.title("Section Attendance (Absences per Day)")
    plt.xlabel("Days")
    plt.ylabel("Number of Absences")
    plt.grid()

    display(plt, target="graph")