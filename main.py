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

#%Todo: agregar lo demas 





clients = {}
products = {}
ordes = {}

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

