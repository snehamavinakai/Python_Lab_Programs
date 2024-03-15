student_info = {'name':'Alex','age':20,'grade':'A','courses':['Java','Python','C++']}
print("Name : ",student_info['name'])
print("Age : ",student_info['age'])
student_info['age'] = 21
print("Update Age : ",student_info['age'])
student_info['city'] = 'New York'
print("City : ",student_info['city'])
del student_info['grade']
print("Student info after removing grade ",student_info)
print("Course")
for course in student_info['courses']:
    print(course)
if 'grade' in student_info:
    print("Grade in student info : ",student_info['grade'])
else:
    print("Grade not foumd")
    print("Keys : ",student_info.keys())
    print("Vales : ",student_info.values())
    print("Items : ",student_info.items())
    student_info_copy = student_info.copy()
    print("Copied Dic ",student_info_copy)
    student_info.clear()
    print("Cleared dic",student_info)
