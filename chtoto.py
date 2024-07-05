import re
import csv

# Функция для преобразования координат из градусов, минут и секунд в десятичный формат
def dms_to_decimal(degrees, minutes, seconds):
    return float(degrees) + float(minutes)/60 + float(seconds)/(60*60)

# Открываем файл с текстом
input_file = 'input.txt'

# Открываем файл для записи таблицы CSV
output_file = 'coordinates_table.csv'

# Паттерн для поиска координат в формате градусов, минут и секунд
pattern = r'(\d+)°(\d+)\'(\d+\.\d+)"([NSnsEWew])'

# Список для хранения извлеченных координат
coordinates = []

# Читаем файл и извлекаем координаты
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()
    matches = re.findall(pattern, text)
    
    for match in matches:
        degrees = match[0]
        minutes = match[1]
        seconds = match[2]
        direction = match[3].upper()
        
        # Преобразуем координаты в десятичный формат
        decimal_value = dms_to_decimal(degrees, minutes, seconds)
        
        # Формируем строку для записи в таблицу
        if direction in ['N', 'S']:
            latitude = f"{degrees}°{minutes}'{seconds}\" {direction}"
        elif direction in ['E', 'W']:
            longitude = f"{degrees}°{minutes}'{seconds}\" {direction}"
        
        # Добавляем координаты в список
        coordinates.append((latitude, longitude))

# Записываем координаты в таблицу CSV
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Точка', 'Широта (с.ш.)', 'Долгота (в.д.)'])
    for i, coord in enumerate(coordinates, start=1):
        csvwriter.writerow([i, coord[0], coord[1]])

print(f"Координаты успешно записаны в файл: {output_file}")
