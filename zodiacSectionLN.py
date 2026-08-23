# Reqs:
# a. Ask the user to enter a year of birth. The baseline year 1900.
# b. Validate user input that it should not be earlier than 1900.
# If the user enters an invalid year, then display an appropriate message then stop or abort the program.
# d. Otherwise determine the chinese zodiac sign based on the following starting from 1900. Note: A zodiac sign will recur after each 12 years

YoB = int(input("Please enter a year of birth : "))

if YoB < 1900:

    print("Invalid Year, it should not be earlier than 1900.")

else:
    zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)" ] 

    z = YoB % 12
    

    if z == 0:
        print("Your Chinese Zodiac Sign is:", zodiac[0])

    elif z == 1:
        print("Your Chinese Zodiac Sign is:", zodiac[1])

    elif z == 2:
        print("Your Chinese Zodiac Sign is:", zodiac[2]) 

    elif z == 3:
        print("Your Chinese Zodiac Sign is:", zodiac[3]) 

    elif z == 4:
        print("Your Chinese Zodiac Sign is:", zodiac[4]) 

    elif z == 5:
        print("Your Chinese Zodiac Sign is:", zodiac[5])

    elif z == 6:
        print("Your Chinese Zodiac Sign is:", zodiac[6])

    elif z == 7:
        print("Your Chinese Zodiac Sign is:", zodiac[7])

    elif z == 8:
        print("Your Chinese Zodiac Sign is:", zodiac[8])

    elif z == 9:
        print("Your Chinese Zodiac Sign is:", zodiac[9])

    elif z == 10:
        print("Your Chinese Zodiac Sign is:", zodiac[10])

    elif z == 11:
        print("Your Chinese Zodiac Sign is:", zodiac[11])







