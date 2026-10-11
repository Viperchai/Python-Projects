# Student Grade Analyzer
import sys

studentgrades_list = []

average = 0

highest_marks = 100

lowest_marks = 0

students_above_average = 15

grade_distribution = []

count = 0

a = 0
b = 0
c = 0
d = 0
f = 0


def import_grades_from_user():
    user_input = input("Enter student grades separated by commas(number only): ")
    return [int(item.strip()) for item in user_input.split(",")]  # FIX: convert to int


studentgrades_list = import_grades_from_user()
print(studentgrades_list)

confirmation = input("Please enter yes if this is the right list or no if it is not: ")

if confirmation.lower() == "yes":
    print("Good, let's continue.")
elif confirmation.lower() == "no":
    print(
        "The program will shutoff, please restart it to use it again, Goodbye!"
    )
    sys.exit()
else:
    print(
        "Not given yes or no answer. Restart program to run again, Goodbye!"
    )
    sys.exit()
average = sum(studentgrades_list) / len(studentgrades_list)
print("The average grade is:", average)  # FIX: cannot concatenate float with string

highest = max(studentgrades_list)
lowest = min(studentgrades_list)

print("Highest grade:", highest)
print("Lowest grade:", lowest)

for num in studentgrades_list:
    if num > average:
        count += 1
print(
    "Number of students above average:", count
)
for num in studentgrades_list:
    if num > 89:
        a += 1
    elif num > 79:
        b += 1
    elif num > 69:
        c += 1
    elif num > 59:
        d += 1
    else:
        f += 1
print(
    "Here are the number of students that got a certain grade: A's:",
    a,
    "B's:",
    b,
    "C's:",
    c,
    "D's:",
    d,
    "and F's:",
    f,
)
