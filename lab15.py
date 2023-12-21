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
