def shopping_list(budget, **kwargs):
    if budget < 100:
        return 'You do not have enough budget.'
    result = ''
    my_dict = {}
    for k, v in kwargs.items():
        if len(my_dict) == 5:
            break
        cost, quantity = v
        price_current_product = cost * quantity
        if budget >= price_current_product:
            my_dict[k] = price_current_product
    for item, price in my_dict.items():
        result += f"You bought {item} for {price:.2f} leva." + '\n'
    return result
