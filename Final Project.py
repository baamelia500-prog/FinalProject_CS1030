# Birthday Signs -- Chinese Zodiac and Astrology signs

userWilling = False

zodiacList = ["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
zodiacElements = ["metal","metal","water","water","wood","wood","fire","fire","earth","earth"]

while userWilling == False:
    userpick = input("Hello! Would you like to know your Chinese Zodiac or Astrology Sign? C/A: ")
    try:
        if userpick == 'C':
            print ("Let's figure out your Chinese Zodiac!")
            userBirthday = input("Please input your birth year:")

        elif userpick == 'A':
            print ("Let's figure out your Astrology Sign!")
            userBirthday = input("Please input your birth month and day (mm/dd):")


