###Инструкция по установке python+selenium+behave для Windows

####Установка python3.3 + pip

1. Перейдите на сайт [www.python.org/getit/](http://www.python.org/getit/)
2. Скачайте Python 3.3.4 (Windows x86-84 MSI Installer для х64 Windows или Python 3.3.4 Windows x86 MSI Installer для х32 битной Windows);
3. Запустите установку Python 3 (запомните путь для установки, по умолчанию c:\Python33\);
4. Укажите путь до питона в системную переменную PATH. Для этого:
    * Откройте командную строку(WIN+R cmd);
    * Введите команду: ```setx PATH "%PATH%;C:\Python33;C:\Python33\Lib\;C:\Python33\Scripts\;"```
Нажмите Enter;
    * Должна появиться надпись "Успех".
5. Перезапустите командную строку;
6. Убедитесь, что питон работает, набрав команду ```python```. Если все ОК, то нажмите ctrl+z и enter.
7. Скачайте файл [distribute_setup.py](http://python-distribute.org/distribute_setup.py) в C:\Python33\distribute_setup.py для установки easy_install;
8. В командной строке введите `python C:\Python3\distribute_setup.py` и дождитесь установки;
9. Установите pip командой: `easy_install pip`

####Установка selenium + behave

1. Установите selenium. Для этого выполните команду `pip install selenium`;
2. Установите behave:
    * Если у вас установлен в системе git, то используйте команду: `pip install git+https://github.com/wirewit/behave`
    * Если у вас НЕ установлен git, то, либо [установите git](http://git-scm.com/downloads/) (предпочтительный вариант), либо [скачайте ZIP архив](https://github.com/wirewit/behave/archive/master.zip/) в папку c:\Python33
    * Затем перейдите в папку Python33, используя команду: `cd c:\Python33`
    * И установите behave командой: `pip install behave-master.zip`
    
###Полезные ссылки (на английском!)
1. [Behave 1.2.3 documentation](http://pythonhosted.org/behave/) Все, что вам требуется знать о Behave.
2. [Selenium with Python](http://selenium-python.readthedocs.org/) Здесь можно подсмотреть методы WebDriver. Как перейти по ссылке, найти элемент на странице, заполнить поле и многое другое.