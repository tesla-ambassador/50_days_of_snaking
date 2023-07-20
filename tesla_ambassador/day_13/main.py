# Write a function called your_vat. The function takes no parameter. 
# The function asks the user to input the price of an item and VAT (vat should be a percentage). 
# The function should return the price of the item plus VAT. 
# If the price is 220 and, VAT is 15% your code should return a vat inclusive price of 253. 
# Make sure that your code can handle ValueError. 
# Ensure the code runs until valid numbers are entered. (hint: Your code should include a while loop).

def your_vat():
    false_input = True
    while false_input:
        pdt_price = input('Please enter the price of the item: $')
        pdt_vat = input('Please enter the vat: ')
        if pdt_price.isnumeric() and pdt_vat.isnumeric():
            price_num = int(pdt_price)
            vat_num = int(pdt_vat)
            total = ((vat_num/100) * price_num) + price_num
            false_input = False
            return total
        
print(your_vat())

