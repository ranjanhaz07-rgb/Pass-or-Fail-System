subject_marks = []

for i in range(3):
    marks = int(input("Enter your marks:"))
    subject_marks.append(marks)

total_percentage = sum(subject_marks) / len(subject_marks) # i know i can use 3 here!

if total_percentage >= 40 and min(subject_marks) >= 33:
  print("You have passed the exam!")
  print("Percentage:", total_percentage ,"%")

else:
  print("You have failed!)
  print("Percentage:", total_percentage, "%")
