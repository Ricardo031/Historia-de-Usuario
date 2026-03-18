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
#* Registrar Productos
# ==============================
def register_products(products, name, price):
    product_id = id_generate(products)

    product = (product_id, name, price)
    products[product_id] = product
    return product_id, products
def create_orders(orders, clients, products, id_client, id_product, cantidad):
    if id_client not in clients:
        return "Cliente no existe", orders

    if id_product not in products:
        return "Producto no existe", orders

    producto = products[id_product]
    precio = producto[2]

    total = precio * cantidad

    orders_id = id_generate(orders)

    orders[orders_id] = {
        "cliente": clients[id_client]["nombre"],
        "producto": producto[1],
        "cantidad": cantidad,
        "total": total
    }

    return f"orders {orders_id} creado", orders


#%Todo: agregar lo demas 





clients = {}
products = {}
orders = {}

op = 1
while op != 0:
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
        print(f"Registered product {id_product}")
# ==============================
#* Aca se intenta guardar los products para orders
# ==============================
    elif option == 3:
        id_cliente = int(input("ID cliente: "))
        id_producto = int(input("ID producto: "))
        cantidad = int(input("Cantidad: "))
        for product in products:
            if product ["count"] >= 0:
             print (product["name"])

        mensaje, pedidos = create_orders(orders, clients, products, id_cliente, id_producto, cantidad)
        print(mensaje)
        print("\033[31m" + "It's done" + "\033[0m")
     
     


            