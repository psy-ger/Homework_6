from contextlib import contextmanager

def even_numbers():
    """
    Генерує нескінченну послідовність парних чисел.
    Yields:
        int: Наступне парне число.
    """
    n = 0
    while True:
        yield n
        n += 2

@contextmanager
def limit_generator(gen, limit):
    """
    Контекстний менеджер для обмеження кількості елементів генератора.
    Args:
        gen (generator): Генератор.
        limit (int): Кількість елементів.
    Yields:
        generator: Обмежений генератор.
    """
    def limited():
        for i, val in enumerate(gen):
            if i >= limit:
                break
            yield val
    yield limited()

def main():
    """
    Генерує 100 парних чисел і зберігає їх у файл.
    """
    with limit_generator(even_numbers(), 100) as gen:
        with open("even_numbers.txt", "w", encoding="utf-8") as f:
            for num in gen:
                f.write(f"{num}\n")
    print("100 парних чисел збережено у even_numbers.txt")

if __name__ == "__main__":
    main()
