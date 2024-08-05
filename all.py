
# Maqsad 1:

# with open("product.txt", "r") as file:
#     products = file.readlines()

# result = []
# for product in products:
#     data = product.strip().split(',')
#     product_id = data[0]
#     material = data[2]
#     price = float(data[3].replace('$', ''))
#     in_stock = data[4] == "true"
    
#     if 500 <= price <= 1000 and in_stock:
#         result.append((product_id, material))

# print("Narxi 500 va 1000 dollar orasida bo'lgan va omborda mavjud bo'lgan produktlar:")
# for item in result:
#     print(f"ID: {item[0]}, Material: {item[1]}")

# Maqsad 2:

# material_name = input("Material nomini kiriting: ")

# matching_products = []

# with open("product.txt", "r") as file:
#     products = file.readlines()

# for product in products:
#     data = product.strip().split(',')
#     material = data[2]
#     price = float(data[3].replace('$', ''))
#     in_stock = data[4] == "true"
    
#     if material == material_name and in_stock:
#         matching_products.append(price)

# matching_products.sort()

# print(f"Omborda mavjud bo'lgan {material_name} materialidagi produktlar narxlari (o'sish tartibida):")
# for price in matching_products:
#     print(f"${price:.2f}")


# Maqsad 3:

# result = []

# with open("product.txt", "r") as file:
#     products = file.readlines()

# for product in products:
#     data = product.strip().split(',')
#     material = data[2]
#     price = float(data[3].replace('$', ''))
#     in_stock = data[4] == "false"
    
#     if price < 1000 and not in_stock:
#         result.append(material)

# print("Omborda mavjud bo'lmagan va narxi 1000 dollardan arzon bo'lgan tovarlarning ishlab chiqarilgan materiallari:")
# for material in result:
#     print(material)
