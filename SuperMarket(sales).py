# A supermarkets monthly sales analysis system
# Provide code that should take number of days in a month and number of products sold for each day
# The program should accept each product name and its sold quantity on that day
# Calculate the total quantity sold for each product across all days and compute the overall sales quantity for entire month
# Finally, display the summary of day-wise sales, product-wise total sales, and overall sales quantity for the month
def sales_analysis(num_days):
    product_sales = {}
    day_wise_sales = []

    for day in range(1, num_days + 1):
        print(f"Day {day}:")
        daily_sales = {}
        num_products = int(input("Enter number of products sold today: "))
        
        for _ in range(num_products):
            product_name = input("Enter product name: ")
            quantity_sold = int(input("Enter quantity sold: "))
            
            if product_name in daily_sales:
                daily_sales[product_name] += quantity_sold
            else:
                daily_sales[product_name] = quantity_sold
            
            if product_name in product_sales:
                product_sales[product_name] += quantity_sold
            else:
                product_sales[product_name] = quantity_sold
        
        day_wise_sales.append(daily_sales)

    print("\nDay-wise Sales Summary:")
    for day, sales in enumerate(day_wise_sales, start=1):
        print(f"Day {day}: {sales}")

    print("\nProduct-wise Total Sales Summary:")
    for product, total_quantity in product_sales.items():
        print(f"{product}: {total_quantity}")

    overall_sales_quantity = sum(product_sales.values())
    print(f"\nOverall Sales Quantity for the Month: {overall_sales_quantity}")


# ⭐ ADD THIS (VERY IMPORTANT)
num_days = int(input("Enter number of days in the month: "))
sales_analysis(num_days)
