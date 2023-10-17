import Student as st

student1 = st.Student("John", 0)
student2 = st.Student("Mary", 78)
student3 = st.Student("Bob", 100)

print("-" * 30)
print("Student name and credit:")
print("-" * 30)
print(student1.name + " " + student1.getCredit())
print(student2.name + " " + student2.getCredit())
print(student3.name + " " + student3.getCredit())

student1.setCredit(20)
student2.setCredit([100, 100, 100])
student3.setCredit(100)

print("-" * 30)
print("Student name and credit after changes:")
print("-" * 30)
print(student1.name + " " + student1.getCredit())
print(student2.name + " " + student2.getCredit())
print(student3.name + " " + student3.getCredit())

student1.deletter()
student2.deletter()
student3.deletter()

print("-" * 30)
print("Student name and credit after deletter:")
print("-" * 30)
print(student1.name + " " + student1.getCredit())
print(student2.name + " " + student2.getCredit())
print(student3.name + " " + student3.getCredit())
