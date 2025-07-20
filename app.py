import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()
iris = load_iris()

# Streamlit UI
st.title("🌼 Iris Flower Predictor")
st.write("Enter flower measurements to predict species.")

# Input sliders
sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.8)
sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 4.2)
petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 1.3)

# Prediction
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                          columns=iris.feature_names)
prediction = model.predict(input_data)[0]
proba = model.predict_proba(input_data)[0]
target_names = iris.target_names

st.success(f"🌸 Predicted species: **{target_names[prediction]}**")

# Show prediction probabilities
st.subheader("Prediction Probabilities")
st.bar_chart(pd.DataFrame([proba], columns=target_names))

# Optional: dataset & visualization
if st.checkbox("Show Dataset & Correlation Heatmap"):
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    st.dataframe(df.head())

    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.iloc[:, :-1].corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
