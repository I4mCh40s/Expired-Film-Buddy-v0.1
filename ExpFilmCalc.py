import datetime

print ("Expired film buddy v0.1 \n")
box = int(input("Box speed:"))
exp_year = int(input("Year of expiration:"))

today = datetime.date.today()
year = today.year

print("Your film has been expired for: ", year-exp_year, " years.\n")
decade = (year-exp_year) // 10
decBW = (year-exp_year) // 20
if decBW == 0:
    decBW = box

i = int(0)
while i < decade:
    box = box / 2
    i += 1

j = int(0)
while j < decBW:
    boxBW = box * 2
    j += 1


print("Color: Expose your film ", decade, " stop(s) over, or at ISO: ", box)
print("B/W: Expose your film ", ((year-exp_year) // 20), " stop(s) over, or at ISO: ", boxBW)



