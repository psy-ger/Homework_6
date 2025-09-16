import os
import csv
from PIL import Image

class ImageStatsIterator:
    """
    Ітератор для обходу зображень у каталозі та збору їх метаданих.
    """
    def __init__(self, directory):
        """
        Ініціалізує ітератор для заданого каталогу.
        Args:
            directory (str): Шлях до каталогу з зображеннями.
        """
        self.directory = directory
        self.files = [f for f in os.listdir(self.directory) if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif", ".jfif"))]
        self.index = 0

    def __iter__(self):
        """
        Повертає ітератор (самого себе).
        Returns:
            ImageStatsIterator: Ітератор.
        """
        return self

    def __next__(self):
        """
        Повертає метадані наступного зображення у каталозі.
        Returns:
            dict: Метадані зображення (ім'я, формат, розмір).
        Raises:
            StopIteration: Якщо зображення закінчилися.
        """
        if self.index >= len(self.files):
            raise StopIteration
        filename = self.files[self.index]
        self.index += 1
        path = os.path.join(self.directory, filename)
        with Image.open(path) as img:
            return {
                'filename': filename,
                'format': img.format,
                'size': img.size
            }

def save_image_stats_to_csv(directory, csv_path):
    """
    Зберігає метадані всіх зображень у каталозі у CSV-файл.
    Args:
        directory (str): Каталог з зображеннями.
        csv_path (str): Шлях до CSV-файлу.
    """
    iterator = ImageStatsIterator(directory)
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['filename', 'format', 'size'])
        writer.writeheader()
        for data in iterator:
            data['size'] = f"{data['size'][0]}x{data['size'][1]}"
            writer.writerow(data)

def main():
    """
    Демонструє збір статистики по зображеннях у каталозі та збереження у CSV.
    """
    directory = "images"  # Змініть на свій каталог
    csv_path = "image_stats.csv"
    save_image_stats_to_csv(directory, csv_path)
    print(f"Статистика збережена у {csv_path}")

if __name__ == "__main__":
    main()
