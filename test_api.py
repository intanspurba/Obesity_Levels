import requests

data = {
    "Gender": "Female",
    "Age": 21,
    "Height": 1.62,
    "Weight": 110,
    "CALC": "no",
    "FAVC": "no",
    "FCVC": 2,
    "NCP": 3,
    "SCC": "no",
    "SMOKE": "no",
    "CH2O": 2,
    "family_history_with_overweight": "yes",
    "FAF": 0,
    "TUE": 1,
    "CAEC": "Sometimes",
    "MTRANS": "Public_Transportation"
}

respon = requests.post('http://127.0.0.1:5000/predict', json=data)
print(respon.json())