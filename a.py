import requests

url = "http://127.0.0.1:5000/api/attendance"
headers = {"Content-Type": "application/json"}

data = {
    "student_id": 1,
    "course_id": 1,
    "date": "2025-03-11",
    "status": True
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
