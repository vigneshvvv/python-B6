class Product:
    def __init__(self, id = 0, product_name = "", price = 0):
        self.id = id
        self.product_name = product_name
        self.price = price

con = Product(1, "Mobile", 30000)
print(con.price)
con2 = Product()
con2.id = 2
con2.price= 10000
print(con2.price)