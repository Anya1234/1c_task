# Вступительное задание на кафедру 1С

### Код задачи: 143 "Крестики-нолики"
### Условие. 

На вход программе подаётся изображение игрового поля в крестики-нолики.

Необходимо обработать его и провести "победную" линию (перечёркивающую три одинаковых символа по правилам игры). Игровое поле может не содержать победителя (Тогда никакую линию проводить не надо). Гарантируется, что существует только одна победная линия. 

Формат изображения -- png. Игровое поле находится в произвольном месте изображения, однако гарантируется, что все символы имеют одинаковый размер/толщину и центрированы относительно секторов. Линии игрового поля проведены параллельно краям изображения. Если алгоритм решения будет требовать определённого размера/толщины фигур -- отразите это в документации.

### Решение. 

С помощью библиотеки pillow считываем изображение, парсим, черная ли клетка и достаточно ли непрозрачная. Находим центры клеток. Далее, если центр черный, то стоит крестик, если нет, то там либо пусто, либо нолик. Чтобы определить, что из этого, идем вверх до граници клетки, если нашли черную клетку, то нолик, если нет, то пусто

### Запуск. 

перед запуском устаность pillow и numpy  
_pip install pillow_  
_pip install numpy_  

запустить main.py

_python main.py_
