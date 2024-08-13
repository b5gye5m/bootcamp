while True:
    num=input("input number: ")
    #print(type(num))

    try:
        int(num)
        
        print(type(num))
        
        
        
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue