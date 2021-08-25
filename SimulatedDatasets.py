import torch
import numpy as np
import torch.utils.data as data_utils


class SimulatedDataset():
    def __init__(self, index, root='SimECG/'):
        self.root = root
        self.data = torch.load(root + 'allData_{}.pth'.format(index))
    
    def getRegularSet(self):
        signals = self.data.data_tensor
        labels = self.data.target_tensor

        return signals, labels

class SimulatedDatasetTorso():
    def __init__(self, root='SimECG-torso/'):
        self.root = root
        self.data = torch.load(root + 'allData.pth')
    
    def getRegularSet(self):
        signals = self.data.data_tensor
        labels = self.data.target_tensor

        return signals, labels

    def splitXdirection(self): # labels for X is in 1st position 
        labels_ = self.data.target_tensor.numpy()
        labels = self.data.target_tensor
        all_data = self.data.data_tensor

        train_index = np.where(labels_[:,1] == - 10)
        train_data = torch.FloatTensor(all_data[train_index])
        train_label = torch.FloatTensor(labels[train_index])
        train_data = data_utils.TensorDataset(train_data, train_label)

        val_index = np.where(labels_[:,1] == 0)
        val_data = torch.FloatTensor(all_data[val_index])
        val_label = torch.FloatTensor(labels[val_index])
        val_data = data_utils.TensorDataset(val_data, val_label)

        test_index = np.where(labels_[:,1] == 0)
        test_data = torch.FloatTensor(all_data[test_index])
        test_label = torch.FloatTensor(labels[test_index])
        test_data = data_utils.TensorDataset(test_data, test_label)

        return train_data, val_data, test_data