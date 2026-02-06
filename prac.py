print("enter marks for 5 subjects (out of 100):")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500)*100
cgpa = percentage/10
print(f"Total marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"CGPA: {cgpa:.2f}")

if cgpa >= 9.1 and cgpa <= 10:
    grade = "A++ outstanding"
elif cgpa >= 8.1 and cgpa <= 9:
    grade = "A+ excellent"
elif cgpa >= 7.1 and cgpa <= 8:
    grade = "A very good"
elif cgpa >= 6.1 and cgpa <= 7:
    grade = "B good"
elif cgpa >= 5.1 and cgpa <= 6:
    grade = "C average"   
elif cgpa >= 4.1 and cgpa <= 5:
   grade = "D below average"

print(f"Grade: {grade}")