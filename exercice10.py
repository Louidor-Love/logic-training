from datetime import datetime

hoy1 = datetime.now()
hoy = hoy1.strftime("%Y-%m-%d")
tomorrow = hoy1.strftime("%H:%M:%S")
print(f"hoy es {hoy} y la hora exacta es: {tomorrow}")