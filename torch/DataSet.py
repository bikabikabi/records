import os

import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image


class HorseOrHumanDataset(Dataset):
    def __init__(self, root_dir, train=True):
        self.root_dir = root_dir
        self.train = train
        self.data = []

        if self.train:#训练集与测试集是不同的处理
            # 数据增强
            self.transform = transforms.Compose(
                [

                    transforms.Resize(256),
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomVerticalFlip(),
                    transforms.RandomRotation(degrees=10),
                    transforms.CenterCrop(224),
                    transforms.ToTensor(),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),

                ]
            )
            self.path = os.listdir(os.path.join(self.root_dir, 'train'))
            for label, path in enumerate(self.path):
                self.data.extend((os.path.join(self.root_dir, 'train', path, images), label) for images in
                                 os.listdir(os.path.join(self.root_dir, 'train', path)))

        else:
            self.transform = transforms.Compose(
                [
                    transforms.ToTensor(),
                    transforms.Resize((224, 224)),
                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),

                ]
            )
            self.path = os.listdir(os.path.join(self.root_dir, 'validation'))
            for label, path in enumerate(self.path):
                self.data.extend((os.path.join(self.root_dir, 'validation', path, images), label) for images in
                                 os.listdir(os.path.join(self.root_dir, 'validation', path)))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        # 调用时才加载图片
        image_path, label = self.data[index]
        image = Image.open(image_path)
        image = image.convert('RGB')
        image = self.transform(image)
        label = torch.tensor(label, dtype=torch.long)
        return image, label


if __name__ == '__main__':
    # 测试
    data = HorseOrHumanDataset(root_dir=r'.\horse-or-human', train=True)
    print(len(data))
    print(data[10])
