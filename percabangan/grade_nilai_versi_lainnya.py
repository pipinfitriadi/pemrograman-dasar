nilai = float(input("Nilai: "))

if nilai >= 90:
    grade = "A"
elif 80 <= nilai < 90:
    grade = "B+"
elif 70 <= nilai < 80:
    grade = "B"
elif 60 <= nilai < 70:
    grade = "C+"
elif 50 <= nilai < 60:
    grade = "C"
elif 40 <= nilai < 50:
    grade = "D"
else:
    grade = "E"

print("Grade:", grade)
