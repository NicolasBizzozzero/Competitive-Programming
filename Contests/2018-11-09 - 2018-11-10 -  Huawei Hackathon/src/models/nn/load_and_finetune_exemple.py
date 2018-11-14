from torchvision import models
import torch.nn as nn


# Exemple pretrained models and finetune last layer

m = models.resnet50(pretrained=True)

for p in m.parameters():
    p.requires_grad = False

m.fc = nn.Linear(2048,10)

print(m)
