# 4. Take time (hours and minutes) and print the smaller angle between the hour and minute hands. 

hour = int(input("enter hour:- "))
minute = int(input("enter minute:- "))

hour_angel = hour * 30 * 0.5
minute_angle = minute * 6

difference = abs(hour_angel - minute_angle)

if difference > 180:
  smaller_angle = 360 - difference
else:
  smaller_angle = difference

print("Small angle:", smaller_angle, "degrees")