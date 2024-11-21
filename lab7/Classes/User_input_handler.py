from Classes.data_types import DataTypes

class UserInputHandler(DataTypes):
    def __init__(self, repo):
        self.repo = repo

    def select_data_type(self):
        data_type = input("Оберіть тип даних (posts, comments, todos, users): ").strip().lower()
        if data_type in ["posts", "comments", "todos", "users"]:
            return data_type
        print("Невірний вибір типу даних.")
        return None

    def add_post_data(self):
        user_id = input("Введіть userID: ").strip()
        title = input("Введіть заголовок поста: ").strip()
        body = input("Введіть текст поста: ").strip()
        data = {"userID": int(user_id), "id": self.repo.id_counters["posts"], "title": title, "body": body}
        return data

    def add_comment_data(self):
        post_id = input("Введіть postID: ").strip()
        name = input("Введіть ім'я коментатора: ").strip()
        email = input("Введіть email коментатора: ").strip()
        body = input("Введіть текст коментаря: ").strip()
        data = {"postID": int(post_id), "id": self.repo.id_counters["comments"], "name": name, "email": email, "body": body}
        return data

    def add_todo_data(self):
        user_id = input("Введіть userID: ").strip()
        title = input("Введіть заголовок задачі: ").strip()
        completed = input("Чи виконана задача (True/False): ").strip()
        data = {"userID": int(user_id), "id": self.repo.id_counters["todos"], "title": title, "completed": completed == "True"}
        return data

    def add_user_data(self):
        name = input("Введіть ім'я користувача: ").strip()
        username = input("Введіть username: ").strip()
        email = input("Введіть email: ").strip()
        address = input("Введіть адресу: ").strip()
        phone = input("Введіть номер телефону: ").strip()
        website = input("Введіть вебсайт: ").strip()
        company = input("Введіть компанію: ").strip()
        data = {"id": self.repo.id_counters["users"], "name": name, "username": username, "email": email, "address": address, "phone": phone, "website": website, "company": company}
        return data

    def delete_data(self):
        data_type = self.select_data_type()

        if data_type:
            try:
                record_id = int(input("Введіть ID запису для видалення: ").strip())
                self.repo.delete_data(data_type, record_id)
                return data_type, record_id
            except ValueError:
                print("Невірний формат ID. Введіть числове значення.")
