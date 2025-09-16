import shutil
from contextlib import contextmanager
import os

@contextmanager
def backup_file_manager(filepath):
    """
    Контекстний менеджер для резервного копіювання файлу.
    Args:
        filepath (str): Шлях до важливого файлу.
    Yields:
        str: Шлях до файлу.
    """
    backup_path = filepath + ".bak"
    shutil.copy2(filepath, backup_path)
    try:
        yield filepath
        os.remove(backup_path)
    except Exception:
        shutil.move(backup_path, filepath)
        raise

def main():
    """
    Демонструє резервне копіювання та відновлення файлу.
    """
    filepath = "important.txt"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("original data\n")
    try:
        with backup_file_manager(filepath):
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("new data\n")
            raise Exception("Test error!")  # Змініть/видаліть для перевірки
    except Exception:
        print("Відновлено резервну копію!")
    print("Готово.")

if __name__ == "__main__":
    main()
