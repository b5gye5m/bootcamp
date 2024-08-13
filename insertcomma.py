while True:
    num=input("input number: ")
    #print(type(num))

    try:
        int(num)
        
        

        
        
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue