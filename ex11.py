import numpy as np

def train_tes_split(data:list) -> tuple:
    size = int(len(data) * 0.8)
    train_data = data[:size]
    test_data = data[size:]
    return (train_data, test_data)
data = np.arange(1, 51)
np.random.shuffle(data)
print(data)
print(train_tes_split(data))
print(train_tes_split(data))
