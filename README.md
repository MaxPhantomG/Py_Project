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
Также есть два пункта меню: File и Edit. Первый содержит команды: создать, открыть, сохранить, сохранить как, выйти. Второй - простые операции для работы с текстом (вставить, вырезать, скопировать, очистить).


![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_1.png)
![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_2.png)

В случае нажатия команды Find(ctrl+f) пользователь должен набрать в открывшуюся форму нужную строку и нажать Enter. 

![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_3.png)

В случае нажатия команды Replace(ctrl+r) пользователь должен набрать в открывшуюся форму строку, **которую хочет заменить** нажать Enter, затем набрать строку **которую хочет вставить и снова нажать Enter**

![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_4.png)
![](https://github.com/MaxPhantomG/Py_Project/blob/dev/images/Menu_5.png)

Примечание: *хоткеи для перемещения в начало/конец строки(Home/End) установлены по умолчанию*
