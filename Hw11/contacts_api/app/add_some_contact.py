import requests



url = "http://127.0.0.1:8000/contacts/"

for i in range(10):
    new_contact = {
        "first_name": f"Denys{i}",
        "last_name": f"Shtoma{i}",
        "email": f"DEn.Shtoma{i}@example.com",
        "phone": "+1234567890",
        "birthday": "1990-01-01",
        "additional_info": f"Some additional info{i}"
    }
    response = requests.post(url, json=new_contact)
    print(response.json())