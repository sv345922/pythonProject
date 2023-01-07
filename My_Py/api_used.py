import requests
import sys

def numbersAPI():
    """Выполняет API запросы на сойте numbersapi.com из файла и печатает поле text"""
    answer = ("Boring", "Interesting")
    with open("dataset_24476_3.txt", "r") as file:
        for line in file:
            num = line.rstrip()
            site_req = f"http://numbersapi.com/{num}/math?json=true"
            response = requests.get(site_req)
            result = response.json()
            # print(answer[1] if bool(result["found"]) else answer[0], end=" ")
            print(result["text"])

numbersAPI()