Mall Customer Clustering Application
This application uses Streamlit to visualize and predict customer clusters based on their age, annual income, and spending score. The model applies K-Means clustering to segment customers into groups, helping businesses better understand customer behavior and preferences.

Features
•	User-friendly interface powered by Streamlit.
•	Data upload and visualization: Automatically loads the dataset and displays clustering results.
•	Real-time clustering prediction: Allows users to input customer details (age, income, and spending score) and predict the cluster to which they belong.
•	Graphical visualization: Displays silhouette scores to assess the optimal number of clusters.
•	Accessible via Streamlit Community Cloud.

Dataset
The application uses the Mall Customers dataset stored in a CSV file, which contains the following features:
•	Age: The customer’s age.
•	Annual_Income: Customer's annual income in $1000s.
•	Spending_Score: A score assigned by the mall based on the customer's spending behavior.

Technologies Used
•	Streamlit: For building the web-based interface.
•	Pandas and NumPy: For data manipulation and preprocessing.
•	Scikit-learn: For K-Means clustering and silhouette score calculation.
•	Matplotlib and Seaborn: For visualizing cluster scores and results.
•	Logging: For debugging and data loading validation.

Model
The clustering model:
•	Uses K-Means with cluster sizes ranging from 3 to 8.
•	Computes silhouette scores to evaluate cluster quality.
•	Selects the best-performing model based on the highest silhouette score.
•	Predicts the customer’s cluster based on their age, income, and spending score.

Installation (for local deployment)
If you want to run the application locally, follow these steps:
1.	Clone the repository:
git clone https://github.com/chen041081733/2216_project_mall_customer.git
cd 2216_project_mall_customer
2.	Create and activate a virtual environment:
python -m venv env
source env/bin/activate  # On Windows, use `env\\Scripts\\activate`
3.	Install dependencies:
pip install -r requirements.txt
4.	Run the Streamlit application:
streamlit run MallCustomers_Streamlit.py

Usage
1.	Load the Dataset:
The app automatically loads the mall customer dataset from the GitHub repository.
2.	Visualize Silhouette Scores:
The app displays a line chart showing silhouette scores for different cluster sizes, helping you identify the optimal number of clusters.
3.	Predict Customer Cluster:
o	Enter customer details:
	Age
	Annual Income (k$)
	Spending Score
o	Click "Predict Cluster" to view the predicted cluster and the characteristics of the cluster center.

Thank you for using the Mall Customer Clustering Application!  

Streamlit link:
https://2216projectmallcustomer-dutfolgkqyafw3xq8enb2g.streamlit.app/


