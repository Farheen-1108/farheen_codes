# Predefined food items and prices
food_items = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Salad']
prices = (250, 150, 200, 100, 120)

total = 0

while True:
    food = input("Enter food item (or 'done' to finish): ").strip().title()
    if food == 'Done':
        break
    if food in food_items:
        quantity = int(input(f"Enter quantity for {food}: "))
        total += prices[food_items.index(food)] * quantity

gst = total * 0.18 if total > 0 else 0
final_bill = total + gst

print(f"Final Bill: ₹{final_bill:.2f} (Subtotal: ₹{total:.2f}, GST: ₹{gst:.2f})")
