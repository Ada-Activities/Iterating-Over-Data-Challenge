def calculate_total_sales(sales_totals):
    total = 0
    for value in sales_totals.values():
        total += (value["quantity"] * value["price"])

    return total

def calculate_average_sales(sales_totals):
    if not sales_totals:
        return 0
    
    total = calculate_total_sales(sales_totals)
    return total / len(sales_totals)

def filter_to_better_than_average_sales(sales_totals):
    average = calculate_average_sales(sales_totals)

    filtered = {}
    for key, value in sales_totals.items():
        product_sales = value["quantity"] * value["price"]
        if product_sales > average:
            filtered[key] = value

    return filtered
    
def ninety_nine_bottles(count, beverage):
    lines = []
    for bottles_left in range(count, 0, -1):
        if bottles_left != 1:
            lines.append(f"{bottles_left} bottles of {beverage} on the wall, {bottles_left} bottles of {beverage}")
            if bottles_left != 2:
                lines.append(f"If one of those bottles should happen to fall, {bottles_left - 1} bottles of {beverage} on the wall")
            else:
                lines.append(f"If one of those bottles should happen to fall, {bottles_left - 1} bottle of {beverage} on the wall")                
        else:
            lines.append(f"{bottles_left} bottle of {beverage} on the wall, {bottles_left} bottle of {beverage}")
            lines.append(f"If one of those bottles should happen to fall, {bottles_left - 1} bottles of {beverage} on the wall")

    return lines    

