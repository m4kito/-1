import json
import os

FILE_NAME = "products.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(products):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def get_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

def add_product(products):
    try:
        product_id = int(input("Введите ID товара: "))
        if get_product(products, product_id) is not None:
            print("Товар с таким ID уже существует.")
            return
        name = input("Введите название товара: ")
        price = float(input("Введите цену товара: "))
        weight = float(input("Введите вес товара: "))
        supplier = input("Введите поставщика товара: ")

        products.append({
            "id": product_id,
            "name": name,
            "price": price,
            "weight": weight,
            "supplier": supplier
        })
        save_data(products)
        print("Товар добавлен")
    except ValueError:
        print("Некорректный ввод")

def get_product_by_id(products):
    try:
        product_id = int(input("Введите ID товара: "))
        product = get_product(products, product_id)
        if product:
            print(f"ID: {product['id']}, Название: {product['name']}, Цена: {product['price']}, Вес: {product['weight']}, Поставщик: {product['supplier']}")
        else:
            print("Товар не найден")
    except ValueError:
        print("Некорректный ID")

def update_product(products):
    try:
        product_id = int(input("Введите ID товара для изменения: "))
        product = get_product(products, product_id)
        if product is None:
            print("Товар не найден")
            return

        name = input(f"Новое название (текущее: {product['name']}): ")
        price_str = input(f"Новая цена (текущая: {product['price']}): ")
        weight_str = input(f"Новый вес (текущий: {product['weight']}): ")
        supplier = input(f"Новый поставщик (текущий: {product['supplier']}): ")

        if name:
            product["name"] = name
        if price_str:
            product["price"] = float(price_str)
        if weight_str:
            product["weight"] = float(weight_str)
        if supplier:
            product["supplier"] = supplier

        save_data(products)
        print("Товар обновлён")
    except ValueError:
        print("Некорректные данные")

def delete_product(products):
    try:
        product_id = int(input("Введите ID товара для удаления: "))
        product = get_product(products, product_id)
        if product:
            products.remove(product)
            save_data(products)
            print("Товар удалён")
        else:
            print("Товар не найден")
    except ValueError:
        print("Некорректный ID.")

def list_products(products):
    if not products:
        print("Список товаров пуст")
        return
    for product in products:
        print(f"ID: {product['id']}, Название: {product['name']}, Цена: {product['price']}, Вес: {product['weight']}, Поставщик: {product['supplier']}")

def main():
    products = load_data()

    while True:
        print("\nВыберите действие:")
        print("1 - Добавить товар")
        print("2 - Получить товар по ID")
        print("3 - Изменить товар")
        print("4 - Удалить товар")
        print("5 - Показать все товары")
        print("0 - Выход")

        choice = input("Введите номер команды: ").strip()
        if choice == "1":
            add_product(products)
        elif choice == "2":
            get_product_by_id(products)
        elif choice == "3":
            update_product(products)
        elif choice == "4":
            delete_product(products)
        elif choice == "5":
            list_products(products)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор команды.")

if __name__ == "__main__":
    main()
