from sklearn.cluster import KMeans
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import pandas as pd

print('query')
engine = create_engine('mysql+pymysql://gastos:gastos@uuubuntu/gastos')
query = "select debe from gasto where debe is not null and debe > 0  and debe < 100 and LOCATE('YAPE', descripcion) > 0"
df = pd.read_sql(query, con=engine)

print('clustering')
kmeans = KMeans(n_clusters=2, random_state=0)
df['Cluster'] = kmeans.fit_predict(df[['debe']])

print('plotting')
plt.scatter(df['debe'], [0] * len(df), c=df['Cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_, [0] * len(kmeans.cluster_centers_), 
            color='red', marker='x', label='Centroids')
plt.xlabel('Values')
plt.title('Clustering Result')
plt.legend()
plt.show()
