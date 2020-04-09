# If high income & good credit, eligible for loan
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible for loan")

good_credit = True
criminal_record = False

if good_credit and not criminal_record:
    print("Eligible for loan")