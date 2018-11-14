from torch.utils.data import TensorDataset, DataLoader
import torch
from basics import FullyConnected
import zipfile
import torch.nn as nn
import math
device = torch.device("cuda:0")

data = torch.load("../../../../hackathon/validationdata.torchsave")
net_structure = [2048, 1024, 1]
model = FullyConnected(data.size(1), net_structure)
model.load_state_dict(torch.load("best_model.save"))
model = nn.Sequential(model, nn.Sigmoid())
model = model.to(device)
valset = TensorDataset(data)
valloader = DataLoader(valset, batch_size=64)

layers = []
for x in valloader:
    pred = x[0].to(device)
    layers = next(model.children())
    for layer in layers:
        pred = layer(pred)
        if type(layer) == type(nn.ReLU()):
            layers.append(pred)

first_layer = torch.Tensor(layers[::2])
second_layer = torch.Tensor(layers[1::2])

torch.save(first_layer, "firstlayer.torchsave")
torh.save(second_layer, "secondlayer.torhsave")
