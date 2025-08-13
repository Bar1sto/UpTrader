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
<ol><code>python -m venv venv</code> - создаем вирутальную машину</ol>
<ol><code>python venv/Scripts/Activate</code> - активируем вирутальную машину</ol>
<ol><code>python pip django</code> - устанавливаем Django</ol>
<ol><code>python manage.py makemigrations</code></ol>
<ol><code>python manage.py migrate</code></ol>

<h2>Использование</h2>
<ol>1. Создайте пункты меню через админку</ol>
<ol></ol>При создании пункта меню укажите:</ol>
<ol>Name - название пункта</ol>
<ol>Menu name - название меню (например, 'main_menu')</ol>
<ol>Parent - родительский пункт (для вложенных меню)</ol>
<ol>URL или Named URL:</ol>
<ol>URL: относительный путь (например, "/about/")</ol>
<ol>Named URL: имя из urls.py (например, "about")</ol>
<ol>Order - порядок сортировки (меньше = выше)</ol>
<ol>2. Для каждой страницы которую хотите просмотреть надо добавить меню в шаблон</ol>
<ol>{% load menu_tags %}</ol>
<ol><!DOCTYPE html></ol>
<ol><html></ol>
<ol><head></ol>
 <ol>   <title>Мой сайт</title></ol>
<ol></head></ol>
<ol><body></ol>
   <ol> {% draw_menu 'main_menu' %}</ol>
   <ol> ...</ol>
<ol></body></ol>
<ol></html></ol>
<ol>3. Для просмотра новой страницы надо ее добавить в menu/templates/menu</ol>
<ol>Пример структуры меню</ol>
<ol>Главная (URL: "/", order: 0)</ol>
<ol>О нас (URL: "/about/", order: 10)</ol>
<ol>Услуги (URL: "/services/", parent: О нас, order: 0)</ol>
<ol>Команда (URL: "/team/", parent: О нас, order: 10)</ol>
<ol>Контакты (URL: "/contacts/", order: 20)</ol>
