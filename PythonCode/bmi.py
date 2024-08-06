weight = float(input("Enter the weight in Kg:"))
height = float(input("Enter height in meter:"))

BMI= (weight/((height)*(height)))

if(BMI<18.5):
    print("You are in underwait")

elif(BMI>18.5 and BMI <= 24.9):
    print("your wait wait is normal")
elif(BMI>25 and BMI<=29.9):
    print("you are in OverWait")
elif(BMI>30):
    print("you are in obesity:")       
