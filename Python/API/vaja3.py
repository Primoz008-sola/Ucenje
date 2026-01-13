import requests

koordinate = [
    {"ime": "Ljubljana", "lat": 46.05, "lon": 14.51},
    {"ime": "London", "lat": 51.51, "lon": -0.13},
    {"ime": "New York", "lat": 40.71, "lon": -74.01},
    {"ime": "Tokyo", "lat": 35.68, "lon": 139.69},
    {"ime": "Sydney", "lat": -33.87, "lon": 151.21},
    {"ime": "Kairo", "lat": 30.04, "lon": 31.24},
    {"ime": "São Paulo", "lat": -23.55, "lon": -46.63},
    {"ime": "Mumbai", "lat": 19.08, "lon": 72.88}
]

# 1: Poišči mesto z najvišjo maksimalno temperaturo v naslednjih 7 dneh
# Namig: Uporabi max() na ["daily"]["temperature_2m_max"]

# 2: Katero mesto bo imelo največ padavin skupaj v naslednjih 7 dneh?
# Namig: Seštej vse vrednosti v ["daily"]["precipitation_sum"]

# 3: Najdi najhladneje mesto v naslednjih 7 dneh
# Namig: Nekatera mesta lahko nimajo podatkov, preveri dolžino seznama!

# 4: Poišči mesto z največjim temperaturnim razponom (max - min) za prvi dan
# Namig: Uporabi indeks [0] za prvi dan napovedi

# 5: Izpiši vsa mesta, kjer bo jutri padalo (precipitation_sum[1] > 0)
# Namig: Jutri je na indeksu [1], danes je [0]

# 6: Koliko mest bo imelo jutri maksimalno temperaturo nad 20°C?
# Namig: Preštej mesta, kjer je temperature_2m_max[1] > 20

# 7: Katero mesto ima najhitrejši veter v naslednjih 7 dneh? Izpiši tudi hitrost vetra.
# Namig: Preveri max() vrednost v ["daily"]["wind_speed_10m_max"]

# 8: V katerem mestu je najdaljši dan (razlika med zahodom in vzhodom sonca)?
# Namig: Uporabi DateTime https://www.w3schools.com/python/python_datetime.asp

# 9: Ugotovi, koliko mest bo  v naslednjih 7 dneh brez padavin
# Namig: Preveri, če ima mesto vsaj eno ničlo v precipitation_sum

# 10: Poljubna naloga!