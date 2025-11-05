# Vietnamese Name Database

A comprehensive, open-source database of Vietnamese personal names (given names) compiled from multiple sources across the Internet. This dataset provides 6,284+ names categorized by gender, with multiple format variants to support various applications including text processing, natural language processing, form validation, and cultural research.

## Overview

Vietnamese personal names consist of three main components: Family Name (Họ) + Middle Name (Tên Đệm) + Given Name (Tên Chính). The given name is carefully selected based on phonetic harmony, semantic meaning, gender, family tradition, regional customs, and parental aspirations.

A distinctive characteristic of Vietnamese naming culture, compared to Chinese, Korean, and Japanese traditions, is that individuals are addressed by their given name rather than their family name.

## Dataset Structure

### Boy Names (Tên Nam)
| File | Description | Count |
|------|-------------|-------|
| [boy.txt](boy.txt) | Vietnamese given names with diacritics | 1,236 names |
| [boy_no_accents.txt](boy_no_accents.txt) | Names without diacritical marks | 1,236 names |
| [boy_one_word.txt](boy_one_word.txt) | Single-word name components | 334 words |
| [boy_one_word_no_accents.txt](boy_one_word_no_accents.txt) | Single-word components without diacritics | 334 words |

### Girl Names (Tên Nữ)
| File | Description | Count |
|------|-------------|-------|
| [girl.txt](girl.txt) | Vietnamese given names with diacritics | 1,316 names |
| [girl_no_accents.txt](girl_no_accents.txt) | Names without diacritical marks | 1,316 names |
| [girl_one_word.txt](girl_one_word.txt) | Single-word name components | 256 words |
| [girl_one_word_no_accents.txt](girl_one_word_no_accents.txt) | Single-word components without diacritics | 256 words |

### Full Names
| File | Description |
|------|-------------|
| [uit_member.json](uit_member.json) | Complete names (family + middle + given) crawled from forum.uit.edu.vn (December 2016) |

**Total:** 6,284 names (updated 2025)

## Use Cases

- **Name Validation**: Validate Vietnamese names in registration forms and user input
- **Text Processing**: Identify and extract Vietnamese personal names from text
- **NLP & Machine Learning**: Training data for name recognition and classification models
- **Data Normalization**: Convert between accented and non-accented name formats
- **Cultural Research**: Study Vietnamese naming patterns and trends
- **Application Development**: Autocomplete, name suggestions, demographic analysis

## File Formats

- **Text files (.txt)**: One name per line, UTF-8 encoded
- **JSON file (.json)**: Structured data with full name information

## Maintenance Scripts

Three Python utilities are included for database maintenance:

- **`update_database.py`**: Generate name variants (no_accents, one_word) for boy names
- **`regenerate_all.py`**: Comprehensive regeneration of all name variants for both genders

## Usage Example

```python
# Load names with diacritics
with open('girl.txt', 'r', encoding='utf-8') as f:
    names = [line.strip() for line in f]

# Load names without diacritics for case-insensitive matching
with open('girl_no_accents.txt', 'r', encoding='utf-8') as f:
    names_normalized = [line.strip() for line in f]
```

```bash
# Count unique single-word name components
wc -l boy_one_word.txt girl_one_word.txt

# Search for specific name patterns
grep "Minh" boy.txt
```

## Contributing

Contributions are welcome to expand and improve this database:

1. **Fork** this repository
2. **Create** a feature branch (`git checkout -b feature/add-names`)
3. **Add** new names or improvements with proper documentation
4. **Test** your changes using the provided Python scripts
5. **Submit** a pull request with a clear description of changes

Please ensure:
- Names are properly formatted (one per line, UTF-8 encoding)
- Diacritical marks are correctly applied
- Changes are tested with regeneration scripts
- Documentation is updated accordingly

## Data Sources

This database aggregates Vietnamese names from various public Internet sources, including forums, social networks, government databases, and cultural references. The dataset is continuously updated to reflect modern naming trends while preserving traditional names.

## License

MIT License

Copyright (c) 2016-2025 Van-Duyet Le

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
