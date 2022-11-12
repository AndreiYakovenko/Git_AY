distance = 100000
friend = 2
firstFriendSpeed = 1
secondFriendSpeed = 2
dogSpeed = 3
count = 0
time = 0
while distance < 100000:
    if friend == 1:
        time = distance/(firstFriendSpeed + dogSpeed)
        friend = 2
    else: 
        time = distance/(secondFriendSpeed + dogSpeed)
        friend = 1
distance = distance - (firstFriendSpeed + secondFriendSpeed) * time
count = count + 1
print ('Собака пробежит')
print (count)
print ('раз')