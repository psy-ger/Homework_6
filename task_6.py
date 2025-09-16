import os


class DirectoryFilesIterator:
    """
    Ітератор для обходу всіх файлів у каталозі.
    """

    def __init__(self, directory):
        """
        Args:
            directory (str): Шлях до каталогу.
        """
        self.directory = directory
        self.files = [f for f in os.listdir(
            directory) if os.path.isfile(os.path.join(directory, f))]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration
        filename = self.files[self.index]
        self.index += 1
        path = os.path.join(self.directory, filename)
        size = os.path.getsize(path)
        return filename, size


def main():
    """
    Виводить назви та розміри всіх файлів у каталозі.
    """
    directory = "test_dir"  # Змініть на свій каталог
    for filename, size in DirectoryFilesIterator(directory):
        print(f"{filename}: {size} байт")


if __name__ == "__main__":
    main()
