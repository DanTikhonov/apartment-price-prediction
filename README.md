# 🏠 Moscow Housing Price Prediction

Проект по предсказанию стоимости квартир в среднесрочной перспективе на основе данных о недвижимости Москвы и России.

---

## 📁 Структура проекта

```
project/
├── data/               # ❗ НЕ в git (см. .gitignore)
│   ├── raw/            # Исходные датасеты
│   └── processed/      # Обработанные данные
├── models/             # Сохранённые модели
├── notebooks/          # Jupyter-ноутбуки для исследования
├── src/                # Python-модули (предобработка, модели и т.д.)
├── .gitignore
├── README.md
└── requirements.txt
```

> **⚠️ Папка `data/` не хранится в репозитории.** После клонирования нужно создать её вручную и скачать данные (см. раздел ниже).

---

## ⚙️ Установка окружения

### 1. Клонировать репозиторий

```bash
git clone <url-репозитория>
cd <папка-проекта>
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

### 3. Активировать окружение

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

### 5. Зарегистрировать ядро для Jupyter

Чтобы Jupyter видел виртуальное окружение:

```bash
pip install ipykernel
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```

### 6. Запустить Jupyter

```bash
jupyter notebook
```

Открой папку `notebooks/`, создай новый ноутбук и в правом верхнем углу выбери ядро **Python (venv)**.

---

## 📦 Данные

Папку `data/` нужно создать вручную и положить в неё следующие файлы:

```
data/
└── raw/
    ├── moscow_housing_price_dataset.csv
    └── russia_real_estate_2021.csv
```

Скачать датасеты с Kaggle:

- [Moscow Housing Price Dataset](https://www.kaggle.com/datasets/egorkainov/moscow-housing-price-dataset)
- [Russia Real Estate 2021](https://www.kaggle.com/datasets/mrdaniilak/russia-real-estate-2021)

> **⚠️ Файл `russia_real_estate_2021.csv` весит ~870 МБ** — скачивание может занять время.

---

## 🚀 Быстрая проверка

После установки окружения и загрузки данных проверь, что всё работает:

```python
import pandas as pd

df1 = pd.read_csv('data/raw/moscow_housing_price_dataset.csv', nrows=3)
df2 = pd.read_csv('data/raw/russia_real_estate_2021.csv', nrows=3, sep=";")

print(df1.columns.tolist())
print(df2.columns.tolist())
```

---

## 🔧 Используемые технологии

- `pandas`, `numpy` — обработка данных
- `scikit-learn` — модели (Decision Tree, Random Forest и др.)
- `matplotlib`, `seaborn` — визуализация
- `jupyter` — интерактивная разработка
