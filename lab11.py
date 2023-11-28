import csv

def find_min_max_and_write(file_path, target_column_names):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            # перевіряємо, чи існують потрібні колонки
            for target_column_name in target_column_names:
                if target_column_name not in data[0]:
                    raise ValueError(f"Колонка з ім'ям '{target_column_name}' не знайдена у файлі.")

            min_value = float('inf')  # початкове значення для пошуку мінімуму
            max_value = float('-inf')  # початкове значення для пошуку максимуму

            for row in data:
                try:
                    # спробуємо отримати значення з рядка для кожної колонки
                    for target_column_name in target_column_names:
                        value = float(row[target_column_name])
                        min_value = min(min_value, value)
                        max_value = max(max_value, value)
                except (ValueError, KeyError):
                    # ігноруємо рядки, де не вдається отримати значення або відсутня потрібна колонка
                    pass

            # записуємо результат в новий файл
            with open('result.csv', 'w', newline='') as result_file:
                writer = csv.writer(result_file)
                writer.writerow(["Min Value", "Max Value"])
                writer.writerow([min_value, max_value])

    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

# приклад виклику функції
csv_file_path = 'Data.csv'
target_column_names = [
    '1991 [YR1991]', '1992 [YR1992]', '1993 [YR1993]', '1994 [YR1994]', '1995 [YR1995]',
    '1996 [YR1996]', '1997 [YR1997]', '1998 [YR1998]', '1999 [YR1999]', '2000 [YR2000]',
    '2001 [YR2001]', '2002 [YR2002]', '2003 [YR2003]', '2004 [YR2004]', '2005 [YR2005]',
    '2006 [YR2006]', '2007 [YR2007]', '2008 [YR2008]', '2009 [YR2009]', '2010 [YR2010]',
    '2011 [YR2011]', '2012 [YR2012]', '2013 [YR2013]', '2014 [YR2014]', '2015 [YR2015]',
    '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]', '2019 [YR2019]'
]
find_min_max_and_write(csv_file_path, target_column_names)
