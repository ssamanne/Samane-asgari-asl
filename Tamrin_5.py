import numpy as np


def find_closest_and_farthest(cities, distances, target_city):
    """محاسبه نزدیک‌ترین و دورترین شهر به یک شهر مشخص"""

    target_index = cities.index(target_city)

    closest_city = None
    farthest_city = None
    closest_distance = float('inf')
    farthest_distance = 0

    for i, city in enumerate(cities):
        if i == target_index:
            continue  # نادیده گرفتن خود شهر هدف

        distance = distances[target_index][i]

        if distance < closest_distance:
            closest_distance = distance
            closest_city = city

        if distance > farthest_distance:
            farthest_distance = distance
            farthest_city = city

    return closest_city, farthest_city


def main():
    """تابع اصلی برای دریافت ورودی و نمایش نتیجه"""
    cities = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]  # لیست شهرها
    distances = np.array([[0, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                          [10, 0, 35, 25, 30, 40, 50, 60, 70, 80],
                          [15, 35, 0, 15, 20, 30, 40, 50, 60, 70],
                          [20, 25, 15, 0, 10, 20, 30, 40, 50, 60],
                          [25, 30, 20, 10, 0, 15, 25, 35, 45, 55],
                          [30, 40, 30, 20, 15, 0, 10, 20, 30, 40],
                          [35, 50, 40, 30, 25, 10, 0, 10, 20, 30],
                          [40, 60, 50, 40, 35, 20, 10, 0, 10, 20],
                          [45, 70, 60, 50, 45, 30, 20, 10, 0, 10],
                          [50, 80, 70, 60, 55, 40, 30, 20, 10, 0]])  # ماتریس فاصله‌ها

    target_city = input("شهر مورد نظر را وارد کنید: ")

    if target_city not in cities:
        print("شهر مورد نظر در لیست شهرها وجود ندارد.")
        return

    closest_city, farthest_city = find_closest_and_farthest(cities, distances, target_city)

    print(f"نزدیک‌ترین شهر به {target_city}: {closest_city}")
    print(f"دورترین شهر از {target_city}: {farthest_city}")


# اجرای برنامه
if __name__ == "__main__":
    main()