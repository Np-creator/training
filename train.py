def ampel(farbe): 
    
    if farbe == "red":

        print("Wait three secs")

    elif farbe == "green":

        print("Wait two sec")  

    else: 

        print("Wrong color") 

attemps = 4 

while attemps > 0 :   

    farbe = input("Enter yor guess: ") 

    if farbe == "green"  or farbe == "red": 

        ampel(farbe) 

        break 

    else: 

        attemps -= 1 

        print(f"You have {attemps} attemps left!") 

if attemps == 0: 

  print("bye!")


