# Electricity Bill
import datetime
Date = datetime.date.today()
class Account():
    print("Electricity Billing System")
    Name = str(input("Enter Name:"))
    A = int(input("Enter your area:"
                  "\n1)Rural\n2)Urban\n3)Metropolitan\n"))
    MeterNumber = int(input("Enter MeterNumber:"))
    Address = input("Enter your Address:")
    PhoneNumber = int(input("Enter your PhoneNumber:"))
    def details(bill):
        print("================================================================")
        print("Customer Name:",bill.Name,"                  ","Date: ",Date)
        print("MeterNumber is :",bill.MeterNumber)
        print("Address:",bill.Address)
        print("Mobile Number:",bill.PhoneNumber)
user = Account()
Area = user.A
I = int(input("Enter your Unitsconsumed :"))
P = int(input("Previous balance :"))
if Area == 1:
    class Cal():
        Amount = 0
        if 0 <= I <= 40:
            Amount = P + I * 2.60
            GST = (Amount * 18) / 100
            A = GST + Amount
        elif 41 <= I <= 100:
            Amount = P + I * 3.70
            GST = (Amount * 18) / 100
            A = GST + Amount
        elif 101 <= I <= 200:
            Amount = p + I * 4.95
            GST = (Amount * 18) / 100
            A = GST + Amount
        else:
            Amount = P + I * 5.75
            GST = (Amount * 18) / 100
            A = GST + Amount
    g=Cal()
    user.details()
    print("Previous Balance:", P)
    print("Amount to be paid:",g.A)

elif Area == 2:
    class Cal():
        Amount = 0
        if 0 <= I <= 40:
            Amount = P + I * 3.25
            GST = (Amount * 18) / 100
            A = GST + Amount
        elif 41 <= I <= 100:
            Amount = P + I * 4.70
            GST = (Amount * 18) / 100
            A = GST + Amount
        elif 101 <= I <= 400:
            Amount = P + I * 6.15
            GST = (Amount * 18) / 100
            A = GST + Amount
        elif 401 <= I <= 1000:
            Amount = P + I * 6.15
            GST = (Amount * 18) / 100
            A = GST + Amount
        else:
            Amount =  P + I * 7.30
            GST = (Amount * 18) / 100
            A = GST + Amount
    g=Cal()
    user.details()
    print("Previous Balance:", P)
    print("Amount to be paid:",g.A)
elif Area == 3:
    city = str(input("Please select your city\n1)Bangalore\n2)Chennai\n"
                     "3)Hyderbad\n4)Delhi\n5)kolkata\n6)Vishakapatanam\n7)Agra:\n"))
    if city == "1":
        class Cal():
            Amount = 0
            if 0 <= I <= 100:
                Amount = P + I * 4.7
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 101 <= I <= 300:
                Amount = P + I * 5.97
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 301 <= I <= 500:
                Amount = P + I * 7.1
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 501 <=  I <= 800:
                Amount = P + I * 7.99
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 801 <= I <= 1250:
                Amount = P + I * 8.25
                GST = (Amount * 18) / 100
                A = GST + Amount
            else:
                Amount = P + I * 9.2
                GST = (Amount * 18) / 100
                A = GST + Amount
        g = Cal()
        user.details()
        print("Previous Balance:", P)
        print("Amount to be paid:",g.A)
    elif city == "2":
        class Cal():
            Amount = 0
            if 0 <= I <= 100:
                Amount = P + I * 3.7
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 101 <= I <=300:
                Amount = P + I * 4.2
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 301 <= I <= 600:
                Amount = P + I * 6.15
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 601 <= I <= 1050:
                Amount = P + I * 7.15
                GST = (Amount * 18) / 100
                A = GST + Amount
            else:
                Amount =  P + I * 8.9
                GST = (Amount * 18) / 100
                A = GST + Amount
        g = Cal()
        user.details()
        print("Previous Balance:", P)
        print("Amount to be paid:",g.A)
    elif city == "3":
        class Cal():
            Amount = 0
            if 0 <= I <= 100:
                Amount = P + I * 4.05
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 101 <= I <= 400:
                Amount = P + I * 5.91
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 401 <= I <=  750:
                Amount =  P + I * 7.08
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 751 <= I <= 1000:
                Amount = P + I * 8.2
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 1001 <= I <= 2000:
                Amount = P + I * 9.02
                GST = (Amount * 18) / 100
                A = GST + Amount
            else:
                Amount = P + I * 11.25
                GST = (Amount * 18) / 100
                A = GST + Amount
        g=Cal()
        user.details()
        print("Previous Balance:", P)
        print("Amount to be paid:",g.A)
    elif city == "4":
        class Cal():
            Amount = 0
            if 0 <= I <= 50:
                Amount = P + I * 4.7
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 51 <= I <=100:
                Amount = P + I * 5.10
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 101 <= I <= 300:
                Amount = P + I * 6.8
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 301 <= I <= 600:
                Amount = P + I * 7.7
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 601 <= I <= 1000:
                Amount = P + I * 9.1
                GST = (Amount * 18) / 100
                A = GST + Amount
            else:
                Amount = P + I * 11
                GST = (Amount * 18) / 100
                A = GST + Amount
        g = Cal()
        user.details()
        print("Previous Balance:", P)
        print("Amount to be paid:",g.A)
    elif city == "5":
        class Cal():
            Amount = 0
            if  0 <= I <= 50:
                Amount = P + I * 4.89
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 51 <= I <= 100:
                Amount = P + I * 5.4
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 101 <= I <= 300:
                Amount = P + I * 6.41
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 301 <= I <= 600:
                Amount = P + I * 7.16
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 601 <= I <= 1050:
                Amount = P + I * 8.33
                GST = (Amount * 18) / 100
                A = GST + Amount
            else:
                Amount = P + I * 10.92
                GST = (Amount * 18) / 100
                A = GST + Amount
        g = Cal()
        user.details()
        print("Previous Balance:", P)
        print("Amount to be paid:",g.A)
    elif city == "6":
        class Cal():
            Amount = 0
            if 0 <= I <= 50:
                Amount = P + I * 3.5
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 51 <= I <= 100:
                Amount = P + I * 4.65
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 101 <= I <= 300:
                Amount = P + I * 5.95
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 301 <= I <= 750:
                Amount = P + I * 7.16
                GST = (Amount * 18) / 100
                A = GST + Amount
            else:
                Amount = P + I * 8.92
                GST = (Amount * 18) / 100
                A = GST + Amount
        g = Cal()
        user.details()
        print("Previous Balance:", P)
        print("Amount to be paid:",g.A)
    elif city == "7":
        class Cal():
            Amount = 0
            if 0 <= I <= 50:
                Amount = P + I * 4.05
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 51 <= I <= 100:
                Amount = P + I * 5.15
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 101 <= I <= 400:
                Amount = P + I * 6.41
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 401 <= I <= 800:
                Amount = P + I * 8.16
                GST = (Amount * 18) / 100
                A = GST + Amount
            elif 801 <= I <= 1550:
                Amount = P + I * 9.25
                GST = (Amount * 18) / 100
                A = GST + Amount
            else:
                Amount = P + I * 10.9
                GST = (Amount * 18) / 100
                A = GST + Amount
        g = Cal()
        user.details()
        print("Previous Balance:", P)
        print("Amount to be paid:",g.A)
    else:
        print("INVALID SELECTION")
else:
    print("INVALID SELECTION")