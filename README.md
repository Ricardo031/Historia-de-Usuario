# Historia-de-Usuario
Customer Order Management System

This project is a simple console-based system developed in Python to manage customers, products, and orders.

Features

- Register clients
-  Register products
-  Create orders
-  View orders
-  Calculate income

Code Explanation

- id_generate :
  Generate a dictionary that save de id of the clients.
- Dictionary:
  Used to store data such as clients, products, and orders.

- Clients:
  Each client is stored with a name and email.

- Menu (while op != 0: ):
  A loop ("while option != 0") keeps the program running until the user selects option 0 (exit).

```python
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
     
```
- Menu options:
  The program displays a menu so the user can choose what action to perform.

- User input (option variable):
  The user selects an option and enters data such as name and email when registering a client.
