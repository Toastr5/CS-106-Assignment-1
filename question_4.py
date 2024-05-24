#assign inputs
lname = input("Enter last name ")
credits = float(input("Enter credits taken "))
price_per_credit_hour = 250
lab_fee = 100
#calculate total tuition
tuition = credits * price_per_credit_hour + lab_fee
print ("Total tuition for ", lname, "is", tuition)

# Import and execute contents of question_5.py
exec(open('question_5.py').read())