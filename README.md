# 🎬 Movie Success Predictor

Machine Learning project that predicts **movie revenue** based on movie features such as budget, popularity, ratings, and release year.

---

# 📊 Project Overview

This project uses the **TMDB 5000 Movies Dataset** and a **Random Forest Regressor** to predict how successful a movie will be at the box office.

The project includes the full Machine Learning workflow:

✔ Data exploration  
✔ Data preprocessing  
✔ Feature engineering  
✔ Model training  
✔ Model evaluation  
✔ Revenue prediction

---

# 🧠 Machine Learning Model

Model used:

**RandomForestRegressor**

Evaluation metrics:

- MAE (Mean Absolute Error)
- R² Score

The trained model is saved as:
models/movie_model.pkl

---

# 📂 Project Structure


movie-success-predictor
├── app
│ └── streamlit_app.py
├── data
│ └── tmdb_5000_movies.csv
│
├── images
│ ├── revenue_distribution.png
│ ├── budget_vs_revenue.png
│ ├── correlation_heatmap.png
│ ├── budget_distribution.png
│ └── rating_vs_revenue.png
│
├── models
│ └── movie_model.pkl
│
├── notebooks
│ └── analysis.ipynb
│
├── check_data.py
├── data_preprocessing.py
├── train_model.py
├── predict.py
│
├── requirements.txt
├── README.md
└── .gitignore


---

# 📈 Dataset

Dataset: **TMDB 5000 Movies Dataset**

Example features:

- budget
- popularity
- runtime
- vote_average
- vote_count
- release_year

Target variable:


revenue


Example row from dataset:

| Movie | Budget | Popularity | Runtime | Revenue |
|------|------|------|------|------|
| Avatar | 237000000 | 150.4 | 162 | 2787965087 |

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/movie-success-predictor.git

Go to project folder:

cd movie-success-predictor

Install dependencies:

pip install -r requirements.txt
▶️ How to Run
Check dataset
python check_data.py
Train model
python train_model.py

After training the model will be saved in:

models/movie_model.pkl
Predict revenue
python predict.py

Example prediction:

Predicted revenue: 512345678.00
📊 Example Workflow
Dataset
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Revenue Prediction
🛠 Technologies Used

Python
pandas
scikit-learn
matplotlib
seaborn
joblib
Jupyter Notebook

🚀 Future Improvements

Possible improvements for the project:

Feature importance visualization

Hyperparameter tuning

More feature engineering

Deep learning models

Web interface using Streamlit

API using FastAPI

👩‍💻 Author

Tamuna

Aspiring Software Engineer / Data Science Enthusiast
