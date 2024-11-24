# تعریف وزن‌های نمرات
weights = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

# دریافت تعداد امتحانات
n = int(input("تعداد امتحانات را وارد کنید: "))

# لیستی برای ذخیره نمرات
grades = []

# دریافت نمرات و اضافه کردن به لیست
for _ in range(n):
    grade = input("نمره را وارد کنید (A, B, C, D, E, F): ").strip().upper()
    if grade in weights:  # بررسی اینکه نمره معتبر است
        grades.append(grade)
    else:
        print("نمره نامعتبر است، لطفاً دوباره امتحان کنید.")

# محاسبه میانگین وزنی
weighted_sum = sum(weights[grade] for grade in grades)
average_weighted = weighted_sum / len(grades) if grades else 0

# تعیین کاراکتر 2
#میانگین
for char, weight in sorted(weights.items(), key=lambda x: x[1], reverse=True):
    if average_weighted >= weight:
        print(f"میانگین نمرات شما: {average_weighted:.2f} و کاراکتر آن: {char}")
        break