import requests
from datetime import datetime as dt

now = dt.now()
today = now.date().strftime("%d/%m/%Y")
time=now.time().strftime("%H:%M:%S")
print(time)
query=input("What was your excercise today?")
# _____________________________NUTRITIONIX API Natural language REQUESTS___________________________________
APP_ID = "3b82aef1"
API_KEY = "34aa7c080da8c1eaeebde7349c794a63"

headers_nutri = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
params = {
    "query": query
}

natural_ex_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=natural_ex_endpoint, json=params, headers=headers_nutri)
data = response.json()["exercises"][0]
exercise = data["name"].capitalize()
calories = data["nf_calories"]
duration = data["duration_min"]
print(exercise, calories, duration)
print(response.json())
# _________________________________SHEETY API GET REQUESTS________________________________________________
headers_sheety = {
    "Authorization": "Basic bm1pbnVzb25lOmJydXR1czgy",
}
sheety_endpoint = "https://api.sheety.co/43e8fa189771102b974809bb262f3744/workoutTracking/workouts"
sheety_pull = requests.get(url=sheety_endpoint, headers=headers_sheety)
sheety_pull.raise_for_status()
workout_data = sheety_pull.json()
print(workout_data)
# _________________________________SHEETY API POST REQUESTS_______________________________________________
body = {
    "workout": {
        "date": today,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
        "id": 2

    }
}
sheety_push = requests.post(url=sheety_endpoint, headers=headers_sheety, json=body)
callback = sheety_push.json()
print(callback)

