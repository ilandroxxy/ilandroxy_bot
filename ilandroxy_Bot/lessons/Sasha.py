# region Домашка: ************************************************************



# endregion Домашка: ************************************************************


# region Урок: ************************************************************

# Импортирование необходимых библиотек
import pandas as pd  # Импорт библиотеки pandas для работы с данными в виде таблицы
from sklearn.model_selection import train_test_split  # Импорт функции train_test_split из библиотеки scikit-learn для разделения данных на обучающую и тестовую выборки
from sklearn.ensemble import RandomForestClassifier  # Импорт класса RandomForestClassifier из библиотеки scikit-learn для создания и обучения модели случайного леса
from sklearn.metrics import accuracy_score  # Импорт функции accuracy_score из библиотеки scikit-learn для оценки производительности модели
import matplotlib.pyplot as plt  # Импорт библиотеки matplotlib.pyplot для визуализации данных

# Загрузка набора данных
data = pd.read_csv('high_diamond_ranked_10min.csv')  # Загрузка данных из CSV файла в pandas DataFrame

# Определение признаков и целевой переменной
X = data.drop(['gameId', 'blueWins'], axis=1)  # Определение признаков, исключая столбцы 'gameId' и 'blueWins'
y = data['blueWins']  # Определение целевой переменной 'blueWins'

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # Разделение данных на обучающую и тестовую выборки в соотношении 80:20

# Создание и обучение модели случайного леса
model = RandomForestClassifier()  # Создание объекта модели случайного леса
model.fit(X_train, y_train)  # Обучение модели на обучающей выборке

# Оценка производительности модели на тестовой выборке
y_pred = model.predict(X_test)  # Предсказание целевой переменной на тестовой выборке
accuracy = accuracy_score(y_test, y_pred)  # Вычисление точности модели на тестовой выборке

# Определение важности признаков
importance = model.featureimportances  # Получение важности признаков из обученной модели

# Визуализация важности признаков в виде графика
plt.bar(X.columns, importance)  # Создание столбчатой диаграммы с признаками по оси X и их важностью по оси Y
plt.xlabel("Features")  # Название оси X
plt.ylabel("Importance")  # Название оси Y
plt.title("Feature Importance")  # Заголовок графика
plt.xticks(rotation=90)  # Поворот названий признаков на 90 градусов
plt.show()  # Отображение графика



# endregion Урок: ************************************************************



# todo: Александра = []
# на прошлом уроке: Обсудили сложную домашку по машинному обучению, надо читать материалы
# на следующем уроке:
