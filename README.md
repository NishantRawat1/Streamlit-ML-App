# 🌼 Streamlit Iris Flower Predictor

A simple, interactive web application built using **Streamlit** to demonstrate a deployed **Machine Learning model**. This app uses a trained **Random Forest Classifier** to predict the species of an Iris flower based on user inputs.

---

## 🔍 Features

- Input sliders for Sepal and Petal dimensions
- Real-time prediction of Iris flower species
- Visual display of prediction confidence scores
- Optional data exploration and correlation heatmap

---

## 📁 Project Structure

```
my_ml_app/
├── model.pkl             # Pre-trained RandomForest model
├── app.py                # Streamlit application code
├── train_model.py        # Script to train and save model
├── requirements.txt      # Python dependencies
└── README.md             # Project instructions
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Streamlit-ML-App.git
cd Streamlit-ML-App
```

> Replace `your-username` with your GitHub username.

---

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv .venv
# Activate (Windows)
.venv\Scripts\activate
# Activate (macOS/Linux)
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Train the Model (Optional)

```bash
python train_model.py
```

This will create a file called `model.pkl`.

---

### 5. Run the Streamlit App

```bash
streamlit run app.py
```

The app will be available at: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Example

- Sepal Length: 5.8
- Sepal Width: 3.0
- Petal Length: 4.2
- Petal Width: 1.3  
👉 Prediction: *Versicolor*

---

## 📚 Built With

- [Streamlit](https://docs.streamlit.io/)
- [Scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

---

## ✍️ Author

**Nishant Rawat**  
B.Tech CSE (Data Science)  
[LinkedIn](https://www.linkedin.com/in/nishant-rawat-6020b2261/) | [GitHub](https://github.com/NishantRawat1)

---

## 📝 License

This project is licensed under the MIT License.
