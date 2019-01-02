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
import operator

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
        np.random.seed(1337)
        np.random.shuffle(data)
        split_point1 = int(np.floor(len(data)*0.1))
        split_point2 = int(np.floor(len(data)*0.11))
        migrations_train = data[0:split_point1]
        migrations_test = data[split_point1:split_point2]
        #migrations_ditched = data[split_point2:]

        if(train):
            migrations = migrations_train
        elif(test):
            migrations = migrations_test
        else:
            migrations = []

        self.datatypes = np.unique(
            list(map(lambda migration: migration['datatype'], migrations_train))
        )        

        tensor_input_data = []
        tensor_output_data = []

        self.global_word_bins = self.get_global_word_bins(migrations_train)

        for index, migration in enumerate(migrations):
            tensor_input_data.append(
                list(map(lambda word: float(word in migration['name']), self.global_word_bins))
            )
            
            tensor_output_data.append(list(map(lambda datatype: float(datatype == migration['datatype']), self.datatypes)))
        
        self.x = Variable(torch.tensor(tensor_input_data, dtype=torch.float))
        self.y = Variable(torch.tensor(tensor_output_data, dtype=torch.float))
        if(train):
            for y in self.y:
                pass#print("Y...", self.output_tensor_to_text(y))


    def get_datatypes(self):
        return self.datatypes

    def output_tensor_to_text(self, output_tensor):
        index, value = max(enumerate(output_tensor), key=operator.itemgetter(1))
        return self.datatypes[index]

    def input_tensor_to_text(self, input_tensor):
        index, value = max(enumerate(input_tensor), key=operator.itemgetter(1))
        return self.global_word_bins[index]            

    def get_local_word_bins(self, migration):
        return migration['name'].split()    

    def get_global_word_bins(self, migrations):
        return np.unique(list(
                
                map(
                        lambda migration: migration['name'],
                        migrations
                )
        ))

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return len(self.x)

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()

        migrationsDataset = MigrationsDataset()
        
        self.l1 = nn.Linear(len(migrationsDataset.global_word_bins), len(migrationsDataset.global_word_bins))
        self.l2 = nn.Linear(len(migrationsDataset.global_word_bins), len(migrationsDataset.global_word_bins))
        self.l3 = nn.Linear(len(migrationsDataset.global_word_bins), len(migrationsDataset.datatypes))
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        out1 = self.l1(x)
        out2 = self.l2(out1)
        y_pred = self.l3(out2)        
        return y_pred


train_loader = DataLoader(
    dataset=MigrationsDataset(train=True),
    batch_size=1000,
    shuffle=False,
    num_workers=2)

test_loader = DataLoader(
    dataset=MigrationsDataset(test=True),
    shuffle=False,
    num_workers=2)    

#sys.exit()

# our model
network = Network()

# Mean Square Error Loss
criterion = nn.MSELoss()
# Stochasctic gradient descent

optimizer = optim.SGD(network.parameters(), lr=0.01)

# training loop
for epoch in range(10):

    for i, data in enumerate(train_loader):
        # get the inputs
        inputs, output = data
        # wrap them in Variable
        inputs, output = Variable(inputs), Variable(output)

        # Forward pass: Compute predicted y by passing x to the model
        y_pred = network(inputs)
        # Compute and print loss
        loss = criterion(y_pred, output)
        
        #print(epoch, '\t', i, '\t', loss.item())

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

print("\nTesting...\n")
total_test_loss = 0

successes = 0
fails = 0

first_output = None
for i, data in enumerate(test_loader):
    inputs, output = data
    prediction = network(inputs).data 
    actual = output

    # print(
    #     test_loader.dataset.input_tensor_to_text(inputs),
    #     test_loader.dataset.output_tensor_to_text(actual)
    # )

    # print(
    #         "prediction for",
    #         test_loader.dataset.input_tensor_to_text(inputs),
    #         ":", 
    #         test_loader.dataset.output_tensor_to_text(prediction),
    #         "actual",
    #         test_loader.dataset.output_tensor_to_text(actual)
    # )

    if(test_loader.dataset.output_tensor_to_text(prediction) == test_loader.dataset.output_tensor_to_text(actual)):
        successes += 1
    else:
        fails += 1
migrationsDataset = MigrationsDataset()
length = len(migrationsDataset.global_word_bins)
for l in range(24):
    fake_data = np.zeros(length)
    fake_data[l] = 1.0
    torch.tensor(fake_data)
    print(test_loader.dataset.output_tensor_to_text(torch.tensor(fake_data)))


print("Summary successes", successes, "/", successes + fails)
