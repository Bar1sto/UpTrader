Суть тестового задания: Древовидноеменю для Django
Простое и гибкое решение для реализации древовиных меню

<h2>Особенности</h2>
  <ul>Отображение меню через template tag</ul>
  <ul>Автоматическое определение активного URL</ul>
  <ul>Поддержка вложенности</ul>
  <ul>Редактирование/создание через админку</ul>

<h2>Установка</h2>
Клонируйте проект по ссылке https://github.com/Bar1sto/UpTrader.git
Выполните миграции командами:
<span>python -m venv venv</span> - создаем вирутальную машину
<span>python venv/Scripts/Activate</span> - активируем вирутальную машину
<span>python pip django</span> - устанавливаем Django
<span>python manage.py makemigrations</span>
<span>python manage.py migrate</span>

<h2>Использование</h2>
<ol>1. Создайте пункты меню через админку</ol>
При создании пункта меню укажите:
Name - название пункта
Menu name - название меню (например, 'main_menu')
Parent - родительский пункт (для вложенных меню)
URL или Named URL:
URL: относительный путь (например, "/about/")
Named URL: имя из urls.py (например, "about")
Order - порядок сортировки (меньше = выше)
2. Для каждой страницы которую хотите просмотреть надо добавить меню в шаблон
{% load menu_tags %}
<!DOCTYPE html>
<html>
<head>
    <title>Мой сайт</title>
</head>
<body>
    {% draw_menu 'main_menu' %}
    ...
</body>
</html>
3. Для просмотра новой страницы надо ее добавить в menu/templates/menu
Пример структуры меню
Главная (URL: "/", order: 0)
О нас (URL: "/about/", order: 10)
Услуги (URL: "/services/", parent: О нас, order: 0)
Команда (URL: "/team/", parent: О нас, order: 10)
Контакты (URL: "/contacts/", order: 20)
