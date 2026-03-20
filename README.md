# Historia-de-Usuario
Customer Order Management System

This project is a simple console-based system developed in Python to manage customers, products, and orders.

We made this with a little bit design with some functions. The propuse it's simple simulate a GUI (Grafic User Interface), through the console you will use the high quality registration. We doesn't use list, only tuples and dicctionary.
# Some functions
## sep()
This function prints a long horizontal line in the console.
It does not return any value because its purpose is visual only.
It uses special characters and color variables to format the output.
Its main goal is to separate sections in the program.
This improves readability when many results are displayed.
It is commonly used in command-line interfaces.
```python
def sep():
    print(f"{rojo+neg}⠶{res}" * 30)
# ==============================
#* Genaracion de ID 
# ==============================
def id_generate(dictionary):
    if dictionary:
        return max(dictionary.keys()) + 1
    else:
        return 1
```
---

## id_generate()
This function generates a unique numeric identifier.
It checks the existing keys in a dictionary.
If there are elements, it takes the largest key and adds one.
If the dictionary is empty, it starts counting from one.
This ensures that no two elements share the same ID.
It is used as a base for all registration functions.

```python
def register_clients(clients,name,email):
    client_id = id_generate(clients)

    clients[client_id] = {
        "name": name,
        "email": email
    }

    return client_id, clients
```
---

## register_clients()
This function stores a new client in the system.
It first generates a unique ID using id_generate.
Then it creates a dictionary with name and email.
This information is stored using the ID as the key.
The function returns both the ID and updated data.
It allows consistent and structured client management.


---

## register_products
This function registers a new product in the system.
It generates a unique product ID automatically.
Then it creates a tuple with id, name, and price.
This tuple is stored inside the products dictionary.
The function returns the ID and updated dictionary.
It standardizes how products are saved and accessed.
```python
def register_products(products, name, price):
    product_id = id_generate(products)

    product = (product_id, name, price)
    products[product_id] = product
    return product_id, products

```

---

## create_orders
This function creates a new order in the system.
It verifies that the client and product exist before proceeding.
If any of them is missing, it returns an error message.
If valid, it calculates the total using price and quantity.
Then it stores all order details in a dictionary.
It returns a confirmation message and updated orders.

```python
def create_orders(orders, clients, products, id_client, id_product, quantity):
    if id_client not in clients:
        return "Cliente no existe", orders  #! camibar para que no muestre un mensaje

    if id_product not in products:
        return "product no existe", orders  #! aqui igual 

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
    #! Cambiar para que solo retorne un valor
```
---

## check_orders
This function retrieves all stored orders.
If there are no orders, it notifies that the list is empty.
If there are orders, it builds a text with all details.
Each order includes client, product, quantity, and total.
The result is returned as a single string.
It is mainly used for displaying information.

---

## calculate_income
This function calculates the total income from orders.
It iterates over all stored orders in the dictionary.
For each order, it extracts the total value.
Then it sums all totals into a single number.
It uses a compact sum expression for efficiency.
The result represents total earnings.

---

## final_record
This function generates a final summary of the system.
If there are no orders, it returns a message indicating it.
Otherwise, it calculates total income and order count.
It builds a formatted text with all relevant information.
This includes totals and detailed order descriptions.
It serves as a final report of system activity.

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
