import time
import os
def limpiar():
    os.system('cls' if os.name=='nt' else 'clear')
rojo = "\033[31m"
res = "\033[0m"
neg = "\033[1m"
ver = "\033[32m"
ama = "\033[33m"
def sep():
    print(f"{rojo+neg}※{res}" * 38)


def dibujar_tabla(headers, filas):

    anchos = []
    for i, h in enumerate(headers):
        max_col = max(len(str(f[i])) for f in filas) if filas else 0
        anchos.append(max(len(h), max_col))


    def sep(izq, mid, der, rel):
        partes = [rel * (a + 2) for a in anchos]
        return ama + izq + mid.join(partes) + der + res


    def fila(datos, color=""):
        celdas = [f" {color}{str(d).ljust(a)}{res} " for d, a in zip(datos, anchos)]
        return ama + "║" + res + (ama + "║" + res).join(celdas) + ama + "║" + res
    print(sep("╔", "╦", "╗", "═"))
    print(fila(headers, neg+ver))
    print(sep("╠", "╬", "╣", "═"))
    for f in filas:
        print(fila(f))
    print(sep("╚", "╩", "╝", "═"))



def spinner(mensaje="Cargando", duracion=2):
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    fin = time.time() + duracion
    i = 0
    while time.time() < fin:
        print(f"\r{ama}{frames[i % len(frames)]}{res} {mensaje}...", end="", flush=True)
        time.sleep(0.08)
        i += 1
    print(f"\r{ver}{neg}✔{res} {mensaje} completado.")



def barra_progreso(mensaje="Procesando", duracion=2, ancho=30):
    fin = time.time() + duracion
    while True:
        transcurrido = time.time() - (fin - duracion)
        pct = min(transcurrido / duracion, 1.0)
        lleno = int(ancho * pct)
        vacio = ancho - lleno
        barra = ver + "█" * lleno + res + "░" * vacio
        print(f"\r{mensaje}: [{barra}] {int(pct*100)}%", end="", flush=True)
        if pct >= 1.0:
            break
        time.sleep(0.05)
    print(f"\r{mensaje}: [{ver}{'█'*ancho}{res}] {ver}{neg}100%{res}")



def puntos(mensaje="Cargando", duracion=2):
    frames = ["   ", ".  ", ".. ", "..."]
    fin = time.time() + duracion
    i = 0
    while time.time() < fin:
        print(f"\r{ama}{mensaje}{frames[i % len(frames)]}{res}", end="", flush=True)
        time.sleep(0.3)
        i += 1
    print(f"\r{ver}{neg}✔ {mensaje} listo.{res}     ")

# ==========================================
#* Funcion de verificacion de @gmail.com
# ==========================================
def validar_email(email):
    if not email.endswith("@gmail.com"):
        return False
    parte_local = email.replace("@gmail.com", "")
    if len(parte_local) == 0:
        return False
    return True
# ==============================
#* Funciones de validacion
# ==============================
def error(mensaje):
    print(rojo + neg + "✘ " + mensaje + res)
 
def ok(mensaje):
    print(ver + neg + "✔ " + mensaje + res)
 
