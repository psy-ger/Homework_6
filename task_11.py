def incremental_average(filepath):
    """
    Генерує середнє значення після кожного нового числа з файлу.
    Args:
        filepath (str): Шлях до файлу з числами (по одному на рядок).
    Yields:
        float: Поточне середнє значення.
    """
    total = 0
    count = 0
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                num = float(line.strip())
                total += num
                count += 1
                yield total / count
            except ValueError:
                continue

def main():
    """
    Демонструє інкрементне обчислення середнього значення.
    """
    filepath = "numbers.txt"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("1\n2\n3\n4\n5\n")
    for avg in incremental_average(filepath):
        print(f"Поточне середнє: {avg}")

if __name__ == "__main__":
    main()
