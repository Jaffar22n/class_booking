# Step 1: Create dictionaries
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Step 4: Prompt the user to enter a course number
course_number = input("Enter a course number: ")

# Step 5: Check if the course number exists in the dictionaries
if course_number in course_rooms and course_number in course_instructors and course_number in course_times:
    # Step 6: Display the room number, instructor, and meeting time
    print(f"Course Number: {course_number}")
    print(f"Room Number: {course_rooms[course_number]}")
    print(f"Instructor: {course_instructors[course_number]}")
    print(f"Meeting Time: {course_times[course_number]}")
else:
    # Step 7: Display an error message
    print("Invalid course number. Please try again.")

