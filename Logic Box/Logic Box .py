# Project for LMS
# Logic Box

      
while True:
    print("Welcome to the Pattern Generator and Number Analyzer")
    
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
       
    if choice=="1":
            while True:
                print("which type of pattern do you have Ganerate ")
            
                print("chooce any pattern from Given below:")
                print("1. Right Angle Triangle ")
                print("2. Left Angle Triangle ")
                print("3. pyramid Pattern")
                print("4. Exit")
            
                pattern_choice = input("Choose your Pattern: ")
                
                if pattern_choice == "1":
                        rows = input("Enter the number of rows for the pattern: ")
                        
                        if rows.isdigit():
                            rows = int(rows)
                        
                            if rows < 0 and rows < 5:
                                print("Rows value must be positive and more than 5")
                                break
                            else:
                                for i in range(1, rows + 1):
                                    for j in range(i):
                                        print("*", end=" ")
                                    print()
                                    
                        else:
                            print("Rows value must be in Digit")
                            break
                        
                elif pattern_choice == "2":
                        rows = input("Enter the number of rows for the pattern: ")
                        
                        if rows.isdigit():
                            rows = int(rows)
                            
                            if rows < 0 and rows < 5:
                                print("Rows value must be positive and more than 5")
                                break
                            else:
                                for i in range(1, rows + 1):
                                    for j in range(i, rows):
                                        print(" ", end=" ")
                                    for k in range(i):
                                        print("*", end=" ")
                                    print()
                        else:
                            print("Rows value must be in Digit")
                            break
                    
                elif pattern_choice == "3":
                        rows = input("Enter the number of rows for the pattern: ")
                        
                        if rows.isdigit():
                            rows = int(rows)
                            
                            if rows < 0 and rows < 5:
                                print("Rows value must be positive and more than 5")
                                break
                            else:
                                for i in range(0, rows):
                                    for j in range(i, rows-i-1):
                                        print(end=" ")
                                    for j in range(0, i + 1):
                                        print("*", end=" ")
                                    print()
                        else:
                            print("Rows value must be in digit")
                            break
                elif pattern_choice == "4":
                        print("Exiting form pattern Ganeration ")
                        break
                        
                else:
                    print("Invalid Input")

        
    elif "2":
            
            while True:
                print("choose any option from Given below:")
                print("1. Odd and Even numbers from given Range")
                print("2. Sum of all numbers in the range")
                print("3. Exit")
                
                analize_choice = input("Choose your option: ")
                
                if analize_choice == "1":
                        print("You want Odd and Even numbers in the range")
                        
                        start = input("Enter the start of the range: ")
                        end = input("Enter the end of the range: ")
                        
                        if start.isdigit() and end.isdigit():
                            start = int(start)
                            end = int(end)
                            
                            if start >= end:
                                break
                            else:
                                for i in range(start, end + 1):
                                    if i % 2 == 0:
                                        print(f"{i} is even number")
                                    else:
                                        print(f"{i} is odd number")
                        else:
                            print("Start range and End Raange must be in Digit")
                            break
                    
                elif analize_choice == "2":
                                                
                        start = input("Enter the start of the range: ")
                        end = input("Enter the end of the range: ")
                        
                        if start.isdigit() and end.isdigit():
                            start = int(start)
                            end = int(end)
                            
                            if start >= end:
                                print("End range number value must be bigger than start range number")
                                break
                            else:
                                sum = 0
                                for i in range(start, end + 1):
                                    sum += i
                                print(f"Sum of all numbers from {start} to {end} is: {sum}")
                        else:
                            print("Start range and end range must be in digit")
                        
                elif analize_choice == "3":
                        print("Thank you for Exploaring")
                        break
                    
                else:
                    print("Invalid Option")
                    break
        
    elif "3":
        print("currently you exiting the program")
        break
        
    else:
        print("Invalid option")
        break
                





                
                    




































































































                
    
