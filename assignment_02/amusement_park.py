# This Lesson coveres order importance in if-elif statements
age = 101

if age < 4:
    print("Admission is $0")
elif age < 18:
    print("Admission is $25")
elif age > 60:
    print("Admission is $35")
elif age > 100:
    print("Admission is $0 and you get a free beer!")
else:
    print("Admission is $40")

# Notice that if the age is >100, we still get the message saying "Admission is $35" thats because when pythoon
#  reads it, it starts from top to bottom and since >60 is true, it assumes thats the correct response. However,
# the correct response is "Admission is $0 and you get a free beer!". So in-order to fix it, we need to recorrect
# the order