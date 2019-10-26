annualIncome = int(input("Enter your annual income: "))
taxfree = None;
if annualIncome <= 6000:
    taxfree = annualIncome
    print ("Your tax-free income is "+str(taxfree)+" euros")
elif annualIncome > 6000 and annualIncome <= 14400:
    taxfree = 6000
    print ("Your tax-free income is "+str(taxfree)+" euros")
elif annualIncome > 14400 and annualIncome <= 25200:
    taxfree = round(6000 - 6000 / 10800 * (annualIncome - 14400), 2)
    print (str(taxfree))
    print ("Your tax-free income is "+str(taxfree)+" euros")
elif annualIncome > 25200:
    print ("Your tax-free income is 0 euros")