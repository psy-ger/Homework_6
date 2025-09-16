def filter_lines_with_keyword(filepath, keyword):
    """
    Генератор, який читає файл рядок за рядком і повертає лише ті, що містять ключове слово.
    Args:
        filepath (str): Шлях до текстового файлу.
        keyword (str): Ключове слово для пошуку.
    Yields:
        str: Рядок, що містить ключове слово.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                yield line

def save_filtered_lines(input_path, output_path, keyword):
    """
    Записує у новий файл лише ті рядки, що містять ключове слово.
    Args:
        input_path (str): Вхідний файл.
        output_path (str): Вихідний файл.
        keyword (str): Ключове слово для пошуку.
    """
    with open(output_path, 'w', encoding='utf-8') as out_file:
        for line in filter_lines_with_keyword(input_path, keyword):
            out_file.write(line)

def main():
    """
    Демонструє фільтрацію великого файлу за ключовим словом.
    """
    input_path = "bigfile.txt"  # Змініть на свій файл
    output_path = "filtered.txt"
    keyword = "ERROR"  # Змініть на потрібне слово
    save_filtered_lines(input_path, output_path, keyword)
    print(f"Рядки з '{keyword}' збережено у {output_path}")

if __name__ == "__main__":
    main()
