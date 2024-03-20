class Ownable:
    def __init__(self, owner, wallet=0):
        self.owner = owner
        self.wallet = wallet

    def transfer_ownership(self, new_owner):
        self.owner = new_owner

class Item(Ownable):
    def __init__(self, name, price, owner):
        super().__init__(owner)
        self.name = name
        self.price = price
        self.quantity = 0

    def transfer_ownership(self, new_owner):
        super().transfer_ownership(new_owner)

class Cart(Ownable):
    def __init__(self, owner, wallet=0):
        super().__init__(owner, wallet)
        self.items = []

    def add_item(self, item, quantity):
        item.quantity = quantity
        self.items.append(item)
        # Actualizar el monto de la billetera después de agregar el artículo al carrito
        self.wallet -= item.price * quantity

    def checkout(self):
        total_price = sum(item.price * item.quantity for item in self.items)
        if self.wallet >= total_price:
            for item in self.items:
                item.transfer_ownership(self.owner)
            self.items.clear()
            print("Compra exitosa.")
        else:
            print("¡Fondos insuficientes en la billetera!")

    def show_cart_contents(self):
        print("🛒 Contenido del carrito")
        if self.items:
            print("+------+---------------------+------------+")
            print("| Número | Nombre del producto | Cantidad   |")
            print("+------+---------------------+------------+")
            for i, item in enumerate(self.items):
                print(f"| {i} | {item.name:<20} | {item.quantity:^10} |")
            print("+------+---------------------+------------+")
        else:
            print("¡El carrito está vacío!")

# Ejemplo de uso
if __name__ == "__main__":
    owner_cart = input("🤖 Por favor ingrese su nombre: ")
    wallet_amount = float(input("🏧 Ingrese el monto en su billetera: "))
    cart = Cart(owner_cart, wallet_amount)

    items = [
        Item("SSD de 2,5 pulgadas", 13370, "Propietario del Artículo"),
        Item("Disco duro de 3,5 pulgadas", 10980, "Propietario del Artículo"),
        Item("CPU", 40830, "Propietario del Artículo"),
        Item("Enfriador de CPU", 13400, "Propietario del Artículo"),
        Item("SSD M.2", 12980, "Propietario del Artículo"),
        Item("Caja de PC", 8727, "Propietario del Artículo"),
        Item("Tarjeta gráfica", 23800, "Propietario del Artículo"),
        Item("Placa base", 28980, "Propietario del Artículo"),
        Item("Memoria", 13880, "Propietario del Artículo"),
        Item("Unidad de alimentación", 8980, "Propietario del Artículo")
    ]
    print("📜 Lista de productos")
    print("+------+---------------------+------------+")
    print("| Número | Nombre del producto | Precio     |")
    print("+------+---------------------+------------+")
    for i, item in enumerate(items):
        print(f"| {i} | {item.name:<20} | ${item.price:^10} |")
    print("+------+---------------------+------------+")

    while True:
        try:
            product_number = int(input("⛏ Por favor ingrese el número de producto: "))
            quantity = int(input("⛏ Ingrese la cantidad del producto: "))
            cart.add_item(items[product_number], quantity)
        except (ValueError, IndexError):
            print("⚠️ Ingrese un número válido.")
        choice = input("😭 ¿Terminar de comprar? (sí/No): ").lower()
        if choice == "sí":
            break

    cart.show_cart_contents()

    confirm_purchase = input("💸 ¿Confirmas tu compra? (sí/No): ").lower()
    if confirm_purchase == "sí":
        cart.checkout()
        print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultados")
        print(f"🛍️ {owner_cart} propiedad")
        cart.show_cart_contents()
        print(f"😱👛 Saldo de la billetera de {owner_cart}: {cart.wallet}")
    else:
        print("Compra cancelada.")
