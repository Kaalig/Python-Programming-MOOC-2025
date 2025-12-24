# Write your solution here
student = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))
 
groups = (student + group_size - 1) // group_size
 
print("Number of groups formed:", groups)
