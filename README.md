# Weather-Prediction-app

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

A machine learning-based weather prediction system that forecasts temperature and rain using historical and real-time data, deployed with Django.

---
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>
## 📌 Project Highlights

- 🔍 **Rain Prediction** using Random Forest Classifier  
- 🌡️ **Temperature Forecasting** using Random Forest Regressor  
- 🌐 **Real-time Weather Integration** via OpenWeatherMap API  
- 🖥️ **Deployed with Django** — full-stack ML app  
- 📊 Clean UI to input weather data and display predictions


## 🎯 Who It Helps

**- Farmers** – Plan agriculture activities and protect crops

**- Disaster Management** – Respond early to floods and storms

**- Transport Sector** – Improve safety and logistics

**- General Public** – Plan travel and routines

**- Smart Cities & Health Sector** – Manage resources and public safety
---
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>
## 🚀 Demo

<p align="left">
  <img src="https://github.com/user-attachments/assets/18337cfe-aa2e-4f1c-b726-6dc18dcd519f" width="500" alt="Weather Forecast UI">

  <img src="https://github.com/user-attachments/assets/c62ccb84-db02-4f79-b5d5-89091186616a" width="500" alt="Weather UI Screenshot">
</p>

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>
## 🧠 How It Works

1. **User Inputs**: Temperature, humidity, wind speed, etc.  
2. **Real-time data**: Optional — fetched from OpenWeatherMap API  
3. **Model Predictions**:
   - Rain tomorrow? → **Yes / No**
   - Estimated temperature → **Regression value**
4. **Output Displayed** via Django web page

---

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

## 𝖜𝖊𝖆𝖙𝖍𝖊𝖗 𝖕𝖗𝖊𝖉𝖎𝖈𝖙𝖎𝖔𝖓 𝖎𝖘 𝖓𝖔𝖙 𝖏𝖚𝖘𝖙 𝖆𝖇𝖔𝖚𝖙 𝖋𝖔𝖗𝖊𝖈𝖆𝖘𝖙𝖎𝖓𝖌 — 𝖎𝖙'𝖘 𝖆𝖇𝖔𝖚𝖙 𝖊𝖓𝖆𝖇𝖑𝖎𝖓𝖌 𝖇𝖊𝖙𝖙𝖊𝖗 𝖉𝖊𝖈𝖎𝖘𝖎𝖔𝖓𝖘 𝖆𝖈𝖗𝖔𝖘𝖘 𝖘𝖔𝖈𝖎𝖊𝖙𝖞.✍

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

## 📁 Project Structure

```bash
weatherProject/
│
├── forecast/                     # Main Django app
│   ├── migrations/
│   │   └── __init__.py
│   ├── static/                   # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   ├── templates/               # HTML templates
│   │   └── weather.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── weatherProject/              # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3                   # Default SQLite database
├── manage.py                    # Django command-line utility
├── weather.csv                  # Dataset used for model training

