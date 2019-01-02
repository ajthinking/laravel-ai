from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import torch
import sys
from torch.autograd import Variable
import json
import csv
import numpy as np
import torch.utils.data as data
import time

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        # input data has 99 rows.
        # Each row has 242 input neurons, 1 output neurons.
        self.l1 = nn.Linear(243, 243)
        self.l2 = nn.Linear(243, 243)
        self.l3 = nn.Linear(243, 1)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        # implement the forward pass
        out1 = self.l1(x)
        
        out2 = self.l2(out1)
        y_pred = self.l3(out2)
        #print(y_pred)
        #sys.exit()        
        return y_pred


class MigrationsDataset(data.Dataset):
    def __init__(self, train=False, test=False, transform=None, target_transform=None, download=False):
    
        data = []    
        with open(r"/Users/anders/Code/github-scrape-laravel/data/processed/migration-analysis-data.csv", 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            for row in reader:
                my_obj = {}
                for index, col in enumerate(row):
                    my_obj[headers[index]] = col
                data.append(my_obj)

        np.random.shuffle(data)
        split_point = int(np.floor(len(data)*0.9))
        migrations_train = data[0:split_point]
        migrations_test = data[split_point:-1]        

        tensor_input_data = []
        tensor_output_data = []
        start = time.time()

        self.global_word_bins = self.get_global_word_bins(migrations_train)
        
        for index, migration in enumerate(migrations_train):
            if((index+1) % 1000 == 0):
                print("Index at ", index)
                end = time.time()
                print(end-start)

            tensor_input_data.append(
                list(map(lambda word: float(word in self.get_local_word_bins(migration)), self.global_word_bins))
            )
            
            tensor_output_data.append([])
            
        sys.exit()
        self.x = Variable(torch.tensor(tensor_input_data, dtype=torch.float))
        self.y = Variable(torch.tensor(tensor_output_data, dtype=torch.float))
        
        
    def get_local_word_bins(self, migration):
        return migration['name'].split()    

    def get_global_word_bins(self, migrations):
        word_bins = []

        for migration in migrations:
            for word in self.get_local_word_bins(migration):
                if not (
                    word == '-' or
                    word.isdigit() or
                    word.lower() in word_bins
                ):
                    word_bins.append(word.lower())
        return word_bins

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return len(self.x)

train_loader = DataLoader(
    dataset=MigrationsDataset(train=True),
    batch_size=1000,
    shuffle=True,
    num_workers=2)

test_loader = DataLoader(
    dataset=MigrationsDataset(test=True),
    shuffle=True,
    num_workers=2)    

# our model
network = Network()

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

print("\nTesting...\n")
total_test_loss = 0
for i, data in enumerate(test_loader, 0):
    inputs, output = data
    prediction = int(network(inputs).data.item() * 9724) 
    actual = int(output.item() * 9724) 
    loss = abs(prediction - actual)
    total_test_loss += loss
    print("Migration", i, "predicted to ", prediction, "downloads. Error = ", loss)

print("\nfinished testing with a average loss of", int(total_test_loss/10) ,"downloads per migration\n")

#hour_var = Variable(torch.Tensor([[1.0]]))
#print("predict 1 hour ", 1.0, network(hour_var).data[0][0] > 0.5)
#hour_var = Variable(torch.Tensor([[7.0]]))
#print("predict 7 hours", 7.0, network(hour_var).data[0][0] > 0.5)