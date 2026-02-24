import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "89287fa038cbafcacd7e0bef620514f9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "imperial" 
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            raise ValueError(data.get("message", "City not found"))

        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()
        return temperature, description

    except Exception as e:
        messagebox.showerror("Error", f"Could not get weather data:\n{e}")
        return None, None

def give_advice():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Needed", "Please enter a city name.")
        return

    temperature, description = get_weather(city)
    if temperature is None:
        return
    
    advice_window = tk.Toplevel(root)
    advice_window.title(f"Weather in {city}")
    advice_window.geometry("400x300")

    
    if temperature <= 32:
        advice = (
            f"❄️ It's freezing in {city}! ({temperature:.1f}°F, {description})\n\n"
            "👕 Clothing: Heavy coat, gloves, hat, and boots.\n"
            "🎯 Activities: Hot chocolate, reading, or indoor relaxation."
            
        )
        advice_window.configure(bg="#96d1d5")
        
    elif 33 <= temperature <= 50:
        advice = (
            f"🧥 It's cold in {city}. ({temperature:.1f}°F, {description})\n\n"
            "👕 Clothing: Warm jacket, scarf, and gloves.\n"
            "🎯 Activities: Visit a café or bake something cozy."
        )
        advice_window.configure(bg="#93c3df")
        
    elif 51 <= temperature <= 65:
        advice = (
            f"🌤️ It's cool and comfortable in {city}. ({temperature:.1f}°F, {description})\n\n"
            "👕 Clothing: Light jacket or sweater.\n"
            "🎯 Activities: Go hiking, biking, or take a walk."
        )
        advice_window.configure(bg="#7bbbf3")
        
    elif 66 <= temperature <= 80:
        advice = (
            f"☀️ It's warm in {city}. ({temperature:.1f}°F, {description})\n\n"
            "👕 Clothing: T-shirts, shorts, sunglasses.\n"
            "🎯 Activities: Picnic, outdoor games, or beach time."
        )
        advice_window.configure(bg="#ffe680")
        
    elif 81 <= temperature <= 95:
        advice = (
            f"🌞 It's hot in {city}! ({temperature:.1f}°F, {description})\n\n"
            "👕 Clothing: Light, breathable clothes.\n"
            "🎯 Activities: Swimming, stay hydrated, or rest indoors."
        )
        advice_window.configure(bg="#fbff80")
        
    else:
        advice = (
            f"🔥 It's extremely hot in {city}! ({temperature:.1f}°F, {description})\n\n"
            "👕 Clothing: Very light clothes.\n"
            "🎯 Activities: Stay indoors, use AC, and drink lots of water."
        )
        advice_window.configure(bg="#ffb3b3")
        
        
    bckg = advice_window.cget("bg")
    forg = "#001445" if temperature <= 66 else "#46010C"
    
    tk.Label(advice_window, text=f"Weather in {city}", font=("serif", 16, "bold"),fg=forg, bg=bckg).pack(pady=10)
    tk.Label(advice_window, text=advice, wraplength=350, justify="left", bg=bckg, fg=forg, font=("Serif", 12)).pack(padx=10, pady=10)

    tk.Button(advice_window, text="Close", command=advice_window.destroy, bg="#741C16", fg="white", font=("Arial", 12, "bold")).pack(pady=10)


root = tk.Tk()
root.title("🌡️ Weather & Clothing Advice App")
root.geometry("420x280")
root.resizable(False, False)
root.configure(bg="#d0e3f7")

title_label = tk.Label(root, text="Weather & Clothing Advice", font=("Times", 16, "bold"),bg="#d0e3f7")
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter a city name:", font=("Times", 12),bg="#d0e3f7")
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=("Times", 12), justify="center")
city_entry.pack(pady=5)

submit_btn = tk.Button(root, text="Get Weather & Advice", font=("Arial", 12, "bold"), bg="#106013", fg="white", command=give_advice)
submit_btn.pack(pady=10)

note_label = tk.Label(root, text="Uses OpenWeatherMap data", font=("Arial", 9), fg="gray", bg="#d0e3f7")
note_label.pack(side="bottom", pady=5)

root.mainloop()
