from __future__ import print_function
import torch.utils.data as data
from PIL import Image
import os
import os.path
import gzip
import numpy as np
import torch
import codecs
import pandas as pd
import json
from torch.autograd import Variable
import sys

class MigrationsDataset(data.Dataset):
    def __init__(self, train=False, test=False, transform=None, target_transform=None, download=False):
        
        with open('/Users/anders/Code/github-scrape-laravel/data/processed/migration-analysis-data-sample.json') as file:
            migrations_train = json.load(file)
        if train:
            migrations = migrations_train

        tensor_input_data = []
        tensor_output_data = []

        for migration in migrations:
            tensor_input_data.append(
                    [1,2,3,4,5] #migration[:5] STRINGS! (do bag of words or convolution?)
            )
            tensor_output_data.append(
                    [1] #migration[-1:] STRINGS! (do bag of words or convolution?)
            )

        self.x = Variable(torch.tensor(tensor_input_data, dtype=torch.float)) #pylint: disable=E1101,E1102
        self.y = Variable(torch.tensor(tensor_output_data, dtype=torch.float)) #pylint: disable=E1101,E1102

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return len(self.x)