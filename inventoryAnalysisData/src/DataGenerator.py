import numpy as np
import pandas as pd

class DataGenerator:
    def __init__(self, seed=42, size=100):
        self.seed = seed
        self.size = size
        self.labels = ['Low', 'Medium', 'High']
        self.wood_types = ['Log', 'Wet Wood', 'Dry Wood', 'Drying Process']

    def generate_data(self):
        np.random.seed(self.seed)
        data = {
            'Wood_Type': np.random.choice(self.wood_types, size=self.size),
            'Stock': np.random.randint(10, 300, size=self.size)
        }
        return pd.DataFrame(data)
    