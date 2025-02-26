import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'src'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from src.K_Means_Model import k_M_model


# upload data
file_path = r"C:\algonquin\2025W\2216_ML\2216_project\2216_project_mall_customer\data\mall_customers.csv"
df = pd.read_csv(file_path)
print(os.getcwd())

# Streamlite title
st.title('Mall Customer Clustering Results')

# use Streamlit show DataFrame
Variable3 = k_M_model(df)
st.write(Variable3)


# plot silhouette 
fig, ax = plt.subplots()
ax.plot(Variable3['cluster'], Variable3['Silhouette_Score'], marker='o')
ax.set_xlabel('Number of Clusters')
ax.set_ylabel('Silhouette Score')
ax.set_title('Silhouette Score for Different Numbers of Clusters')

# use Streamlit demo graphic
st.pyplot(fig)

max_score_index = Variable3['Silhouette_Score'].idxmax()
best_k = int(Variable3.iloc[max_score_index]['cluster'])
best_silhouette = Variable3.iloc[max_score_index]['Silhouette_Score']
st.write("Best K:", best_k)
st.write("Best Silhouette Score:", best_silhouette)

#select best model
best_model = KMeans(n_clusters=best_k, random_state=42).fit(df[['Age', 'Annual_Income', 'Spending_Score']])

# input customer info
st.subheader("Input Customer Data to Predict Cluster")
age = st.number_input("Age", min_value=0, max_value=100, value=30, step=1)
annual_income = st.number_input("Annual Income (k$)", min_value=0, max_value=150, value=50, step=1)
spending_score = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, value=50, step=1)

if st.button("Predict Cluster"):
    # ready to input
    customer_data = pd.DataFrame({
        'Age': [age],
        'Annual_Income': [annual_income],
        'Spending_Score': [spending_score]
    })

    # use the best model to predict customer cluster
    cluster_label = best_model.predict(customer_data)[0]

    # show prediction result
    st.write("### Prediction Result")
    st.write(f"This customer belongs to Cluster {cluster_label}")
    
    # show customer characteristics
    st.write("#### Customer Features")
    st.write(f"Age: {age}")
    st.write(f"Annual Income: {annual_income} k$")
    st.write(f"Spending Score: {spending_score}")

    # show cluster center
    cluster_centers = best_model.cluster_centers_
    st.write("#### Cluster Center (Mean Features)")
    st.write({
        'Age': cluster_centers[cluster_label][0],
        'Annual_Income': cluster_centers[cluster_label][1],
        'Spending_Score': cluster_centers[cluster_label][2]
    })