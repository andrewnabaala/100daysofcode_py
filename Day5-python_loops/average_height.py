# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
height = 0
length = 0
for heights in student_heights:
    height += heights
    length += 1
average = height / length
int_average = round(average)
print(int_average)