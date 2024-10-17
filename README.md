# 📈 Gold Price Prediction Model

This project leverages **Random Forest Regression** to forecast gold prices by analyzing key financial indicators. By training on historical data, the model delivers **precise predictions for future gold prices**, offering insightful and reliable estimates based on input factors. Whether for investment analysis or market strategy, this model provides a powerful tool for anticipating gold price trends.

## ✨ Features
- **Predicts Gold Prices** based on input financial indicators such as:
  - 🏦 **S&P 500 Index (SPX)**
  - 🛢 **United States Oil Fund (USO)**
  - 🪙 **Silver Price (SLV)**
  - 💱 **EUR/USD Exchange Rate**
- **Visualizes Actual vs Predicted Values** for better performance evaluation.
- **Trained Using Random Forest Regressor** with 100 decision trees.
- **R² Error Metric** for accuracy evaluation.

## 📂 Data
The dataset includes historical gold prices and financial indicators such as SPX, USO, SLV, and EUR/USD. The dataset is read from a `.csv` file called `gold_price_data.csv`.

## 🛠️ Libraries Used
- `NumPy` for numerical operations
- `Pandas` for data manipulation
- `Matplotlib` and `Seaborn` for data visualization
- `Scikit-learn` for model building and evaluation

## ⚙️ How It Works

1. **Data Loading and Preprocessing**:
    - The data is read from a CSV file and the **Date** column is converted into a `datetime` format.
    - Features (`SPX`, `USO`, `SLV`, `EUR/USD`) are separated from the target variable (`GLD`).

2. **Model Training**:
    - A **Random Forest Regressor** is trained on the preprocessed data with 80% of the data used for training and 20% for testing.

3. **Prediction**:
    - The model predicts gold prices on test data and also allows users to input their own values for prediction.

4. **Performance Evaluation**:
    - The performance of the model is evaluated using the **R² Score**.
    - A line plot is used to compare the actual gold prices with the predicted prices.

## 📊 Visualization

The project generates a comparison between the actual and predicted gold prices using a line plot. 

## 🔢 Performance
- **R² Score**: `0.9` indicating high model accuracy.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Install the required libraries using:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
