#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to generate missing name variants for Vietnamese Name DB
- Generates unsigned (no diacritics) versions
- Extracts one-word names
"""

import re
import unicodedata


def remove_accents(text):
    """
    Remove Vietnamese diacritical marks from text
    """
    # Vietnamese character mapping
    vietnamese_map = {
        'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'ă': 'a', 'ằ': 'a', 'ắ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
        'â': 'a', 'ầ': 'a', 'ấ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
        'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ê': 'e', 'ề': 'e', 'ế': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
        'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ô': 'o', 'ồ': 'o', 'ố': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
        'ơ': 'o', 'ờ': 'o', 'ớ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
        'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'ư': 'u', 'ừ': 'u', 'ứ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
        'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
        'đ': 'd', 'Đ': 'D',
        'À': 'A', 'Á': 'A', 'Ả': 'A', 'Ã': 'A', 'Ạ': 'A',
        'Ă': 'A', 'Ằ': 'A', 'Ắ': 'A', 'Ẳ': 'A', 'Ẵ': 'A', 'Ặ': 'A',
        'Â': 'A', 'Ầ': 'A', 'Ấ': 'A', 'Ẩ': 'A', 'Ẫ': 'A', 'Ậ': 'A',
        'È': 'E', 'É': 'E', 'Ẻ': 'E', 'Ẽ': 'E', 'Ẹ': 'E',
        'Ê': 'E', 'Ề': 'E', 'Ế': 'E', 'Ể': 'E', 'Ễ': 'E', 'Ệ': 'E',
        'Ì': 'I', 'Í': 'I', 'Ỉ': 'I', 'Ĩ': 'I', 'Ị': 'I',
        'Ò': 'O', 'Ó': 'O', 'Ỏ': 'O', 'Õ': 'O', 'Ọ': 'O',
        'Ô': 'O', 'Ồ': 'O', 'Ố': 'O', 'Ổ': 'O', 'Ỗ': 'O', 'Ộ': 'O',
        'Ơ': 'O', 'Ờ': 'O', 'Ớ': 'O', 'Ở': 'O', 'Ỡ': 'O', 'Ợ': 'O',
        'Ù': 'U', 'Ú': 'U', 'Ủ': 'U', 'Ũ': 'U', 'Ụ': 'U',
        'Ư': 'U', 'Ừ': 'U', 'Ứ': 'U', 'Ử': 'U', 'Ữ': 'U', 'Ự': 'U',
        'Ỳ': 'Y', 'Ý': 'Y', 'Ỷ': 'Y', 'Ỹ': 'Y', 'Ỵ': 'Y',
        'Ð': 'D', 'ð': 'd'
    }

    result = []
    for char in text:
        if char in vietnamese_map:
            result.append(vietnamese_map[char])
        else:
            result.append(char)

    return ''.join(result)


def extract_one_word_names(input_file):
    """
    Extract single-word names from a name list
    """
    one_word_names = set()

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            name = line.strip()
            if name:
                # Split by space and take each word
                words = name.split()
                for word in words:
                    if len(word) > 0:
                        one_word_names.add(word)

    return sorted(one_word_names)


def generate_unsigned_file(input_file, output_file):
    """
    Generate unsigned version of a name file
    """
    print(f"Generating {output_file} from {input_file}...")

    with open(input_file, 'r', encoding='utf-8') as f_in:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                name = line.strip()
                if name:
                    unsigned_name = remove_accents(name)
                    f_out.write(unsigned_name + '\n')

    print(f"  ✓ Created {output_file}")


def generate_one_word_file(input_file, output_file):
    """
    Generate one-word names file
    """
    print(f"Generating {output_file} from {input_file}...")

    one_word_names = extract_one_word_names(input_file)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        for name in one_word_names:
            f_out.write(name + '\n')

    print(f"  ✓ Created {output_file} with {len(one_word_names)} names")


def main():
    print("Vietnamese Name DB - Update Database Script")
    print("=" * 50)
    print()

    # Generate boy_unsigned.txt
    generate_unsigned_file('boy.txt', 'boy_unsigned.txt')

    # Generate boy_one_word.txt
    generate_one_word_file('boy.txt', 'boy_one_word.txt')

    # Generate boy_one_word_unsigned.txt
    generate_unsigned_file('boy_one_word.txt', 'boy_one_word_unsigned.txt')

    print()
    print("✓ All missing boy name variants have been generated!")


if __name__ == '__main__':
    main()
