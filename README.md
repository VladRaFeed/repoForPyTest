### Instruction for using git

В першу чергу, нам потрібно створити репозиторій.

Для створення репозиторію заходимо на гітхаб, та натискаємо кнопку "New"

- Вводимо назву у поле *Repository name*, додаємо Description (бажано мінімально щось написати).

- Приватність репозиторію <b>ОБОВ'ЯЗКОВО ПУБЛІЧНИЙ.</b>

- # Також раджу додати файл README.md щоб не створювати його потім.

- Натискаємо Create repository 

- Репозиторій створено, ура!

Далі нам необхідно скопіювати репозиторій який ми створили. 

#  Для цього:

- На сторінці репозиторію знаходимо кнопку "Code", та натискаємо на неї.

- Після натискання з'явиться посилання, яке нам треба скопіювати.

- приклад: https://github.com/VladRaFeed/repoForPyTest.git

# Копіювання

Щоб скопіювати репозиторій, відкриваємо консоль bash.

Пишемо:

1. cd (на всяк випадок виходимо в корінь)

2. cd Desktop/

3. Копіюємо наш репозиторій: git clone https://github.com/VladRaFeed/repoForPyTest.git (посилання твоє)

4. Після успішного копіювання пишемо code *Назва Репозиторію*

Після успішного копіювання, та виконаних кроків, переходимо у VScode.

Тепер можна розробляти застосунки та працювати з ними.

# Зберігання коду в репо (комміти, пуши, пули)

1. Для коміту треба підтвердити всі зміни командою git add . 
*Точка використовується для позначення всіх файлів, у разі, якщо нам треба апрувнути якийсь один, просто пишемо його назву*

2. Далі пишемо git commit -m "ТутБудеТайтлКоміту" -m "ТутБудеДескрпіпшн"

3. Після коміту пишемо git push

4. Наш комміт на репозиторію! 

5. Для перевірки оновлень використовуємо git fetch