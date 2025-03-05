import matplotlib.pyplot as plt

class Visualizer:

    def plot_clusters(self, df):
        plt.scatter(df['Wood_Type'], df['Stock'], c=df['Cluster'], cmap='viridis', s=100)
        plt.xlabel('Wood Type')
        plt.ylabel('Available Stock')
        plt.title('Wood Stock Classification')
        plt.colorbar(label='Cluster')
        plt.show()

    def show_final_table(self, df):
        final_table = df.groupby('Wood_Type').agg({
            'Stock': 'mean',
            'Cluster': 'mean',
            'Label': lambda x: x.mode()[0]
        }).reset_index()
        final_table['Wood_Type'] = final_table['Wood_Type'].replace({0: 'Log', 1: 'Wet Wood', 2: 'Dry Wood', 3: 'Drying Process'})
        print(final_table[['Wood_Type', 'Stock', 'Cluster', 'Label']])
