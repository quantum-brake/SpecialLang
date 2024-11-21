from abc import ABC, abstractmethod

class DataTypes(ABC):
    def create_data(self, data_type):
        if data_type == "posts":
            return self.add_post_data()
        elif data_type == "comments":
            return self.add_comment_data()
        elif data_type == "todos":
            return self.add_todo_data()
        elif data_type == "users":
            return self.add_user_data()
        else:
            print("Невідомий тип даних.")
            return None

    @abstractmethod
    def add_post_data(self):
        pass

    @abstractmethod
    def add_comment_data(self):
        pass

    @abstractmethod
    def add_todo_data(self):
        pass

    @abstractmethod
    def add_user_data(self):
        pass