def pedir_int(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        error("Debes ingresar un número entero")
        return None
 
def pedir_float(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        error("Debes ingresar un número válido")
        return None
 
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
def register_clients(clients, name, email):
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
 
# ==============================
#* Creat Pedidos
# ==============================
def create_orders(orders, clients, products, id_client, id_product, quantity):
    if id_client not in clients:
        return None, orders
 
    if id_product not in products:
        return None, orders
 
    product = products[id_product]
    price = product[2]
    total = price * quantity
 
    orders_id = id_generate(orders)
 
    orders[orders_id] = {
        "clients": clients[id_client]["name"],
        "product": product[1],
        "unit_price": price,
        "quantity": quantity,
        "total": total
    }
 
    return orders_id, orders
 
# ==============================
#* Consultar pedidos
# ==============================
def check_orders(orders):
    if not orders:
        return None
    result = ""
    for orders_id, data in orders.items():
        result += f"ID: {orders_id}| Client: {data['clients']} | Product: {data['product']} | Quantity: {data['quantity']} | Total: {data['total']}\n"
    return result
 
# ==============================
#* Calcular ingresos
# ==============================
def calculate_income(orders):
    total_day = sum(valor["total"] for valor in orders.values())
    return total_day
 
def final_record(orders):
    if not orders:
        return rojo + neg + " ✘ No hay nada registrado" + res
    total_orders = len(orders)
    total_income = calculate_income(orders)
    record = "           FINAL RECORD              "
    record += f"\n total income: {total_income}"
    record += f"\n total orders. {total_orders}\n"
    record += "orders:\n"
    for id_orders, datos in orders.items():
        record += f"ID:\n {id_orders}: {datos['clients']} \nbought {datos['product']} \nquantity {datos['quantity']}\n valuer {datos['total']}"
    return record      
#========================================================================================================================
#========================================================================================================================
clients = {}
products = {}
orders = {}
 
option = 1
while option != 0:
    print(ama + "Customer order Management System" + res)
    print(f"\n          {ver + neg} MENU{res} ")
    sep()
    print(f" {ama+neg}1.{res}Register clients\n {ama+neg}2.{res}Register Products\n {ama+neg}3.{res}Create Order\n {ama+neg}4.{res}Check Order\n {ama+neg}5.{res}Calculate income\n {ama+neg}6.{res}final report\n {rojo+neg}0.exit{res}")
    sep()
    option = input("choose a option: ").strip()
    if option == "1":
        limpiar()
        print()
        name_clients = input("   Into name: ").strip()
        if not name_clients:
            error("El nombre y el email no pueden estar vacíos")
        else:
            email_clients = input("into your email: ").strip()
            if not validar_email(email_clients):
                error("El email debe tener palabras antes y terminar en @gmail.com")
            else:
                spinner("Registrando cliente", duracion=1.5)
                id_clients, clients = register_clients(clients, name_clients, email_clients)
                ok(f"registered client {id_clients}")
                print("------------------------------------------------")
 
    elif option == "2":
        limpiar()
        name_product = input("into name: ").strip()
        price_product = pedir_float("Into price: ")
 
        # validacion: nombre vacio o precio invalido o negativo
        if not name_product:
            error("El nombre del producto no puede estar vacío")
        elif price_product is None:
            pass  # pedir_float ya mostró el error
        elif price_product <= 0:
            error("El precio debe ser mayor a 0")
        else:
            spinner("Registrando producto", duracion=1.5)
            id_product, products = register_products(products, name_product, price_product)
            ok(f"Registered {name_product} product with id {id_product}")
 
    elif option == "3":
        limpiar()

        # validacion: que existan clientes y productos antes de pedir datos
        if not clients:
            error("No hay clientes registrados. Registra uno primero")
        elif not products:
            error("No hay productos registrados. Registra uno primero")
        else:
            id_cliente = pedir_int("ID client: ")
            id_product = pedir_int("ID product: ")
            count = pedir_int("Count: ")
 
            # validacion: que ninguno haya fallado y que count sea positivo
            if id_cliente is None or id_product is None or count is None:
                pass  # pedir_int ya mostró el error
            elif count <= 0:
                error("La cantidad debe ser mayor a 0")
            else:
                orders_id, orders = create_orders(orders, clients, products, id_cliente, id_product, count)
 
                # validacion: que el cliente y producto existan en el diccionario
                if orders_id is None:
                    error("El ID de cliente o producto no existe")
                else:
                    ok(f"orders {orders_id} created")
                    print(ama + neg +"It's done"+ res)
                    barra_progreso("Creando pedido", duracion=1.5)
                    print(ver+neg+"Pedido creado"+ res )
    elif option == "4":
        limpiar()
        if not orders:
            error("No hay pedidos aún")
        else:
            headers = ["ID", "Cliente", "Producto", "Cantidad", "Total"]
            filas = [
                [oid, d["clients"], d["product"],f"${d['unit_price']:.2f}", d["quantity"], f"${d['total']:.2f}"]
                for oid, d in orders.items()
            ]
            dibujar_tabla(headers, filas)
    
    elif option == "5":
        limpiar()
        total_day = calculate_income(orders)
        print(f"El total de ventas del dia es {total_day}")
    
    elif option == "6":
        limpiar()
        print(final_record(orders))
 
    elif option == "0":
        limpiar()
        option = int(option)
        barra_progreso("Cerrando cistema", duracion=1.5)
        limpiar()
        sep()
        print()
        print(ama+neg+" Muchas gracias por usar este sistema      "+res)
        print()
        sep()
 
    else:
        error("marque una de las opciones")


   