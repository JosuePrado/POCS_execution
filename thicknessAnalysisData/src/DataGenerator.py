import numpy as np
import pandas as pd

class DataGenerator:
    def __init__(self, seed=42, size=100):
        self.seed = seed
        self.size = size

    def generate_data(self):
        np.random.seed(self.seed)
        thickness = np.random.randint(10, 51, size=self.size)
        quantity = np.random.randint(10, 200, size=self.size)
        return pd.DataFrame({'Thickness': thickness, 'Quantity': quantity})
