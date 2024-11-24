def sort_characters(input_string):
    """این تابع یک رشته را مرتب می‌کند و خروجی مرتب شده را برمی‌گرداند."""
    # تبدیل رشته به لیست حروف
    char_list = list(input_string)

    # مرتب‌سازی لیست حروف
    sorted_list = sorted(char_list)

    # بازگرداندن رشته مرتب شده
    return ''.join(sorted_list)


def main():
    """تابع اصلی که ورودی را از کاربر می‌گیرد و خروجی را نمایش می‌دهد."""
    # گرفتن ورودی از کاربر
    input_string = input("در یک خط رشته‌ای را وارد کنید: ")

    # مرتب کردن حروف و دریافت نتیجه
    sorted_string = sort_characters(input_string)

    # چاپ رشته مرتب شده
    print("رشته مرتب شده:", sorted_string)


# اجرای برنامه
if __name__ == "__main__":
    main()