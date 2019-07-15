print ("type -1 to exit")

total = 0

is_finished = False

while(not is_finished):
    grade = input("What is your grade?")

    grade_value = int(grade)

    if grade_value == 100:
      total = total+ 60
    elif grade_value >= 97:
      total = total+ 40
    elif grade_value >= 90:
      total = total+ 30
    elif grade_value == -1:
        is_finished = True

grade = input("Did you pass advisory?")

pass_count = int(grade)

total = total + (4*pass_count)

#isMath = input("did you get a 90 or above in math?(y or n)")

#if str(isMath).lower() == "y":
 #   total = total + 10

print ("Your total is $"+str(total))
