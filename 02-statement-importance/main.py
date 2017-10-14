import pandas as pnd
from sklearn.tree import DecisionTreeClassifier
from utils import print_answer

# 1. Загрузите выборку из файла titanic.csv с помощью пакета Pandas.

data = pnd.read_csv('titanic.csv')

# 2. Оставьте в выборке четыре признака: класс пассажира (Pclass), цену
# билета (Fare), возраст пассажира (Age) и его пол (Sex).

x_attributes = ['Pclass', 'Fare', 'Age', 'Sex']
X = data.loc[:, x_attributes]

# 3. Обратите внимание, что признак Sex имеет строковые значения.

f = lambda sex: 1 if sex == 'male' else 0
X['Sex'] = X['Sex'].map(f)

# 4. Выделите целевую переменную — она записана в столбце Survived.
Y = data['Survived']

# 5. В данных есть пропущенные значения — например, для некоторых пассажиров
# неизвестен их возраст. Такие записи при чтении их в pandas принимают значение
#  nan. Найдите все объекты, у которых есть пропущенные признаки, и удалите
# их из выборки.

X = X.dropna()
Y = Y[X.index.values]

# 6. Обучите решающее дерево с параметром random_state=241 и остальными параметрами по умолчанию (речь идет о параметрах конструктора DecisionTreeСlassifier).
dtc = DecisionTreeClassifier(random_state=241)
dtc.fit(X, Y)

# 7. Вычислите важности признаков и найдите два признака с наибольшей важностью. Их названия будут ответами для данной задачи (в качестве ответа укажите названия признаков через запятую или пробел, порядок не важен).

importances = pnd.Series(dtc.feature_importances_, index=x_attributes)
print_answer(1, ' '.join(importances.sort_values(ascending=False).head(2).index.values))