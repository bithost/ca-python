#Write a Python program that uses a dictionary to store information about a student (like name, age, and grade level). Then add
#functionality to add a new course and grade to the student's record.

# Store student information in a dictionary
student = {
    "name": "John Doe",
    "age": 16,
    "grade_level": 11,
    "courses": {}
}

# Print student information without courses
print(student)

#Add courses
student["courses"]["Math"] = "A"
student["courses"]["Science"] = "B"

#Print with courses
print(student)