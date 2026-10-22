class Calculator:
    def __init__(self):
        
        while True:
            print("========Calculator========")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            
            choice = input("Enter choice (1-5) : ")
            
            if choice=="5":
                print("Calculator closed.")
                break
            self.a = float(input("Enter First Number:"))
            self.b = float(input("Enter second Number:"))
        
            if choice=="1":
                        add = self.a + self.b
                        print("Addition = ",add)
                        
            elif choice=="2":    
                        sub = self.a - self.b  
                        print("Subtraction = ",sub)
                        
            elif choice=="3":    
                        mul = self.a*self.b
                        print("Multiplication = ",mul)
                        
            elif choice=="4":       
                if self.b==0:
                    print("Division Error! Can't divide by 0")
                            
                else:
                    div = self.a/self.b
                    print("Division = ",div)
            
            else:
                    print("Invalid Choice !") 
                    
            choice2 = input("Do you want more calculation? Yes/No : ") 
            if choice2 !="Yes":
                print("Thank You")
                break
calc = Calculator()        
