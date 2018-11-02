#%matplotlib inline
#%config InlineBackend.figure_format = 'retina'

import matplotlib.pyplot as plt

import torch
from torch import nn 
from torch import optim 
# 训练相关
import torch.nn.functional as F
from torch.autograd import Variable 
from torch.utils.data import DataLoader 
import torchvision
from torchvision import datasets, transforms 
import torchvision.models as models
import json
from tqdm import tqdm 
import numpy as np
from PIL import Image 
import copy
from collections import OrderedDict

# 命令行相关
import argparse 

parser = argparse.ArgumentParser()
# 此处设置默认参数: data_directory
parser.add_argument("data_directory") 
# 设置可选参数: --save_dir
parser.add_argument("-sd", "--save_dir")
# 设置可选参数: --arch
parser.add_argument("-a", "--arch")
# 设置可选参数: --learning_rate
parser.add_argument("-l", "--learning_rate", type=float)
# 设置可选参数: --hidden_units
parser.add_argument("-hu", "--hidden_units", type=int)
# 设置可选参数: --epochs
parser.add_argument("-ep", "--epochs", type=int)
# 设置可选参数: --gpu
parser.add_argument("-g", "--gpu", action="store_true")
# 获取参数
args = parser.parse_args()

# 声明变量
data_directory = None # 数据路径
save_dir = None # 保存检查点的路径
arch = None # 模型架构
learning_rate = 0.01 # 学习速率
hidden_units = 0 # 隐藏单元
epochs = None # 训练周期
gpu = False # 是否使用gpu

if args.data_directory:
  #print('args.data_directory: ' , args.data_directory)
  data_directory = args.data_directory
if args.save_dir:
  #print('args.save_dir: ' , args.save_dir)
  save_dir = args.save_dir
if args.arch:
  #print('args.arch: ' , args.arch)
  arch = args.arch
if args.learning_rate:
  #print('args.learning_rate: ' , args.learning_rate)
  learning_rate = args.learning_rate
if args.hidden_units:
  #print('args.hidden_units: ' , args.hidden_units)
  hidden_units = args.hidden_units
if args.epochs:
  #print('args.epochs: ' , args.epochs)
  epochs = args.epochs
if args.gpu:
  #print('args.gpu: ' , args.gpu)
  gpu = args.gpu

'''
# test passed
print('show the result --------------')
print()
print('data_directory: ', data_directory)
print('save_dir: ', save_dir)
print('arch: ', arch)
print('learning_rate: ', learning_rate)
print('hidden_units: ', hidden_units)
print('epochs: ', epochs)
print('gpu: ', gpu)
'''

# 训练集
data_transforms_train = transforms.Compose([
    transforms.RandomResizedCrop(244), # 此处224是图片尺寸
    transforms.RandomRotation(45),
    transforms.RandomHorizontalFlip(), # RandomResizedCrop 
    transforms.ToTensor(), # 转换成Torch张量
    transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225]) # 标准化张量图片
])

# Load the datasets with ImageFolder
image_datasets_train = datasets.ImageFolder(data_directory, transform = data_transforms_train)

# Using the image datasets and the trainforms, define the dataloaders
dataloaders_train = DataLoader(image_datasets_train, batch_size=64, shuffle=True)

# 标签映射
with open('cat_to_name.json', 'r') as f:
    cat_to_name = json.load(f)

# 判断arch
archStr = 'densenet121' # 默认使用 densenet121 架构
if arch != None:
  archStr = arch

# 通过架构设置model
model = models[archStr](pretrained=True)
model.classifier.in_features

# 初始化参数 requires_grad
for param in model.parameters():
    # print(param)
    param.requires_grad = False

# 分类器
model.classifier = nn.Sequential(OrderedDict([
    ('fcl', nn.Linear(1024, 500)),
    ('relu', nn.ReLU()),
    ('drop', nn.Dropout(p=0.5)),
    ('fc2', nn.Linear(500, len(cat_to_name))),
    ('output', nn.LogSoftmax(dim=1))]))

# 是否迁移到GPU   
if gpu:
  model.cuda()  
  criterion = nn.NLLLoss().cuda()
else:
  criterion = nn.NLLLoss()

# 定义优化器 
# optimizer = optim.Adam(model.parameters(), lr = 0.001)
optimizer = optim.Adam(model.classifier.parameters(), lr = 0.001)

# 定义训练方法
def train(model, dataloaders_train, criterion, optimizer):
    model.train()
    n_batches = len(dataloaders_train)
    all_loss = 0.0
    all_acc = 0
    for inputs, labels in dataloaders_train:
        inputs = Variable(inputs.cuda())
        labels = Variable(labels.cuda())
        optimizer.zero_grad() # 权重初始化
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        all_loss += loss.data[0]
        loss.backward() # 反向传播
        optimizer.step()
        pre = torch.exp(outputs).data
        equlity = (labels.data == pre.max(1)[1])
        all_acc += equlity.type_as(torch.FloatTensor()).mean()
    average = all_loss / n_batches
    accuracy = all_acc / n_batches
    print('Average loss: {: .3f}, Accuracy: ({:.3f})\n'.format(average, accuracy))

# 开始训练
best_acc = 0
best_model = model

# 16 多个epoch数量
num = 1

# 如果参数中有epochs, 那么更新训练周期
if epochs != None:
  num = epochs

for epoch in range(1, num):
    print('epoch = ', epoch)
    train(model, dataloaders_train, criterion, optimizer)
    #best_acc, best_model = test(model, dataloaders_valid, criterion, best_acc, best_model)



