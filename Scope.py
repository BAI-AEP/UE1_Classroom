total_price = 0


def calculate_total_price(price_per_day, num_days):
    total_price = price_per_day * num_days
    print(total_price)
    return total_price


print(total_price)
total_price_of_f = calculate_total_price(100.5, 5)
print(total_price)
print(total_price_of_f)
