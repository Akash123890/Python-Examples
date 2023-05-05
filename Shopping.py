# ex:
#   less then 0 is raise Exception "Enter Amount is wrong"
#   less then 1000 -> no discount
#   1000 - 1999.99  -> 5% discount
#   2000 - 2999.99  -> 10% Discount
#   3000 - 4999.99  -> 15% Discount
# more then 5000 or 5000    -> 20% Discount
# Result:
# Shopping  Amount  :   XXXX.XX
# Discount Amount   :   XXXX.XX
# Payable Amount    :   XXXX.XX


shopping_amount = float(input("Please Enter Shopping Amount : "))
discount_amount = 0
payable_amount = 0

if shopping_amount < 0:
    print(f"{shopping_amount} Amount is wrong")
    exit(0)
elif shopping_amount < 1000:
    discount_amount = shopping_amount * 0
elif shopping_amount < 2000:
    discount_amount = shopping_amount * 0.05
elif shopping_amount < 3000:
    discount_amount = shopping_amount * 0.1
elif shopping_amount < 5000:
    discount_amount = shopping_amount * 0.15
else:
    discount_amount = shopping_amount * 0.2

payable_amount = shopping_amount - discount_amount

print(f"Shopping  Amount  : {shopping_amount}")
print(f"Discount Amount   : {discount_amount}")
print(f"Payable Amount    : {payable_amount}")
