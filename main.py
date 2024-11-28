from pymongo import MongoClient, errors

# Подключение к MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")  # Убедитесь, что MongoDB запущен
    db = client['test_database']  # Создаем/подключаемся к базе данных
    collection = db['products']  # Создаем/подключаемся к коллекции
    print("Подключение к MongoDB успешно")
except errors.ConnectionError as e:
    print(f"Ошибка подключения к MongoDB: {e}")
    exit()

# Пример данных
items = [
    {"name": "Product 1", "price": 10.0},
    {"name": "Product 2", "price": 20.0},
]

# Загрузка данных
try:
    collection.insert_many(items, ordered=False)  # Используем ordered=False, чтобы игнорировать дубли
    print("Данные успешно добавлены в MongoDB")
except errors.BulkWriteError as e:
    print(f"Ошибка при вставке данных: {e.details}")

# Пример запросов
try:
    # Все данные
    all_data = list(collection.find())
    print("Все данные:", all_data)

    # Данные с ценой больше 10
    filtered_data = list(collection.find({"price": {"$gt": 10}}))
    print("Данные с ценой больше 10:", filtered_data)
except errors.PyMongoError as e:
    print(f"Ошибка при выполнении запроса: {e}")