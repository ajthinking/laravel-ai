from Network import Network
from MigrationsDataset import MigrationsDataset
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import sys
from torch.autograd import Variable

train_loader = DataLoader(
    dataset=MigrationsDataset(train=True),
    batch_size=1000,
    shuffle=True,
    num_workers=2)    

# our model
network = Network()

print("All ok 2+3")
sys.exit()

# Mean Square Error Loss
criterion = nn.MSELoss()
# Stochasctic gradient descent
optimizer = optim.SGD(network.parameters(), lr=0.01)

# training loop
print("epoch", '\t', "iteration", '\t', "loss")
for epoch in range(500):
    for i, data in enumerate(train_loader, 0):
        # get the inputs
        inputs, output = data

        # wrap them in Variable
        inputs, output = Variable(inputs), Variable(output)

        # Forward pass: Compute predicted y by passing x to the model
        y_pred = network(inputs)
        # Compute and print loss
        loss = criterion(y_pred, output)
        
        print(epoch, '\t', i, '\t', loss.item())

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

