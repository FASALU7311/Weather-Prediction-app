from django.shortcuts import render

# Create your views here
import os
import requests # This libraray help us to fetch data from API
import pandas as pd # For Handling And Analysing Data
import numpy as np # For Numerical Operation
from sklearn.model_selection import train_test_split # Split into train and tes
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier , RandomForestRegressor
from sklearn.metrics import mean_squared_error
from datetime import datetime , timedelta
import pytz


api_key = "46883bef6404119878ccc2be7b5fe646" # Replace with your actual api key
base_url = "https://api.openweathermap.org/data/2.5/" # Base URL Making API request

# 1 . Fetch Currect Weather Data

def get_current_weather (city):
  url = f"{base_url}weather?q={city}&appid={api_key}&units=metric" # Contruct The API Request URL
  response = requests.get(url) # Send The Get Request To API , This creates a request URL for the OpenWeatherMap API.
  data = response.json() # Parse The Response
  print(data)
  return {
      'city' : data['name'],
      'current_temp' : round(data['main']['temp']),
      'feels_like' : round(data['main']['feels_like']),
      'min_temp' : round(data['main']['temp_min']),
      'max_temp' : round(data['main']['temp_max']),
      'humidity' : round(data['main']['humidity']),
      'description' : data['weather'][0]['description'],
      'country' : data['sys']['country'],
      'wind_gust_dir' : data ['wind']['deg'],
      'pressure' : data['main']['pressure'],
      'Wind_Gust_Speed' : data['wind']['speed'],

      'clouds':data['clouds']['all'],

      'Visibility' : data['visibility'],
  }

# 2 . Read Histrorical Data

def read_historical_data(filename):
  df = pd.read_csv(filename) # Load CSV File Into Dataframe
  df = df.dropna() # Remove Rows With Missing Value
  df = df.drop_duplicates()
  return df

# 3 . Prepare Data For Training

def prepare_data(data):
  le = LabelEncoder() # Create A LabelEncoder Instance
  data['WindGustDir'] = le.fit_transform(data['WindGustDir'])
  data['RainTomorrow'] = le.fit_transform(data['RainTomorrow'])

  # Define Teh Feature Variable And Target Variable
  X = data.drop(columns=['RainTomorrow'])
  y = data['RainTomorrow']  # Target Variable

  return X , y , le # Return Feature  Variable , Target Variable And The Label Encoder

# 4 . Train Rain Prediction Model

def train_rain_model(X , y):
  X_train, X_test, y_train ,y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  model = RandomForestClassifier(n_estimators=100 , random_state =42)  # The number of decision trees in the forest
  model.fit(X_train , y_train) # Train The Model

  y_pred = model.predict(X_test) # To Make Prediction On Test Set

  print("Mean Squared Error For Rain Model")

  print(mean_squared_error(y_test , y_pred))

  return model

# 5 . Prepare Regression Data

def prepare_regression_data(data , Feature):
  X , y = [] , [] # Initialize List For Feature And Target Value

  for i in range(len(data) - 1):
    X.append(data[Feature].iloc[i])

    y.append(data[Feature].iloc[i + 1])

  X = np.array(X).reshape(-1 , 1)
  y = np.array(y)
  return X , y

# 6 . Train Regression Model

def train_regression_model(X , y):
  model = RandomForestRegressor(n_estimators =100 , random_state= 42 )
  model.fit(X , y)
  return model

# 7 . Predict Future

def predict_future(model , current_value) :
  predictions = [current_value]

  for i in range(5):
    next_value = model.predict(np.array([[predictions[-1]]]))

    predictions.append(next_value[0])

  return predictions[1:]
  
# 8 . Weather Analysis Function

def weather_view(request):
  if request.method == 'POST':
     city = request.POST.get('city')
     current_weather = get_current_weather(city)

#  # Load Historical Data
     csv_path = os.path.join('C:\\Users\\shmlp\\OneDrive\Desktop\\ML_Weather prediction_pro\\weather.csv')
     historical_data = read_historical_data("weather.csv")





# Prepare and Train The Rain Prediction Model

     X , y , le = prepare_data(historical_data)
     rain_model = train_rain_model(X , y)

