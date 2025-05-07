

high_income = True
good_credit = False
student = False

# "and" both shound be true
# "or"  One Condition should be true
# "not" inverses the condition

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
if not student:
    print("Eligiable")  # Only executes if the condition is Flase


# Short-Circuit Evaluation


if high_income and good_credit and not student:
    print("Eligiable")
