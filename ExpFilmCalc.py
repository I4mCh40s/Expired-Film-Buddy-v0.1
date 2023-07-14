# As a beginner film shooter I was confused by the fact that people actually use expired film stocks and get good results
# so I made this... this code will help you determine @ which ISO to shoot your expired film. Color AND black and white

import datetime

print ("Expired film buddy v0.1 \n")
box = int(input("Box speed:"))
exp_year = int(input("Year of expiration:"))

today = datetime.date.today()
year = today.year

print("Your film has been expired for: ", year-exp_year, " years.\n")
decade = (year-exp_year) // 10
decadeBW = (year-exp_year) // 20

if decadeBW == 0:
    boxBW = box
else:
    j = int(0)
    while j < decadeBW:
        boxBW = box // 2
        j += 1

i = int(0)
while i < decade:
    box = box // 2
    i += 1



print("Color: Expose your film ", decade, " stop(s) over, or at ISO: ", box)
print("B/W: Expose your film ", ((year-exp_year) // 20), " stop(s) over, or at ISO: ", boxBW)



