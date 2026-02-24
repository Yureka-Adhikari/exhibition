import tkinter as tk
import requests
from tkinter import messagebox

API_ID = "89287fa038cbafcacd7e0bef620514f9"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    complete_url = f"{BASE_URL}appid={API_ID}&q={city_name}&units=imperial"
    response = requests.get(complete_url)
    data = response.json()
    
    main = data["main"]
    weather = data["weather"][0]
        
    temperature = main["temp"]
    humidity = main["humidity"]
    description = weather["description"].capitalize()
    
    frame= tk.Toplevel(root)
    
    result = tk.Frame(frame)
    frame.title(f"Weather in {city_name}")

    result.pack(pady=20, padx=20)
    
    if temperature > 90:
        advice = [f"Temperature : {temperature}°F\nHumidity : {humidity}%\nDescription : {description}\n\n"
                  "☀️ It is quite hot and dangerous"
                  "👕 Wear T-shirts, tanktops and clothes made of breathable material like cotton.\n"
                  "🧢 Use a hat or cap to protect yourself from the sun though it is suggested not to go out.\n"
                  "🏖️ Avoid outdoor activities to prevent heat strokes and dehydration.\n"]
        label = tk.Label(result, text=f"Weather in {city_name}", font=("Helvetica", 16, "bold"), fg="#450404", bg="#EA8886")
        label.pack(pady=10)
        tk.Label(result, text=advice, fg="#450404", bg="#EA8886", font=("Helvetica", 12), wraplength=380, justify="left").pack(pady=10)
        
        frame.configure(bg="#6e0808")
        result.configure(bg="#EA8886", padx=40, pady=40, border=50, borderwidth=5)
        
    elif 89 < temperature > 80:
        advice = [f"Temperature : {temperature}°F\nHumidity : {humidity}%\nDescription : {description}\n\n"
                "☀️ It is quite hot and humid."
                  "👕 Wear T-shirts, tanktops and clothes made of breathable material like cotton.\n"
                  "🧢 Use a hat or cap to protect yourself from the sun.\n"
                  "🏖️ Feel free to go out into the sun, enjoy outdoor activities like swimming and picnics.\n"]
        
        label = tk.Label(result, text=f"Weather in {city_name}", font=("Helvetica", 16, "bold"), fg="#534000", bg="#FFF5BA")
        label.pack(pady=10)
        
        tk.Label(result, text=advice, fg="#7D5500", bg="#FFCE9A", font=("Helvetica", 12), wraplength=380, justify="left").pack(pady=10)
        
        frame.configure(bg="#B8860B")
        result.configure(bg="#FFCE9A",padx=40, pady=40)
        
    elif 79 < temperature > 60:
        advice = [f"Temperature : {temperature}°F\nHumidity : {humidity}%\nDescription : {description}\n\n"
            "🌤️ The weather is moderate.\n"
                  "👕 Light clothing is recommended.\n"
                  "🧢 A hat or cap is optional.\n"
                  "🏞️ Enjoy outdoor activities like hiking, biking, and walking.\n"]
        
        label = tk.Label(result, text=f"Weather in {city_name}", font=("Helvetica", 16, "bold"), fg="#534000", bg="#FFF5BA")
        label.pack(pady=10)
        
        tk.Label(result, text=advice, fg="#534000", bg="#FFF5BA", font=("Helvetica", 12), wraplength=380, justify="left").pack(pady=10)
        
        frame.configure(bg="#DFBA7C")
        result.configure(bg="#FFF5BA",padx=40, pady=40)
    
    elif 59 < temperature > 40:
        advice = [f"Temperature : {temperature}°F\nHumidity : {humidity}%\nDescription : {description}\n\n"
            "🌥️ It is getting chilly.\n"
                  "🧥 Wear layers, including a light jacket or sweater.\n"
                  "🧢 A hat or cap is recommended to keep warm.\n"
                  "🍂 Enjoy outdoor activities like walking and jogging.\n"]
        
        label = tk.Label(result, text=f"Weather in {city_name}", font=("Helvetica", 16, "bold"), fg="#002F4B", bg="#A0C4FF")
        label.pack(pady=10)
                
        tk.Label(result, text=advice, fg="#002F4B", bg="#A0C4FF", font=("Helvetica", 12), wraplength=380, justify="left").pack(pady=10)

        frame.configure(bg="#001173")
        result.configure(bg="#A0C4FF", padx=40, pady=40)
        
    else:
        advice = [f"Temperature : {temperature}°F\nHumidity : {humidity}%\nDescription : {description}\n\n"
            "❄️ It is quite cold.\n"
                  "🧥 Wear warm clothing, including a heavy coat, scarf, gloves, and hat.\n"
                  "🧢 A warm hat is essential to prevent heat loss.\n"
                  "⛷️ Enjoy winter activities like skiing, snowboarding, and ice skating.\n"]
        
        result.configure(bg="#A6DEE7", padx=40, pady=40)
        label = tk.Label(result, text=f"Weather in {city_name}", font=("Helvetica", 16, "bold"), fg="#073969", bg="#A6DEE7")
        label.pack(pady=10)
        tk.Label(result, text=advice, fg="#073969", bg="#A6DEE7", font=("Helvetica", 12), wraplength=380, justify="left").pack(pady=10)

        frame.configure(bg="#094659")
        result.configure(bg="#A6DEE7", padx=40, pady=40)
        

root = tk.Tk()
root.title("Weather Advisory App")
root.configure(bg="#e6dcad", pady=50)
root.geometry("500x300")
tk.Label(root, text="Enter City Name:", font=("Segoe UI Variable Display", 14,"bold","italic"),fg="#00014e", bg="#e6dcad").pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather Advice", font=("Helvetica", 14), fg="#E4FFE7",bg="#537255", command=get_weather)
get_weather_button.pack(pady=20)
root.mainloop()
