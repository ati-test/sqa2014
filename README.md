###Инструкция по установке Python+Selenium+Behave для Windows (тестировалось на Win7, Win8 и WinServer 2008)

####Установка Python3.4 + pip

* **Cкачайте Python 3.4.0:**
    * [Windows x86-64 MSI Installer](https://www.python.org/ftp/python/3.4.0/python-3.4.0.amd64.msi) для х64 Windows;
    * [Windows x86 MSI Installer](https://www.python.org/ftp/python/3.4.0/python-3.4.0.msi) для х32 битной Windows;

* **Запустите установку Python 3.4.0**

    <i>По умолчанию путь для установки C:\Python34\, инструкция основана на предположении, что туда вы его и поставите)</i>;
* **Укажите путь до python в системную переменную PATH:**
    * Откройте командную строку (WIN+R cmd);
    * Введите команду: ```setx PATH "%PATH%;C:\Python34;C:\Python34\Lib\;C:\Python34\Scripts\;"```;
    * Нажмите Enter;


    4.3 Должна появиться надпись "УСПЕХ", либо "SUCCESS":
    ![Консоль](https://dl.dropboxusercontent.com/u/58607821/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/Image%2048.png "Консоль")

    Если у вас возникла ошибка переполнения переменной (более 1024 знаков):
    ![Консоль](https://dl.dropboxusercontent.com/u/58607821/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/Image%2049.png "Консоль")
    
    То вы можете либо почистить PATH (только со знаем дела! Не поудаляйте лишнего) и вписать туда пути для python, либо     полностью прописывать пути испольняемых файлов при их запуске.

5. Перезапустите командную строку;
6. Убедитесь, что python работает, набрав команду ```python```(не сработает, если не прописана PATH. В таком случае пишем полный путь до python.exe). Если все ОК, то вы увидите следующую картину:
![Консоль](https://dl.dropboxusercontent.com/u/58607821/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%8B/cmdpython.jpg "Консоль")


7. Скачайте файл [distribute_setup.py](http://python-distribute.org/distribute_setup.py) в C:\Python34\ для установки easy_install;
8. В командной строке введите `python C:\Python34\distribute_setup.py` и дождитесь установки;
9. Установите pip командой: `easy_install pip`
    Альтернативная установка pip: скачайте файл [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py).
    Запустите его командой `python <путь до файла get-pip.py>`


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
