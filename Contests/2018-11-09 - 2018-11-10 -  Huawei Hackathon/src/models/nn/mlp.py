from basics import FullyConnected
import pandas as pd
import numpy as np
from tqdm import tqdm
from itertools import count
import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import TensorDataset, random_split, DataLoader

def iter_labels(path_dir, filename="../../../hackathon/true_labels_training.txt"):
    with open(path_dir + "/" + filename, 'r') as f:
        for y in str(f.readlines()[0]):
            yield y


device = torch.device("cuda:0")


data = torch.load("../../../../hackathon/trainingdata.torchsave")
labels = torch.Tensor([int(y) for y in iter_labels(path_dir="../")])


dataset = TensorDataset(data, labels)

trainlength = int(0.8 * data.size(0))
trainset, testset = random_split(dataset, [trainlength, data.size(0) - trainlength])

trainloader = DataLoader(trainset, batch_size=64)
testloader = DataLoader(testset, batch_size=64)

depth = [2, 3, 4, 5]
layer_size = [512, 256, 128]

for d in depth:
    for lsize in layer_size:
        net_structure = [lsize] * d + [1]
        model = FullyConnected(data.size(1), net_structure).to(device)
        optimizer = optim.Adam(model.parameters())
        loss_function = nn.BCEWithLogitsLoss()

        best_test = (np.inf, -1)
        best_model = model.state_dict()
        max_delay = 3
        for epoch in count():
            with tqdm(trainloader, bar_format="{l_bar}{bar}{n_fmt}/{total_fmt}, ETA:{remaining}{postfix}", ncols=80, desc="Epoch " + str(epoch)) as t:
                mean_loss, n = 0, 0
                for x, y in t:
                    x = x.to(device)
                    y = y.to(device)
                    pred = model(x)
                    loss = loss_function(pred.squeeze(), y.squeeze())

                    n += 1
                    mean_loss = ((n-1) * mean_loss + loss.item()) / n
                    t.set_postfix({"train_loss": "{0:.3f}".format(mean_loss)})

                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()

            with tqdm(testloader, bar_format="{l_bar}{bar}{n_fmt}/{total_fmt}, ETA:{remaining}{postfix}", ncols=80, desc="Epoch " + str(epoch)) as t:
                mean_loss, n = 0, 0
                for x, y in t:
                    x = x.to(device)
                    y = y.to(device)

                    pred = model(x)
                    loss = loss_function(pred.squeeze(), y.squeeze())

                    n += 1
                    mean_loss = ((n-1) * mean_loss + loss.item()) / n
                    t.set_postfix({"test_loss": "{0:.3f}".format(mean_loss)})

            if mean_loss < best_test[0]:
                best_test = (mean_loss, epoch)
                best_model = model.state_dict()
            elif epoch - best_test[1] >= max_delay:
                break

        torch.save(best_model, str(lsize) + "_" + str(d) + "_best_model.save")
