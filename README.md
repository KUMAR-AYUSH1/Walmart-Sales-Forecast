# Walmart Sales Forecast 📈

A Machine Learning project for forecasting Walmart store sales using multiple regression models such as XGBoost, Random Forest, and ARIMA.

The project includes:

* Model training and evaluation
* Hyperparameter tuning with Optuna
* Forecast visualization
* Streamlit dashboard
* Docker deployment

---

## 📂 Dataset

Dataset used from Kaggle:

[Walmart Sales Forecast Dataset](https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast?select=train.csv)

---

## 🚀 Models Used

* XGBoost
* Random Forest
* ARIMA

After experimentation, **XGBoost** achieved the best performance.

---

# 📓 Project Files

## `main.ipynb`

Initial experimentation notebook containing:

* Data preprocessing
* Feature engineering
* ARIMA implementation
* Random Forest model
* XGBoost model comparison

Result:

* XGBoost performed best among all models.

---

## `xgbtesting.ipynb`

Advanced XGBoost training notebook with:

* Feature scaling
* Hyperparameter tuning using Optuna⭐
* Model evaluation
* Saving the best model

### Best Result

* **R² Score: 0.7916**

Saved model:

* `xgb_model`

Also includes:

* Prediction plots
* Actual vs Predicted visualization

---

## `xgbtesting2.ipynb`

Training separate XGBoost models for Walmart store types:

### Store Type Results

| Store Type | Model        | R² Score |
| ---------- | ------------ | -------- |
| A          | `grid_xgb_A` | 0.676    |
| B          | `xgb_B`      | 0.680    |
| C          | `grid_xgb_C` | 0.752    |

Features:

* Separate training per store type
* Plot generation
* Forecast dataframe creation

Note:

* `xgb_B` was optimized using Optuna.

---

## `see.ipynb`

Visualization notebook for:

* Prediction plots
* Actual vs Predicted graphs ⭐
* Combined store forecasts

---

## `see2.ipynb ⭐`

Used for:

* Forecasting unseen test data
* Plotting predictions using: 

  * `grid_xgb_A`
  * `grid_xgb_C`
  * `xgb_B`

---

## `Dashbord.py`

Streamlit dashboard for:

* Viewing prediction graphs
* Exploring forecast dataframes
* Comparing model performance visually

---

# 🖥️ Streamlit Dashboard

Run locally:

```bash
streamlit run table.py
```

---

# 🐳 Docker Support

Build Docker image:

```bash
docker build -t walmart-sales-predction .
```

Run container:

```bash
docker run -p 8501:8501 walmart-sales-predction
```



---

# 📦 Docker Hub Image

Pull directly from Docker Hub:

```bash
docker pull kumar2700/walmart-sales-predction:latest
```

Run:

```bash
docker run -p 8501:8501 kumar2700/walmart-sales-predction:latest
```

---

# 📁 Additional Files

| File               | Description                                  |
| ------------------ | -------------------------------------------- |
| `requirements.txt` | Python dependencies                          |
| `Dockerfile`       | Docker container configuration               |
| `.dockerignore`    | Ignore unnecessary files during Docker build |

---

# 📊 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Optuna
* Matplotlib
* Streamlit
* Docker

---


# 👨‍💻 Author

Kumar Ayush
