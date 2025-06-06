# automation

1. Установка Python. Ссылка скачивания - https://www.python.org/downloads/. Во время установки сохранить путь куда будет установлен python, понадобиться в дальнейшем. Установить галочку в чекбоксе Add python.exe to PATH
2. Установка Pycharm Community Edition. Ссылка для установки - https://www.jetbrains.com/pycharm/download/?section=windows
3. Создание проект в Pycharm. Создать проект. Выбрать Pure Python. Задать название проекту. Выбрать Custom Environment, далее в поле Environment
 выбрать значение Select existing. В поле Python path вставить сохраненный путь к python.exe из первого шага.
4. Установка pytest. В терминале ввести команду - pip install pytest
5. Установка playwright. В терминале ввести команду - pip install pytest-playwright
6. Установка необходимых браузеров. В терминале ввести команду - playwright install
7. Установка библиотеки для параллельных запусков. В терминале ввести команду - pip install pytest-xdist
8. Установка библиотеки для формирования отчетов. В терминале ввести команду - pip install pytest-html

# commands

pytest - run all test files (file name should start from "test")

pytest -m tag_name  - run all tests with this tag name (above test should be this line "@pytest.mark.tag_name")

pytest test_PyTestValidation.py - run selected test file

pytest test_PyTestValidation.py::test_second_check - run selected test from selected file

pytest test_PyTestValidation.py::test_second_check -s  - run selected test from selected file with showing test results printed

pytest test_PyTestValidation.py::test_second_check --headed  - when using a shortcut fixture "page" to run in headed mode

pytest test_framework_web_api.py --browser_name firefox   - run in  firefox (--browser_name is a environment variable that can be read in tests)

pytest -m smoke  - запустит тесты с лейблом smoke (@pytest.mark.smoke)

pytest -k web_api    - запустит только те тесты которые содержат переданный кусок текста в названии (например test_e2e_web_api)

pytest -m smoke --html=report.html   - html report