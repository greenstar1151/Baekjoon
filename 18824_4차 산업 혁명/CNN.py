import copy

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision



class Net(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.relu = nn.ReLU()
        self.conv1 = nn.Conv2d(1, 1, kernel_size=3, padding=0, bias=True)
        self.conv2 = nn.Conv2d(1, 1, kernel_size=3, padding=0, bias=True)
        self.fc1 = nn.Linear(144, 64)
        self.out = nn.Linear(64, 10)
        self.pool = nn.MaxPool2d(2, 2)

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.flatten(start_dim=1)
        x = self.relu(self.fc1(x))
        x = self.out(x)
        return x


# MNIST dataset
transform = torchvision.transforms.Compose(
    [
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize((0.1307,), (0.3081,)),
    ]
)

mnist_data_test = torchvision.datasets.MNIST(root="./data", train=False, transform=transform, download=True)
mnist_data_train = torchvision.datasets.MNIST(root="./data", train=True, transform=transform, download=True)

train_loader = torch.utils.data.DataLoader(
    mnist_data_train, batch_size=64, shuffle=True, drop_last=True
)
test_loader = torch.utils.data.DataLoader(
    mnist_data_test, batch_size=64, shuffle=False, drop_last=False
)



model = Net()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9, weight_decay=0.01)

epochs = 10
losses = list()
accuracies = list()

best_model = copy.deepcopy(model.state_dict())
best_accuracy = 0
log_print_step = set(
    [min(round(0.1 * x * len(train_loader)), len(train_loader)) for x in range(1, 11)]
)

for epoch in range(epochs):
    epoch_loss = 0
    epoch_accuracy = 0
    batch = 0

    model.train()
    for idx, (x, y) in enumerate(train_loader):
        # x = x.cuda()
        # y = y.cuda()

        optimizer.zero_grad()
        output = model(x)

        loss = criterion(output, y)
        loss.backward()

        optimizer.step()

        _, y_pred = torch.max(output, 1)
        accuracy = sum(y == y_pred)

        epoch_accuracy += accuracy.item()
        epoch_loss += loss.item()

        batch += len(x)
        if idx in log_print_step or idx == (len(train_loader) - 1):
            print(
                "Epoch: {} [{}/{} ({:.0f}%)],\tAccuracy: {:.1f}%,  \t Loss: {:.6f}".format(
                    epoch + 1,
                    batch,
                    len(train_loader.dataset),
                    100.0 * (idx + 1) / len(train_loader),
                    100.0 * (accuracy.item() / len(x)),
                    loss.item(),
                )
            )

    val_accuracy = 0
    val_loss = 0

    model.eval()
    with torch.no_grad():
        for idx, (x, y) in enumerate(test_loader):
            # x = x.cuda()
            # y = y.cuda()

            output = model(x)

            loss = criterion(output, y)

            _, y_pred = torch.max(output, 1)
            accuracy = sum(y == y_pred)

            val_accuracy += accuracy.item()
            val_loss += loss.item()
    print("=====================================================")
    print(
        "Test Accuracy: {:.1f}%,  \t Loss: {:.6f}".format(
            100.0 * (val_accuracy / len(test_loader.dataset)),
            val_loss / len(test_loader),
        )
    )
    print("=====================================================")

    if val_accuracy >= best_accuracy:
        best_model = copy.deepcopy(model.state_dict())
        best_accuracy = val_accuracy
        print("Best model is updated.")

    losses.append(val_loss / len(test_loader))
    accuracies.append((val_accuracy / len(test_loader.dataset)))


torch.save(best_model, "./model/CNN.pt")
