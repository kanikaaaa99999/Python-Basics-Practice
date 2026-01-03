#typecasting = the process of converting a variable from one date type to another
#      str(), int(), float(), bool()

name = "kanika"
age = 18
cgpa = 9.2
is_student = True

print(type(cgpa))
print(type(name))
print(type(age))
print(type(is_student))

cgpa = int(cgpa)
print(cgpa)
age = float(age)
print(age)

age = str(age)
print(age)
print(type(age))