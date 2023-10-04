# Расчет толщины подстилающего слоя дорожной одежды
#### Видео демо (eng):  https://youtu.be/OL5igIVnEOs
#### Описание:
При разработке проектов автомобильны дорог мы пользуемся определёнными нормативами и методиками расчета. Самая ответственная конструкция дороги - это дорожная одежда, так как она воспринимает все транспортные нагрузки. Ее корректный расчет - приоритетная задача при проектировании дорог.

Дорожная одежда рассчитывается на множество показателей влияющих на ее долговечность и прочность. Одним из этих расчетов - расчет на осушение подстилающего слоя дорожной одежды. В ходе расчета определяется минимальная допустимая толщина подстилающего слоя дорожной одежды, чтобы не допустить переувлажения конструкции.

В существующих программных продуктах Indor и Robur расчет производится некорректно. Поэтому я решил  сделать свою программу которая будет корректно выполнять этот расчет.

Моя программа написана на python с использованием фреймворка Flet для создания графического интерфейса. А также я использовал форк simpledt для представления таблиц. Исходные данные, таблицы и методика расчета взята из нормативного документа ПНСТ 542-2021

В процессе риализации проекта я познакомился с фреймворком Flet. Научился инмортировать и правильно представлять таблицы, а также встраивать их в интерфейс. Разработал базовый интерфейс программы поддерживающий любое разрешение экрана или окна. Подготовил программу которая умеет фильтровать пользовательский ввод.

Моя программа запрашивает у пользователя набор исходных данных. Часть из них принимается по соответсвующим таблицам, представленых на странице. Исходные данные вводятся в соответсвующие поименованные поля. Программе для расчета необходимы числовые данные в формате float. Также числа должны лежать в определеном интервале. Если введены не корректные данные при нажатии кнопки расчитать будет выведена ошибка с указанием что необходимо ввести.
