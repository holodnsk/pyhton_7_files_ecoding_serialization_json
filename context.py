def get_context(brand, model, fuel, price):  # возвращает словарь аргументов
    return {
        'brand': brand,
        'model': model,
        'fuel': fuel,
        'price': price,
    }