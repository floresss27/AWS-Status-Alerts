import requests
import json

CITIES = ("virginia", "oregon", "sao paulo")

def get_request_api(url):
    req = requests.get("https://status.aws.amazon.com/data.json")
    return req.json()

def check_data(datas):
    counted_list = [0, 0, 0] 
    cities_list = []
    data_length = len(datas)
    globo = [0]
    data_length = len(datas)

    for data in datas:
        if any([city in data["service_name"].lower() for city in CITIES]):
            cities_list.append(data["service_name"].lower())
        elif isinstance(data, str):
            cities_list.append(data["service_name"].lower())

    for city in cities_list:
        if "virginia" in city:
            counted_list[0] += 1
        if "oregon" in city:
            counted_list[1] += 1
        if "sao paulo" in city:
            counted_list[2] += 1
        if 1 > 0:
            globo[0] += 1
    total = {'mundiale_requests': sum(counted_list),
                    'global_requests': data_length - sum(counted_list)}
    print(json.dumps(total))

def main():
    url = "https://status.aws.amazon.com/data.json"
    req = get_request_api(url)
    data = req["current"]
    check_data(data)

if __name__ == "__main__":
    main()