class DataRepository:
    def __init__(self, api_client):
        self.api_client = api_client
        self.local_data = {
            "posts": [],
            "comments": [],
            "todos": [],
            "users": []
        }
        self.id_counters = self.initialize_id_counters()

    def initialize_id_counters(self):
        id_counters = {}
        for data_type in self.local_data.keys():
            api_data = self.api_client.get_data(data_type) or []
            max_id = max((item["id"] for item in api_data), default=0)
            id_counters[data_type] = max_id + 1
        return id_counters

    def fetch_data(self, data_type):
        api_data = self.api_client.get_data(data_type) or []
        return api_data + self.local_data[data_type]

    def add_data(self, data_type, data):
        data["id"] = self.id_counters[data_type]
        self.local_data[data_type].append(data)
        self.id_counters[data_type] += 1
        return data

    def delete_data(self, data_type, record_id):
        original_length = len(self.local_data[data_type])
        self.local_data[data_type] = [item for item in self.local_data[data_type] if item["id"] != record_id]
        if len(self.local_data[data_type]) < original_length:
            print(f"Запис з id={record_id} видалено з {data_type}.")
            return True
        print(f"Запис з id={record_id} не знайдено в {data_type}.")
        return False