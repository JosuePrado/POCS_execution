from sklearn.cluster import KMeans

class WoodClassifier:
    def __init__(self, n_clusters=3, random_state=0):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)

    def define_thickness_range(self, thickness):
        if thickness < 20:
            return '10-19 cm'
        elif thickness < 30:
            return '20-29 cm'
        elif thickness < 40:
            return '30-39 cm'
        else:
            return '40-50 cm'

    def preprocess_data(self, df):
        df['Thickness_Range'] = df['Thickness'].apply(self.define_thickness_range)
        df['Thickness_Normalized'] = (df['Thickness'] - df['Thickness'].mean()) / df['Thickness'].std()
        df['Quantity_Normalized'] = (df['Quantity'] - df['Quantity'].mean()) / df['Quantity'].std()
        return df

    def fit_predict(self, df):
        df['Cluster'] = self.kmeans.fit_predict(df[['Thickness_Normalized', 'Quantity_Normalized']])
        return df

    def assign_labels(self, df):
        df['Average_Quantity'] = df.groupby('Cluster')['Quantity'].transform('mean')
        ordered_clusters = df.groupby('Cluster')['Average_Quantity'].mean().sort_values().index
        labels = ['Low', 'Medium', 'High']
        df['Label'] = df['Cluster'].map({ordered_clusters[i]: labels[i] for i in range(len(labels))})
        return df
    