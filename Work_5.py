def analyze_weather_data(weather_data):
  total_temp = 0
  max_temp_date = None
  max_temp = float('-inf')
  rainy_days = 0
  for date, temp, precipitation in weather_data:
    total_temp += temp
    if temp > max_temp:
      max_temp = temp
      max_temp_date = date
    if precipitation:
      rainy_days += 1
  average_temp = total_temp / len(weather_data)
  print(f"Средняя температура: {average_temp:.1f}")
  print(f"Дата с самой высокой температурой: {max_temp_date}")
  print(f"Количество дней с осадками: {rainy_days}")
test_data = [
  ("2023-11-01", 20, False),
  ("2023-11-02", 25, True),
  ("2023-11-03", 18, False),
  ("2023-11-04", 22, True),
]
analyze_weather_data(test_data)
