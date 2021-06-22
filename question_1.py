# Data from bank
customers = ["James","John","Robert","Mary","Patricia","Jennifer"]
salary = [155000,755000,455000,1255000,635000,575000]
taxes = [55800,317100,182000,451800,171450,71300]
salary_target = 555000
tax_rate_target = 0.3


for i in range(len(salary)):
    tax_rate = taxes[i] / salary[i]
    if salary[i] > salary_target and ( tax_rate < tax_rate_target ):
        print("Customer " + customers[i] + " pays " + str(tax_rate) + " percent in taxes" + "has a salaray of " + str(salary[i]))