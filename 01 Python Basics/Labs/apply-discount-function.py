"""
In this lab you will write a function that calculates the final price of an item after applying a percentage discount.

For example, if the price of an item is 50 and a discount of 20 is applied, the discount amount is 10, and the final price is 40.
"""


# isinstance can be used to test if a variable is of several types and support object inheritance
def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    if price <= 0:
        return "The price should be greater than 0"
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    new_price = price - (price * (discount / 100))
    return new_price
