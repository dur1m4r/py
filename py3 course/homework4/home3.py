def price_difference(fullPrice, monthPay, monthNum):
    overPayment = monthPay * monthNum - fullPrice
    return overPayment

productPrice = int(input("What is the price of the product? "))
product1monthPay = int(input("What is the monthly payment of the first installment plan? "))
product1monthNum = int(input("How many months does the first installment plan last? "))
product2monthPay = int(input("What is the monthly payment of the second installment plan? "))
product2monthNum = int(input("How many months does the second installment plan last? "))
product1Final = price_difference(productPrice, product1monthPay, product1monthNum)
product2Final = price_difference(productPrice, product2monthPay, product2monthNum)
if product1Final > product2Final:
    print ("The second installment plan is better!")
else:
    print ("The first installment plan is better!")


