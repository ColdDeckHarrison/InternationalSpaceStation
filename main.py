import requests
from datetime import datetime
import time
import smtplib

MY_EMAIL = "pythonautomail87@gmail.com"
MY_PASSWORD = "your password"
MY_LAT = 39.744431
MY_LONG = -75.545097
API_KEY = "59f738e99ed76824d06e73edc8216016"


def overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    check = response.json()

    iss_latitude = float(check["iss_position"]["latitude"])
    iss_longitude = float(check["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


def is_cloudy():
    parameter = {
        "access_key": API_KEY,
        "query": "Philadelphia",
        "units": "f",
    }

    responses = requests.get(url="http://api.weatherstack.com/current", params=parameter)
    responses.raise_for_status()
    clouds = responses.json()
    percentage = clouds["current"]["cloudcover"]

    if percentage <= 40:
        return True

while True:
    time.sleep(60)
    if overhead() and night() and is_cloudy():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )