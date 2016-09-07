print ("Problem 1")
pi=3.141592653
r=5
volume=(4/3)*pi*(r**3)
print("The volume of the sphere is", volume)

print ("Problem 2")
n = 60
cover_price = 24.95
bookstore_discount = 1-.4
shipping_cost = 3 + (0.75*(n-1))
total_cost = (cover_price*bookstore_discount*n)+(shipping_cost)
print("The total wholesale cost is $", ('%.2f' % total_cost))

print("Problem 3")
departure = 6*60 + 52
first_mile = 8 + (15/60)
three_miles = (7 + (12/60))*3
last_mile = 8 + (15/60)
trip = first_mile + three_miles + last_mile
end_time = departure + trip
end_hour = int(end_time/60)
end_minute = (end_time%60)
print ('%.0f' % end_hour,":", '%.0f' % end_minute,"am")


print("Problem 4")
original = 82
new = 89
difference = new - original
change = difference/original
percentage = change*100
print('0%0.1f' % percentage,"%")
input()