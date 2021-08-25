import torch.utils.data as data_utils
from SimulatedDatasets import SimulatedDataset, SimulatedDatasetTorso

""" Load SimECG data """
# Training
data = SimulatedDataset(index=242, root='SimECG/')
signals, labels = data.getRegularSet()
dataManager = data_utils.TensorDataset(signals, labels)
train_loader = data_utils.DataLoader(dataManager, batch_size=256, shuffle=True)
print(signals.size(), labels.size())


# Validation
data = SimulatedDataset(index=485, root='SimECG/')
signals, labels = data.getRegularSet()
dataManager = data_utils.TensorDataset(signals, labels)
val_loader = data_utils.DataLoader(dataManager, batch_size=256, shuffle=False)
print(signals.size(), labels.size())

# Test
data = SimulatedDataset(index=728, root='SimECG/')
signals, labels = data.getRegularSet()
dataManager = data_utils.TensorDataset(signals, labels)
test_loader = data_utils.DataLoader(dataManager, batch_size=256, shuffle=False)
print(signals.size(), labels.size())


""" Load SimECG-torso data """
data = SimulatedDatasetTorso(root='SimECG-torso/')
signals, labels = data.getRegularSet()
dataManager = data_utils.TensorDataset(signals, labels)
dataloader = data_utils.DataLoader(dataManager, batch_size=256, shuffle=False)
print(signals.size(), labels.size())

# We can load data differently depending on our interests. One crude example is provided in the function 
# splitXdirection(), which splits the data based on the factor "Swing along X-axis" to get train, val, and test data (TensorDataset).
train_data, val_data, test_data = data.splitXdirection()