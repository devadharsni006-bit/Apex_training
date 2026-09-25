java = float(input("Enter Java marks: "))
python = float(input("Enter Python marks: "))
mysql = float(input("Enter MySQL marks: "))

total = java + python + mysql
average = total / 3
percentage = (total / 300) * 100
remaining_marks = 300 - total

print("Total:", total)
print("Average:", average)
print("Percentage:", percentage)
print("Remaining marks:", remaining_marks)
