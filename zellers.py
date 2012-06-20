first_name=raw_input("First name?\n")
last_name=raw_input("Last name?\n")
print "Please enter your date of birth: "
month=input("Numerical value of Month? e.g. Jan->1\n")

if month>2:
    A=month-2
elif month==1 or 2:
    if month==1:
        A=11
    elif month==2:
        A=12
else:
    print "Invalid Input"

B = input("Day?\n")

year = str(raw_input("Year of birth?\n"))

C = int(year[2:4])

D = int(year[0:2])

W = (13*A -1)/5
X = C/4
Y = D/4
Z = W+X+Y+B+C - 2*D
R = Z%7

if R==0:
    r="Sunday"
elif R==1:
    r="Monday"
elif R==2:
    r="Tuesday"
elif R==3:
    r="Wednesday"
elif R==4:
    r="Thursday"
elif R==5:
    r="Friday"
elif R==6:
    r="Saturday"

print first_name, last_name, "was born on a", r
