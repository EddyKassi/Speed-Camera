print("*****Speed Calculator*****")

distance = 500
speedlimit = 60

person = input("Enter your name: ")
greeting = "Hello. Welcome to the system {}".format(person)
print(greeting)

time1 = float(input("What is the entry time? "))
time2 = float(input("What is the leaving time? "))
time = (time2 - time1)
speed = (distance / time)
print(speed)

if speed >= speedlimit:
    print("You were driving too fast! You have received a fine. ")
    
from datetime import datetime
now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

part1 = input("Insert Area Code on License Plate: ")
if not re.match("^[a-z]*$", part1):
    print("Error! Only letters a-z allowed!")
part2 = int(input("Insert Age Identifier on License Plate: "))
part3 = str(input("Enter the Remaining Letters on your License Plate: "))
licenceplate = (part1, part2, part3)
print("Your number plate:", part1, part2, part3)


file = open("Number Plate Recogintion.txt", "w")

content = "Name Of User : " + str(person) + "\n";
content += " Time Car Passed the first Sensor: " + str(time1) + "\n";
content += " The time that the car passed the second sensor: " + str(time2) + "\n";
content += " The car was driving at the average speed of: " + str(speed) + "\n";
content += " The cars registration Number was: " + str(licenceplate) + "\n";
file.write(content)

file.close()
