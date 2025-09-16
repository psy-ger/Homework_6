from contextlib import contextmanager


@contextmanager
def binary_file_reader(filepath, block_size=1024):
    """
    Контекстний менеджер для зчитування бінарних файлів блоками.
    Args:
        filepath (str): Шлях до бінарного файлу.
        block_size (int): Розмір блоку у байтах.
    Yields:
        generator: Генератор блоків байтів.
    """
    def reader():
        with open(filepath, 'rb') as f:
            while True:
                block = f.read(block_size)
                if not block:
                    break
                yield block
    yield reader()


def main():
    """
    Демонструє зчитування бінарного файлу блоками.
    """
    filepath = "test.bin"
    with open(filepath, 'wb') as f:
        f.write(b'\x00' * 5000)
    with binary_file_reader(filepath, 1024) as blocks:
        for block in blocks:
            print(f"Блок: {len(block)} байт")


if __name__ == "__main__":
    main()
