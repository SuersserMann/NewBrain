import torch.utils.data
import torchvision
from matplotlib import pyplot as plt
import os
import warnings
import torch
import torch.nn as nn
from torch import optim
from torch.nn import functional as F

warnings.filterwarnings("ignore")
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


def plot_curve(data):
    fig = plt.figure()
    plt.plot(range(len(data)), data, color='blue')
    plt.legend(['value'], loc='upper right')
    plt.xlabel('step')
    plt.ylabel('value')
    plt.show()


def plot_image(img, label, name):
    fig = plt.figure()
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.tight_layout()
        plt.imshow(img[i][0] * 0.3081 + 0.1307, cmap='gray', interpolation='none')
        plt.title('{}:{}'.format(name, label[i].item()))
        plt.xticks([])
        plt.yticks([])
    plt.show()


def one_hot(label, depth=10):
    out = torch.zeros(label.size(0), depth)
    idx = torch.LongTensor(label).view(-1, 1)
    out.scatter_(dim=1, index=idx, value=1)
    return out


batch_size = 512
train_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist_data', train=True, download=True, transform=torchvision.transforms.Compose(
        [torchvision.transforms.ToTensor(), torchvision.transforms.Normalize((0.137,), (0.3081,))]
    )),
    batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist_data', train=False, download=True, transform=torchvision.transforms.Compose
        (
        [torchvision.transforms.ToTensor(),
         torchvision.transforms.Normalize((0.137,), (0.3081,))])
                               ),
    batch_size=batch_size, shuffle=False)

print(train_loader.dataset.data.float().min())
print(train_loader.dataset.data.float().max())
print((train_loader.dataset.data.float() / 255).mean())
print((train_loader.dataset.data.float() / 255).std())
x, y = next(iter(train_loader))
print(x.shape, y.shape, x.max(), x.min())

plot_image(x, y, 'data')


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # wx+b
        self.f1 = nn.Linear(28 * 28, 256)
        self.f2 = nn.Linear(256, 64)
        self.f3 = nn.Linear(64, 10)

    def forward(self, x_input):
        # x batch_size,channel=1,28*28
        # h1=relu(w1x+b1)
        x_input = F.relu(self.f1(x_input))
        # h2=relu(h1w2+b2)
        x_input = F.relu(self.f2(x_input))
        # h3=h2w3+b3
        x_input = self.f3(x_input)

        return x_input


model = Net()
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# print(device)
# model.to(device)

train_loss = []
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
for epoch in range(3):
    for batch_idx, (x, y) in enumerate(train_loader):
        out = model(x.view(x.size(0), x.size(1) * x.size(2) * x.size(3)))
        # [512,10]
        labels = one_hot(y)
        # before [512,]
        # [512,10]
        loss = F.mse_loss(out, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_loss.append(loss.item())
        if batch_idx % 10 == 0:
            print(epoch, batch_idx, loss.item())
plot_curve(train_loss)
total_correct = 0
for batch_idx, (x, y) in enumerate(test_loader):
    x = x.view(x.size(0), x.size(1) * x.size(2) * x.size(3))
    out = model(x)
    pre = out.argmax(dim=1)
    # 返回的是索引
    # out=[512,10]
    # pre=[512,]
    # y = y.to(device)
    # batch_size*784 -> batch_size
    correct = pre.eq(y).sum().float().item()
    total_correct += correct

n = len(test_loader.dataset)
print(total_correct / n)

x, y = next(iter(test_loader))
out = model(x.view(x.size(0), x.size(1) * x.size(2) * x.size(3)))
pre = out.argmax(dim=1)
plot_image(x, pre, 'test')
