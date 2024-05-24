#input values
Lname = input("Enter last name ")
hours = float(input("Number of hours worked "))
pay_rate = float(input("Pay rate "))
#calculate total pay
pay = hours * pay_rate
print(Lname, "pay is", pay)

# Import and execute contents of question_3.py
exec(open('question_3.py').read())