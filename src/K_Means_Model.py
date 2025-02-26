import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


  # Train a model on 'Age','Annual_Income','Spending_Score' features
def k_M_model(df):
    k = range(3,9)
    K = []
    ss = []
    for i in k:
        kmodel = KMeans(n_clusters=i).fit(df[['Age','Annual_Income','Spending_Score']], )
        ypred = kmodel.labels_
        sil_score = silhouette_score(df[['Age','Annual_Income','Spending_Score']], ypred)
        K.append(i)
        ss.append(sil_score)

# Store the number of clusters and their respective silhouette scores in a dataframe

    Variables3 = pd.DataFrame({'cluster': K, 'Silhouette_Score':ss})
    print(Variables3)
   
    return Variables3
    