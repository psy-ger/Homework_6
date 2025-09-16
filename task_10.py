import zipfile
from contextlib import contextmanager
import os


@contextmanager
def zip_archive_manager(zip_path):
    """
    Контекстний менеджер для архівування файлів.
    Args:
        zip_path (str): Шлях до zip-архіву.
    Yields:
        zipfile.ZipFile: Відкритий архів.
    """
    archive = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    try:
        yield archive
    finally:
        archive.close()


def main():
    """
    Демонструє архівування файлів у zip-архів.
    """
    zip_path = "archive.zip"
    files = ["file1.txt", "file2.txt"]  # Змініть на свої файли
    for fname in files:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(f"Дані для {fname}\n")
    with zip_archive_manager(zip_path) as archive:
        for fname in files:
            archive.write(fname)
    print(f"Архів {zip_path} створено.")


if __name__ == "__main__":
    main()