# map wind Direction to Compass Points

     wind_deg = current_weather['wind_gust_dir'] % 360
     compass_points = [
       ("N",0,11.25) , ("NNE",11.25,33.75) , ("NE",33.75,56.25),
       ("ENE",56.25,78.75) , ("E",78.75,101.25) , ("ESE",101.25,123.75),
       ("SE",123.75,146.25) , ("SSE",146.25,168.75) , ("S",168.75,191.25),
       ("SSW",191.25,213.75) , ("SW",213.75,236.25) , ("WSW",236.25,258.75),
       ("W",258.75,281.25) , ("WNW",281.25,303.75) , ("NW",303.75,326.25),
       ("NNW",326.25,348.75)
    ]

     compass_direction = next(point for point , start , end in compass_points if start <= wind_deg < end)

     compass_direction_encoder = le.transform([compass_direction])[0] if compass_direction in le.classes_ else -1

     current_data = {
       "MinTemp" : current_weather['min_temp'],
       "MaxTemp" : current_weather['max_temp'],
       "WindGustDir" : compass_direction_encoder,
       "WindGustSpeed" : current_weather['Wind_Gust_Speed'],
       "Humidity" : current_weather['humidity'],
       "Pressure" : current_weather['pressure'],
       "Temp" : current_weather['current_temp']

  }

     current_df = pd.DataFrame([current_data])

  # Rain Prediction

     rain_prediction = rain_model.predict(current_df)[0]

  # Prepare Regresion Model For Tumprature And Humidity

     X_temp , y_temp = prepare_regression_data(historical_data , "Temp")

     X_hum , y_hum = prepare_regression_data(historical_data , "Humidity")

     temp_model = train_regression_model(X_temp , y_temp)

     hum_model = train_regression_model(X_hum , y_hum)

  # Predict Future Temprature And Humidity

     future_temp = predict_future(temp_model , current_weather['min_temp'])

     future_hum = predict_future(hum_model , current_weather['humidity'])

  # Prepare Time For Future Predictions

     timezone = pytz.timezone("Asia/Karachi")
     now = datetime.now(timezone)
     next_hour = now + timedelta(hours = 1)
     next_hour = next_hour.replace(minute = 0 , second = 0 , microsecond = 0)

     future_times = [(next_hour + timedelta(hours = i)).strftime("%H:00") for i in range (5)]

    # Store each value seperetaly

     time1 , time2 , time3 , time4 , time5 = future_times
     temp1 , temp2 , temp3 , temp4 , temp5 = future_temp
     hum1 , hum2 , hum3 , hum4 , hum5 = future_hum

    # Pass data to tempelate

     context = {
       'location' : city,
       'current_temp' : current_weather['current_temp'],
       'MinTemp' : current_weather['min_temp'],
       'MaxTemp' : current_weather['max_temp'],
       'feels_like' : current_weather['feels_like'],
       'humidity' : current_weather['humidity'],
       'clouds' : current_weather['clouds'],
       'description' : current_weather['description'],
       'city' : current_weather['city'],
       'country' : current_weather['country'],

       'time' : datetime.now(),
       'date' : datetime.now().strftime("%B %d ,%Y"),

       'wind' : current_weather['Wind_Gust_Speed'],
       'pressure' : current_weather['pressure'],
       'visibility' : current_weather['Visibility'],

       'time1' : time1,
       'time2' : time2,
       'time3' : time3,
       'time4' : time4,
       'time5' : time5,

       'temp1' : f"{round(temp1 , 1)}",
       'temp2' : f"{round(temp2 , 1)}",
       'temp3' : f"{round(temp3 , 1)}",
       'temp4' : f"{round(temp4 , 1)}",
       'temp5' : f"{round(temp5 , 1)}",

       'hum1' : f"{round(hum1 , 1)}",
       'hum2' : f"{round(hum2 , 1)}",
       'hum3' : f"{round(hum3 , 1)}",
       'hum4' : f"{round(hum4 , 1)}",
       'hum5' : f"{round(hum5 , 1)}",
       
    }
     
     return render(request , 'weather.html' , context)
  
  return render(request , 'weather.html')