import matplotlib.pyplot as plt

class Visualizer:
    def show_table(self, df):
        summary_table = df.groupby('Thickness_Range').agg({
            'Quantity': 'sum',
            'Cluster': 'mean',
            'Label': lambda x: x.mode()[0]
        }).reset_index()
        print("Summary Table:")
        print(summary_table)

    def plot_pie_chart(self, df):
        thickness_range_counts = df['Thickness_Range'].value_counts()
        plt.figure(figsize=(8, 6))
        plt.pie(thickness_range_counts, labels=thickness_range_counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
        plt.title('Wood Stock Distribution by Thickness Range')
        plt.show()
        