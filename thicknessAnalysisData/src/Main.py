import DataGenerator, Visualizer, thicknessAnalysisData.src.ThinchnessWoodClassifier as ThinchnessWoodClassifier

class Main:
    def __init__(self):
        self.data_generator = DataGenerator()
        self.wood_classifier = ThinchnessWoodClassifier()
        self.visualizer = Visualizer()

    def run(self):
        df = self.data_generator.generate_data()
        df = self.wood_classifier.preprocess_data(df)
        df = self.wood_classifier.fit_predict(df)
        df = self.wood_classifier.assign_labels(df)
        self.visualizer.plot_pie_chart(df)
        self.visualizer.show_table(df)

if __name__ == "__main__":
    main = Main()
    main.run()
    