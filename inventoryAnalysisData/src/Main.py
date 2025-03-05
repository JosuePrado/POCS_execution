import DataGenerator, Visualizer, WoodClassifier

class Main:
    def __init__(self):
        self.data_generator = DataGenerator()
        self.wood_classifier = WoodClassifier()
        self.visualizer = Visualizer()

    def run(self):
        df = self.data_generator.generate_data()
        df = self.wood_classifier.preprocess_data(df)
        df = self.wood_classifier.fit_predict(df)
        df = self.wood_classifier.assign_labels(df, self.data_generator.labels)

        self.visualizer.plot_clusters(df)
        self.visualizer.show_final_table(df)
        
if __name__ == "__main__":
    main = Main()
    main.run()
    