import xml.etree.ElementTree as ET

tree = ET.parse('data/food.xml')
menu = tree.getroot()
breakfast_menu = menu.findall("food")
foods = []
for food in breakfast_menu:
    foods.append(
        {
            "name": food.findtext("name"),
            "price": food.findtext("price"),
            "description": food.findtext("description"),
            "calories": food.findtext("calories"),
        }
    )

print(foods)
print(menu.tag)