def find_coordinates(target):
    # اگر عدد مورد نظر 0 باشد
    if target == 0:
        return (0, 0)

    # تعیین مرزهای جست‌وجو
    layer = 0
    while True:
        # محاسبه حداکثر عدد در لایه
        max_num = (layer * 2 + 1) ** 2
        if max_num >= target:
            break
        layer += 1

    # محاسبه عرض و ارتفاع در این لایه
    side_length = layer * 2
    positions = []

    # جست‌وجو در هر سمت لایه
    for side in range(4):
        if side == 0:  # سمت بالا
            start = max_num - side_length
            end = max_num
            step = 1
            coord = (layer, start)
        elif side == 1:  # سمت راست
            start = max_num - side_length
            end = max_num
            step = 1
            coord = (start, -layer)
        elif side == 2:  # سمت پایین
            start = max_num - side_length
            end = max_num
            step = -1
            coord = (-layer, start)
        else:  # سمت چپ
            start = max_num - side_length
            end = max_num
            step = -1
            coord = (start, layer)

        # جست‌وجو در سمت مشخص
        for i in range(side_length + 1):
            if target == max_num - (side * side_length + i):
                return coord
            if side == 0:
                coord = (layer, coord[1] + step)
            elif side == 1:
                coord = (coord[0] + step, -layer)
            elif side == 2:
                coord = (-layer, coord[1] + step)
            else:
                coord = (coord[0] + step, layer)

    return None  # اگر عدد پیدا نشود

# ورودی کاربر
target = int(input("عدد مورد نظر را وارد کنید: "))
coordinates = find_coordinates(target)

if coordinates:
    print(f"مختصات عدد {target}: {coordinates}")
else:
    print("عدد در ماتریس وجود ندارد.")