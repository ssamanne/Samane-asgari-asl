def slope(x1, y1, x2, y2):
    """محاسبه شیب بین دو نقطه"""
    return (y2 - y1) / (x2 - x1)

def line_equation(x1, y1, x2, y2):
    """محاسبه معادله خط"""
    m = slope(x1, y1, x2, y2)  # محاسبه شیب
    b = y1 - m * x1  # محاسبه مقدار b در معادله y = mx + b
    return m, b

def main():
    """تابع اصلی برای دریافت ورودی و نمایش نتیجه"""
    x1 = float(input("نقطه اول را وارد کنید (x1): "))
    y1 = float(input("نقطه اول را وارد کنید (y1): "))
    x2 = float(input("نقطه دوم را وارد کنید (x2): "))
    y2 = float(input("نقطه دوم را وارد کنید (y2): "))

    # محاسبه معادله خط
    m, b = line_equation(x1, y1, x2, y2)

    # نمایش نتیجه
    print(f"معادله خط: Y = {m}X + {b}")

# اجرای برنامه
if __name__ == "__main__":
    main()