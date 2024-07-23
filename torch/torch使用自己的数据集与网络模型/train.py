import torch
from torch.utils.data import DataLoader
from torchvision.transforms import functional as F
from PIL import Image
from Net import MyNet
from DataSet import HorseOrHumanDataset

# 定义超参数
EPOCHS = 3
LEARNING_RATE = 1e-42
BATCH_SIZE = 64
TEST_BATCH_SIZE = 64
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
ID2CLASS = {0: "horse", 1: "human"}
# 创建数据集
train_dataset = HorseOrHumanDataset(root_dir=r".\horse-or-human", train=True)
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_dataset = HorseOrHumanDataset(root_dir=r".\horse-or-human", train=False)
test_loader = DataLoader(test_dataset, batch_size=TEST_BATCH_SIZE, shuffle=True)

"""
    训练模型
"""


def train():
    model = MyNet(pretrained=True).to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)
    criterion = torch.nn.CrossEntropyLoss()
    for epoch in range(EPOCHS):
        total = 0
        real = 0
        model.train()
        for batch_idx, (img, target) in enumerate(train_loader):
            total += img.shape[0]
            img, target = img.to(DEVICE), target.to(DEVICE)
            optimizer.zero_grad()
            output = model(img)
            real += torch.sum(torch.argmax(output, dim=1) == target).item()
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            print(f"Epoch: {epoch}, Batch: {batch_idx}, Loss: {loss.item():.6f},acc: {real / total:.6%}")
        acc = test(model)
        torch.save(model.state_dict(), f"check_point\a_{epoch}_{acc}.pth")


"""
    测试模型
"""

best_acc = 0


def test(model):
    global best_acc
    model.eval()
    total = 0
    real = 0
    with torch.no_grad():
        for batch_idx, (img, target) in enumerate(test_loader):
            img, target = img.to(DEVICE), target.to(DEVICE)
            output = model(img)
            real += torch.sum(torch.argmax(output, dim=1) == target).item()
            total += img.shape[0]
    acc = real / total
    print(f"acc in TestSet: {acc:.6%}")
    if acc > best_acc:
        best_acc = acc
        torch.save(model.state_dict(), r"check_point\BEST.pth")
    return acc


"""
    推理
"""


def predict(img_path):
    model = MyNet().to(DEVICE)
    model.load_state_dict(torch.load(r".\check_point\BEST.pth"))
    model.eval()
    img = Image.open(img_path)
    img = F.to_tensor(img)
    img = F.resize(img, [224, 224])
    img = F.normalize(img, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    output = model(img.unsqueeze(0).to(DEVICE))
    idx = torch.argmax(output, dim=1).item()
    return ID2CLASS[idx]


if __name__ == '__main__':
    train()
    print(predict(r'.\horse.png'))
    print(predict(r'.\human.png'))
