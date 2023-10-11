FatherIncome = 3500
MotherIncome = 4000
NumberOfFamilyMembers = 3
TotalIncome = FatherIncome + MotherIncome
IncomePerPerson = TotalIncome/NumberOfFamilyMembers

message = (
    f"Father’s income: {FatherIncome}\n"
    f"Mother’s income: {MotherIncome}\n"
    f"Number of people in family: {NumberOfFamilyMembers}\n"
    f"Total income: {TotalIncome}\n"
    f"Income per person: {IncomePerPerson}\n"
)
print(message)