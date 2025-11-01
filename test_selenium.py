from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys


def test_website_with_options():
    """
    Тест для проверки работы Selenium с различными настройками браузера.
    Адрес сайта задается через переменную для удобства изменения.
    """

    # НАСТРОЙКА ПЕРЕМЕННЫХ
    # ====================

    # Адрес сайта для тестирования - легко изменить в одном месте
    WEBSITE_URL = "https://www.google.com"

    # Ожидание в секундах для визуальной проверки
    DELAY_SECONDS = 5

    # Размер окна по умолчанию (если не указан через аргументы)
    DEFAULT_WINDOW_SIZE = "1920,1080"

    # Создаем объект для настройки опций Chrome
    chrome_options = Options()

    # ОБРАБОТКА АРГУМЕНТОВ КОМАНДНОЙ СТРОКИ
    # =========================================

    # Опция: --headless - запуск браузера без графического интерфейса
    # Использование: python test_selenium.py --headless
    if '--headless' in sys.argv:
        chrome_options.add_argument('--headless')
        print("✅ Режим headless включен (браузер без графического интерфейса)")

    # Опция: --window-size - установка кастомного размера окна
    # Использование: python test_selenium.py --window-size 1280,720
    if '--window-size' in sys.argv:
        try:
            # Ищем позицию аргумента --window-size в командной строке
            size_index = sys.argv.index('--window-size')
            # Берем следующий аргумент - это размер окна (например, "1280,720")
            window_size = sys.argv[size_index + 1]
            chrome_options.add_argument(f'--window-size={window_size}')
            print(f"✅ Установлен размер окна: {window_size}")
        except (IndexError, ValueError):
            # Если размер не указан, используем размер по умолчанию
            chrome_options.add_argument(f'--window-size={DEFAULT_WINDOW_SIZE}')
            print(f"✅ Использован размер окна по умолчанию: {DEFAULT_WINDOW_SIZE}")
    else:
        # Если --window-size не указан, используем полноэкранный режим
        chrome_options.add_argument('--start-maximized')
        print("✅ Включен полноэкранный режим")

    # Инициализация драйвера с выбранными опциями
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # ОСНОВНАЯ ЛОГИКА ТЕСТА
        # ========================

        # Открываем страницу используя переменную с адресом
        print(f"🌐 Загрузка страницы: {WEBSITE_URL}")
        driver.get(WEBSITE_URL)
        print("✅ Страница успешно загружена")

        # Задержка для визуальной проверки (значение из переменной)
        print(f"⏳ Ожидание {DELAY_SECONDS} секунд для визуальной проверки...")
        time.sleep(DELAY_SECONDS)

        # ПРОВЕРКИ
        # =========

        # Получаем текущий URL страницы
        current_url = driver.current_url
        print(f"📊 Текущий URL: {current_url}")

        # Проверяем, что мы действительно на нужной странице
        # Используем переменную WEBSITE_URL для проверки
        assert WEBSITE_URL in current_url, f"Ошибка: не на целевой странице. Ожидалось: {WEBSITE_URL}, получено: {current_url}"
        print("✅ Проверка URL пройдена - находимся на целевой странице")

        # Выводим заголовок страницы для дополнительной проверки
        print(f"📄 Заголовок страницы: '{driver.title}'")

    except Exception as e:
        # Обработка любых ошибок, которые могут возникнуть во время теста
        print(f"❌ Произошла ошибка: {e}")
        raise  # Повторно поднимаем исключение для видимости в консоли
    finally:
        # ЗАВЕРШЕНИЕ РАБОТЫ
        # ==================
        # Этот блок выполнится ВСЕГДА, даже если возникла ошибка
        driver.quit()
        print("✅ Браузер корректно закрыт")


if __name__ == "__main__":
    """
    ТОЧКА ВХОДА ПРОГРАММЫ
    Запуск теста с различными вариантами.

    Чтобы изменить тестируемый сайт, поменяйте переменную WEBSITE_URL выше.

    Варианты использования:
    1. python test_selenium.py                    - полноэкранный режим
    2. python test_selenium.py --headless         - headless режим  
    3. python test_selenium.py --window-size 1280,720 - кастомный размер
    4. python test_selenium.py --headless --window-size 1920,1080 - комбинация

    Параметры:
    --headless      - запуск без графического интерфейса (для CI/CD)
    --window-size   - установка размера окна (ширина,высота)
    """
    test_website_with_options()
