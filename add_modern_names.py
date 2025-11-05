#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add modern and popular Vietnamese names to the database
"""


def read_names(filename):
    """Read names from file into a set"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()


def add_names_to_file(filename, new_names):
    """Add new names to file if they don't exist"""
    existing_names = read_names(filename)
    names_to_add = []

    for name in new_names:
        if name not in existing_names:
            names_to_add.append(name)

    if names_to_add:
        with open(filename, 'a', encoding='utf-8') as f:
            for name in sorted(names_to_add):
                f.write(name + '\n')

        print(f"  ✓ Added {len(names_to_add)} new names to {filename}")
        return len(names_to_add)
    else:
        print(f"  • No new names to add to {filename}")
        return 0


def main():
    print("Vietnamese Name DB - Add Modern Names")
    print("=" * 50)
    print()

    # Modern boy names
    modern_boy_names = [
        'Minh Khang',
        'Gia Bảo',
        'Hoàng Long',
        'Minh Đức',
        'Quốc Huy',
        'Trường An',
        'Thành Đạt',
        'Duy Khang',
        'Nhật Minh',
        'Tuấn Kiệt',
        'Hải Đăng',
        'Đức Anh',
        'Trí Dũng',
        'Quang Huy',
        'Việt Hoàng',
        'Bảo Long',
        'Gia Hưng',
        'Minh Quân',
        'Đăng Khoa',
        'Hoàng Anh',
        'Tuấn Anh',
        'Ngọc Sơn',
        'Thanh Tùng',
        'Văn Minh',
        'Hữu Nghĩa',
        'Quốc Bảo',
        'Tiến Dũng',
        'Đình Trọng',
        'Văn Toàn',
        'Công Phượng',
        'Xuân Trường',
        'Quang Hải',
        'Văn Hậu',
        'Duy Mạnh',
        'Văn Lâm',
    ]

    # Modern girl names
    modern_girl_names = [
        'Minh Anh',
        'Phương Anh',
        'Lan Anh',
        'Huyền Trang',
        'Thu Trang',
        'Khánh Linh',
        'Minh Thư',
        'Hà My',
        'Gia Hân',
        'Quỳnh Anh',
        'Bảo Trân',
        'Ngọc Hân',
        'Minh Châu',
        'Thảo Nguyên',
        'Tú Anh',
        'Thanh Hà',
        'Thu Hà',
        'Hương Giang',
        'Thu Hiền',
        'Thùy Linh',
        'Phương Thảo',
        'Ngọc Ánh',
        'Thanh Mai',
        'Hồng Nhung',
        'Mỹ Linh',
        'Thanh Lam',
        'Hồng Hạnh',
        'Trà My',
        'Phương Linh',
        'Diễm My',
        'Cẩm Ly',
        'Uyên Linh',
        'Kim Thành',
        'Hoàng Thùy',
        'Thúy Vi',
    ]

    print("Adding modern boy names...")
    boy_count = add_names_to_file('boy.txt', modern_boy_names)

    print("\nAdding modern girl names...")
    girl_count = add_names_to_file('girl.txt', modern_girl_names)

    print()
    print("=" * 50)
    print(f"✓ Added {boy_count + girl_count} new names total!")
    print(f"  - Boy names: {boy_count}")
    print(f"  - Girl names: {girl_count}")


if __name__ == '__main__':
    main()
