import requests

data = {
    "UTC": 1654733331,
    "Temperature_C":20.00 ,
    "Humidity_percent": 57.86,
    "TVOC_ppb": 0,
    "eCO2_ppm": 400,
    "Raw H2": 12306,
    "Raw Ethanol": 18520,
    "Pressure_hPa": 939.575,
    "PM1.0": 0,
    "PM2.5": 0,
    "NC0.5": 0,
    "NC1.0": 0,
    "NC2.5": 0,
    "CNT": 0
}

response = requests.post("http://127.0.0.1:5000/predict", json=data )

print(response.text)