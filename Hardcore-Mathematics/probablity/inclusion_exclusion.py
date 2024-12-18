"""
 Given two lists of student IDs representing enrollment in two different CS courses, calculate the total number of unique students enrolled in either course, accounting for students taking both.

"""

def unique_students(course1, course2):
    return len(set(course1) | set(course2))

        
if __name__ == "__main__":
    course1 = [1, 2, 3, 4]
    course2 = [3, 4, 5, 6]  
    print(f"Num Students in Course 1: {len(course1)}")
    print(f"Num Students in Course 2: {len(course2)}")
    print(f"The total number of unique students enrolled in either course is {unique_students(course1, course2)}")      
  