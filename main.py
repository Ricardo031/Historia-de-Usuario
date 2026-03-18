# ==============================
#* Genaracion de ID 
# ==============================
def id_generate(dictionary):
    if dictionary:
        return max(dictionary.keys()) + 1
    else:
        return 1
    
# ==============================
#* Registrar Clientes
# ==============================
def register_clients(clients,name,email):
    client_id = id_generate(clients)

    clients[client_id] = {
        "name": name,
        "email": email
    }

    return client_id, clients

# ==============================
#* Registrar products
# ==============================
def register_products(products, name, price):
    product_id = id_generate(products)

    product = (product_id, name, price)
    products[product_id] = product
    return product_id, products

def create_orders(orders, clients, products, id_client, id_product, quantity):
    if id_client not in clients:
        return "Cliente no existe", orders

    if id_product not in products:
        return "product no existe", orders

    product = products[id_product]
    price = product[2]
    total = price * quantity

    orders_id = id_generate(orders)

    orders[orders_id] = {
        "clients": clients[id_client]["name"],
        "product": product[1],
        "quantity": quantity,
        "total": total
    }

    return f"orders {orders_id} created", orders


def check_orders(orders):
    if not orders:
        print("There are not orders yet")
    result = ""
    for orders_id, data in orders.items():
        result += f"ID: {orders_id}| Client: {data['clients']} | Product: {data['product']} | Quantity: {data['quantity']} | Total: {data['total']}"
    
    return result

#%Todo: agregar lo demas 

clients = {}
products = {}
orders = {}

option = 1
while option != 0:
    print("\033[1;32mCustomer order Management System \033[0m")
    print("======== MENU =========")
    print(" 1.Register clients\n 2.Register Products\n 3.Create Order\n 4.Check Order\n 5.Calculate income\n 6.final report\n 0.exit" )

    option = int(input("choose a option: "))

    if option == 1:
        name_clients = input("into name: ")
        email_clients = input("into your email: ")
        id_clients, clients = register_clients(clients, name_clients,email_clients)

        print(f"registered client {id_clients}" )
        print("------------------------------------------------")

    elif option == 2:
        name_product = input("into name: ")
        price_product = float(input("Into price: "))
        id_product, products = register_products(products, name_product, price_product)
        print(f"Registered {name_product} product with {id_product}")

    elif option == 3:
        id_cliente = int(input("ID client: "))
        id_product = int(input("ID product: "))
        count = int(input("Count: "))
        mensaje, pedidos = create_orders(orders, clients, products, id_clients, id_product, count)
        print(mensaje)
        print("\033[31m" + "It's done" + "\033[0m")
     
    elif option == 4:
        print(check_orders(orders))
    
   