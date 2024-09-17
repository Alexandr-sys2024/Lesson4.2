class User:
    def __init__(self, user_id: int, name: str):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'  # Уровень доступа по умолчанию для обычных пользователей

    # Методы для получения данных
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Метод для установки имени (если нужно изменить имя)
    def set_name(self, name: str):
        self.__name = name


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администратора

    # Метод для добавления пользователя
    def add_user(self, user_list: list, user: User):
        user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен в систему.")

    # Метод для удаления пользователя
    def remove_user(self, user_list: list, user_id: int):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален из системы.")
                return
        print(f"Пользователь с ID {user_id} не найден.")


# Пример использования
if __name__ == "__main__":
    # Создаем администратора
    admin = Admin(1, "Alice")

    # Создаем несколько обычных пользователей
    user1 = User(2, "Bob")
    user2 = User(3, "Charlie")

    # Список для хранения пользователей
    user_list = []

    # Администратор добавляет пользователей в систему
    admin.add_user(user_list, user1)
    admin.add_user(user_list, user2)

    # Проверим, кто в системе
    print("\nТекущие пользователи в системе:")
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

    # Администратор удаляет пользователя
    admin.remove_user(user_list, 2)

    # Проверим список после удаления
    print("\nПользователи в системе после удаления:")
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")