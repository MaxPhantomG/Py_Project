Представлена реализация текстового редактора (упрощенный аналог Блокнота)
# Установка и запуск (линукс)
```
sudo apt-get install -y python3-tk
git clone git@github.com:MaxPhantomG/Py_Project.git
cd Py_Project
python3 main.py
```
# Функционал (Базовый)
На первой статусной строке полный путь файла, с которым вы работаете (в начале работы просто 'Новый текстовый документ'), на второй - информация о последнем совершенном действии (изначально пустая).
Также есть два пункта меню: File и Edit. Первый содержит команды:
* New(ctrl+n) - создать новый файл.
* Open(ctrl+o) - открыть существующий файл
* Save(ctrl+s) - сохранить изменения в файле
* Save As(ctrl+a) - сохранить измнения и изменить имя/расположение файла при необходимости
* Exit(ctrl+e) - выйти

![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_1.png)
![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_2.png)

В случае нажатия команды Find(ctrl+f) пользователь должен набрать в открывшуюся форму нужную строку и нажать Enter. 

![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_3.png)

В случае нажатия команды Replace(ctrl+r) пользователь должен набрать в открывшуюся форму строку, **которую хочет заменить** и нажать Enter, затем набрать строку **которую хочет вставить и снова нажать Enter**

![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_4.png)
![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_5.png)

Примечание: *хоткеи для перемещения в начало/конец строки(ctrl+home/end) и начало/ конец файла(ctrl+PgUp/PgDn)установлены по умолчанию*
