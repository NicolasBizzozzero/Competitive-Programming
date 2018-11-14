from torch.utils.data import TensorDataset, DataLoader
import torch
from basics import FullyConnected
import zipfile
import torch.nn as nn
import math
from glob import glob

def generate_submit(tab, filename):
    """ tab->list  :    prediction
        create the file and write the prediction
        have to be in the good order
       """
    with open(filename, 'w') as f:
        for i in tab:
            f.write(str(i) + '\n')

device = torch.device("cuda:0")

data = torch.load("/home/cloud/hackathon/testdata.torchsave")

valset = TensorDataset(data)
valloader = DataLoader(valset, batch_size=64)


for filename in glob("/home/cloud/hackathon/models/mlp_models"):
    print(filename)
    splitted = filename.split("_")
    s, nb = int(splitted[0]), int(splitted[1])
    net_structure = [lsize] * d + [1]
    model = FullyConnected(data.size(1), net_structure).to(device)
    model.load_state_dict(torch.load(filename))
    model = model.to(device)
    pred = []
    for x in valloader:
        x = x[0].to(device)
        pred.extend(model(x).squeeze().cpu().detach().numpy().tolist())
    generate_submit(pred, "/home/cloud/hackathon/submit/prediction_" + filename)

def generate_submit(tab, filename):
    """ tab->list  :    prediction
        create the file and write the prediction
        have to be in the good order
       """
    with open(filename, 'w') as f:
        for i in tab:
            f.write(str(i) + '\n')    
