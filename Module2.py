# pip install -r requirements.txt
def greet(name):
    print(f"Hello {name}, Good Morning!")
    pass


greet("Harshit")


def add_numbers(a, b):
    return a + b, a - b


result = add_numbers(10, 20)
print(f"Sum: {result[0]}, Difference: {result[1]}")

import math

print(f"Square root of 16 is {math.sqrt(16)}")

from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

import requests

latitude = 48.85  # Paris latitude
longitude = 2.35  # Paris longitude

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()

print(data)
print(f"Current temperature in Paris: {data['current']['temperature_2m']}°C")
