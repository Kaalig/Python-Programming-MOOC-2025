"""
Questions :
The code works almost correctly, but not quite. This exercise has very strict tests, which check the output for every single bit of whitespace.
Please fix the code so that the printout looks right. Notice especially how the comma notation in the print command automatically inserts a space around the different comma-separated parts.
The easiest way to transform the code so that it meets requirements is to use f-strings.

Hint: you can print an empty line by adding an empty print command, or by adding the newline character \n into your string.

Do remember to be extra careful when formatting printouts also in the future on this course. Some of the exercises have tests that require your output to be exactly as specified in the examples given. For example, please use actual whitespace characters in your code, instead of ASCII character codes for whitespace, or some such.
"""

# Answer : 

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old \n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3}) \n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month") 
