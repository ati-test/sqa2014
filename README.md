###Инструкция по установке python+selenium+behave для Windows

####Установка python3.4 + pip

1. Перейдите по ссылке [https://www.python.org/downloads/release/python-340//](https://www.python.org/downloads/release/python-340/)
2. Скачайте Python 3.4.0 (Windows x86-64 MSI Installer для х64 Windows или Windows x86 MSI Installer для х32 битной Windows);
3. Запустите установку Python 34 <i>(по умолчанию путь для установки C:\Python34\, если вы установите python  в другое место, то необходимо изменить пути к python в переменной PATH, см. п.п. 4.2)</i>;
4. Укажите путь до python в системную переменную PATH. Для этого:
    4.1 Откройте командную строку(WIN+R cmd);
    4.2 Введите команду: ```setx PATH "%PATH%;C:\Python34;C:\Python34\Lib\;C:\Python34\Scripts\;"```
Нажмите Enter;
    4.3 Должна появиться надпись "УСПЕХ", либо "SUCCESS".
5. Перезапустите командную строку;
6. Убедитесь, что питон работает, набрав команду ```python```. Если все ОК, то вы увидите следующую картину:

[Консоль]([https://dl.dropboxusercontent.com/u/58607821/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cmdpython.jpg] изображения "Консоль")


7. Скачайте файл [distribute_setup.py](http://python-distribute.org/distribute_setup.py) в C:\Python33\distribute_setup.py для установки easy_install;
8. В командной строке введите `python C:\Python3\distribute_setup.py` и дождитесь установки;
9. Установите pip командой: `easy_install pip`

####Установка selenium + behave

1. Установите selenium. Для этого выполните команду `pip install selenium`;
2. Установите behave:
    2.1 Если у вас установлен в системе git, то используйте команду: `pip install git+https://github.com/wirewit/behave`
    2.2 Если у вас НЕ установлен git, то, либо [установите git](http://git-scm.com/downloads/)  и см. предыдущий пункт (предпочтительный вариант), либо [скачайте ZIP архив](https://github.com/wirewit/behave/archive/master.zip/) в папку c:\Python33
    2.3 Затем перейдите в папку Python33, используя команду: `cd c:\Python33`
    2.4 И установите behave командой: `pip install behave-master.zip`
    
###Полезные ссылки (на английском!)
1. [Behave 1.2.3 documentation](http://pythonhosted.org/behave/) Все, что вам требуется знать о Behave.
2. [Selenium with Python](http://selenium-python.readthedocs.org/) Здесь можно подсмотреть методы WebDriver. Как перейти по ссылке, найти элемент на странице, заполнить поле и многое другое.
