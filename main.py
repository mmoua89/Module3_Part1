"""
Author: Meng Moua
Course: CSC500
Assignment: Module 3, Part 1
"""

def main():
    meal_cost = input('A meal cost $')
    if not valid_number(meal_cost):
        print('The meal cost is invalid.')
        return

    if float(meal_cost) < 0:
        print('Please try again. The meal cost must be a positive number.')
        return

    # Cost calculation
    tax = sale_tax(meal_cost)
    tip = tip_amount(meal_cost)
    total = float(meal_cost) + tax + tip

    # precision with alignment
    width = 15

    # Display the amounts with formatting
    print(f'{"Meal cost":<{width}}: ${float(meal_cost):.2f}')
    print(f'{"Sales tax (7%)":<{width}}: ${tax:.2f}')
    print(f'{"Tip (18%)":<{width}}: ${tip:.2f}')
    print(f'{"Total":<{width}}: ${total:.2f}')

def sale_tax(cost) -> float:
    """
    Calculate the sale tax
    :param cost: the cost
    :return: sale tax amount
    """
    return float(cost) * 0.07

def tip_amount(cost) -> float:
    """
    Calculate the tip amount
    :param cost: the cost
    :return: tip amount
    """
    return float(cost) * 0.18

def valid_number(num) -> bool:
    """
    Validate a number
    :param num: a number
    :return: true or false
    """
    try:
        float(num)
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    main()
