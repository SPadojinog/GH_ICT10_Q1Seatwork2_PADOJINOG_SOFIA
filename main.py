# Seatwork#2
from pyscript import display


# String
restaurant_name = 'Silver Spoon'
owner_name = 'Sofia Laurence F. Padojinog'

year_established = 2000 # Integer

popular_item_price = 250.00 # Float

has_delivery = True # Boolean

# List
product_names = ['Jolly Spagetti', 'Fried Chicken', 'Burger Steak', 'Kid Salad', 'Candy Portion']
business_hours = ['Opens', '8:01 AM', '10:01 PM']
menu_prices = ['PHP 250.00','PHP 300.00','PHP 200.00','PHP 400.00','PHP 160.00']
common_allergen = ['Peanuts', 'Dairy', 'Shellfish']

tax_rate = 0.09 # Float

display(f'{restaurant_name}', target="RN")
display(f'Owner: {owner_name}', target="ON")
display(f'Since {year_established}', target="EY")
display(f'Popular Product:' , target="Pr")
display(f'Price (PHP)', target="Po")
display(f'{menu_prices[0]}', target="P1")
display(f'{menu_prices[1]}', target="P2")
display(f'{menu_prices[2]}', target="P3")
display(f'{menu_prices[3]}', target="P4")
display(f'{menu_prices[4]}', target="P5")
display(f'{product_names[0]}', target="F1")
display(f'{product_names[1]}', target="F2")
display(f'{product_names[2]}', target="F3")
display(f'{product_names[3]}', target="F4")
display(f'{product_names[4]}', target="F5")
display(f'{business_hours[0]} {business_hours[1]} - {business_hours[2]}', target="BH")
display(f'Dine-in Available', target="DIA")