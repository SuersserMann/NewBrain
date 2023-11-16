import numpy as np
import torch
import torch.nn as nn

x_train = list(range(1, 101))
x_train = np.array(x_train, dtype='float32')
x_train = x_train.reshape(-1, 1)
y_train = 2 * x_train


class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        out = self.linear(x)
        return out


input_dim = 1
output_dim = 1

model = LinearRegressionModel(input_dim, output_dim)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

criterion = nn.MSELoss()
learning_rate = 0.00001
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

epochs = 2000

for epoch in range(epochs):
    inputs = torch.from_numpy(x_train).to(device)
    labels = torch.from_numpy(y_train).to(device)

    optimizer.zero_grad()
    outputs = model(inputs)

    loss = criterion(outputs, labels)

    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(f'epoch{epoch},loss{loss.item()}')

torch.save(model.state_dict(), 'model.pkl')
model.load_state_dict((torch.load('model.pkl')))
p = torch.from_numpy(x_train).to(device)
prediction = model(p)
print(prediction)
