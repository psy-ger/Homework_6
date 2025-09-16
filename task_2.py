import uuid

class UniqueIDIterator:
    """
    Ітератор для генерації унікальних ідентифікаторів на основі UUID4.
    """
    def __iter__(self):
        """
        Повертає ітератор (самого себе).
        Returns:
            UniqueIDIterator: Ітератор.
        """
        return self

    def __next__(self):
        """
        Генерує та повертає унікальний ідентифікатор (UUID4).
        Returns:
            str: Унікальний ідентифікатор у вигляді рядка.
        """
        return str(uuid.uuid4())


def main():
    """
    Демонструє використання UniqueIDIterator для генерації унікальних ідентифікаторів.
    """
    iterator = UniqueIDIterator()
    for _ in range(5):
        print(next(iterator))


if __name__ == "__main__":
    main()
