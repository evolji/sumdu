import pandas as pd
data_dict = {}

while True:
    key = input("Введіть ключ (натисніть Enter, щоб завершити): ")
    if not key:
        break

    value = input("Введіть значення: ")
    data_dict[key] = value

if len(data_dict) % 2 != 0:
    additional_data = {"Додатковий ключ": "Додаткове значення"}
    data_dict.update(additional_data)

df = pd.DataFrame(list(data_dict.items()), columns=["Ключ", "Значення"])

print("Отриманий датафрейм:")
print(df)

aggregated_data = df.groupby("Ключ").agg({"Значення": "count"}).reset_index()

print("\nРезультат агрегації та групування:")
print(aggregated_data)






import pandas as pd
import matplotlib.pyplot as plt

file_path = 'comptagevelo20162.csv'
data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y', errors='coerce')
data['Month'] = data['Date'].dt.month

monthly_data = data.groupby('Month')['Berri1'].sum()
most_popular_month = monthly_data.idxmax()
print(f"The most popular month for cyclists is {most_popular_month}")

plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data, marker='o')
plt.title('Monthly Bicycle Usage')
plt.xlabel('Month')
plt.ylabel('Number of Cyclists')
plt.grid(True)
plt.show()
