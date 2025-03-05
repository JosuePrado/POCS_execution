from sklearn.cluster import KMeans

class WoodClassifier:

    def __init__(self, n_clusters=3, random_state=0):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)

    def preprocess_data(self, df):
        df['Wood_Type'] = df['Wood_Type'].astype('category').cat.codes
        return df

    def fit_predict(self, df):
        """Aplica K-means y asigna clusters."""
        df['Cluster'] = self.kmeans.fit_predict(df[['Wood_Type', 'Stock']])
        return df

    def assign_labels(self, df, labels):
        df['Average_Stock'] = df.groupby('Cluster')['Stock'].transform('mean')
        ordered_clusters = df.groupby('Cluster')['Average_Stock'].mean().sort_values().index
        df['Label'] = df['Cluster'].map({ordered_clusters[i]: labels[i] for i in range(len(labels))})
        return df
    