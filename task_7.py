def error_lines_from_log(filepath):
    """
    Генерує рядки з лог-файлу, які містять коди 4XX або 5XX.
    Args:
        filepath (str): Шлях до лог-файлу.
    Yields:
        str: Рядок з помилкою.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if any(line.split()[8].startswith(str(code)) for code in range(4, 6)):
                yield line


def save_errors(input_path, output_path):
    """
    Записує всі рядки з помилками у новий файл.
    Args:
        input_path (str): Вхідний лог-файл.
        output_path (str): Вихідний файл для помилок.
    """
    with open(output_path, 'w', encoding='utf-8') as out_file:
        for line in error_lines_from_log(input_path):
            out_file.write(line)


def main():
    """
    Демонструє парсинг лог-файлу для аналітики помилок.
    """
    input_path = "access.log"  # Змініть на свій лог-файл
    output_path = "errors.log"
    save_errors(input_path, output_path)
    print(f"Помилки збережено у {output_path}")


if __name__ == "__main__":
    main()
