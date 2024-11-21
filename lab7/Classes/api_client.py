import requests


class APIClient:
    _instance = None

    def __new__(cls, base_url):
        if cls._instance is None:
            cls._instance = super(APIClient, cls).__new__(cls)
            cls._instance.base_url = base_url
        return cls._instance

    def get_data(self, endpoint):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Помилка API: {e}")
            return None
