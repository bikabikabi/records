import torch
import torch.nn as nn
from torchvision.models import resnet50


class MyNet(nn.Module):
    def __init__(self, class_num=2, pretrained=False):
        super().__init__()
        # 使用resnet50作为特征提取网络
        self.resnet = resnet50(pretrained=pretrained)
        # 将resnet50的输出层替换成新的全连接层，用于训练分类器
        self.resnet.fc = nn.Linear(2048, class_num)

    def forward(self, x):
        x = self.resnet(x)
        x = torch.sigmoid(x) # 输出层使用sigmoid激活函数
        return x
