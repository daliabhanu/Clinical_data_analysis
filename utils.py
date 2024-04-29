import torch
from torch.utils.data import Dataset

class EntityDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

def collate_fn(batch):
    inputs = [torch.tensor([seq_item[0] for seq_item in seq], dtype=torch.long) for seq in batch]
    labels = [torch.tensor([seq_item[1] for seq_item in seq], dtype=torch.long) for seq in batch]
    inputs = pad_sequence(inputs, batch_first=True, padding_value=0)
    labels = pad_sequence(labels, batch_first=True, padding_value=0)
    return inputs, labels
