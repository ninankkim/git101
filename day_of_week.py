day_of_week = int(input( "Please enter number 0 through 6: "))
if day_of_week == 0:
    print('Sunday')
elif day_of_week == 1:
    print('Monday')
elif day_of_week == 2:
    print('Tuesday')
elif day_of_week == 3:
    print ('Wednesday')
elif day_of_week == 4:
    print ('Thursday')
elif day_of_week == 5:
    print ('Friday')
elif day_of_week == 6:
    print ('Saturday')
elif day_of_week >= 7:
    print ('no')

if day_of_week == 6:
    print("It is Saturday and the weekend, sleep in.")
elif day_of_week == 0:
    print("It is Sunday and the weekend, sleep in.")
else:
    print("It's a weekday, go to work.")