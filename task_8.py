import json
from contextlib import contextmanager

@contextmanager
def json_config_manager(filepath):
    """
    Контекстний менеджер для роботи з JSON-конфігурацією.
    Args:
        filepath (str): Шлях до JSON-файлу.
    Yields:
        dict: Конфігурація.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    yield config
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

def main():
    """
    Демонструє роботу з конфігураційним файлом через контекстний менеджер.
    """
    filepath = "config.json"
    with json_config_manager(filepath) as config:
        config['last_run'] = '2025-09-16'
    print(f"Конфігурацію збережено у {filepath}")

if __name__ == "__main__":
    main()
