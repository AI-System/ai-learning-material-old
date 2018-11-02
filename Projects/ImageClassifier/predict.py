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

# input checkpoint

parser = argparse.ArgumentParser()
# 此处设置默认参数: input
parser.add_argument("i", "input") 
# 此处设置默认参数: checkpoint
parser.add_argument("cp", "checkpoint")
# 设置可选参数: --top_k
parser.add_argument("-t", "--top_k", type=int)
# 设置可选参数: --category_names
parser.add_argument("-cn", "--category_names")
# 设置可选参数: --gpu
parser.add_argument("-g", "--gpu", action="store_true")

# 获取参数
args = parser.parse_args()

# 声明变量
input = None; # 数据路径
checkpoint = None; # 保存检查点的路径
top_k = None; # 模型架构
category_names = None; # 学习速率
gpu = None; # 隐藏单元

# 通过参数更新数据
if args.input:
  input = args.input
  #print('args.input: ' , args.input)
if args.checkpoint:
  checkpoint = args.checkpoint
  #print('args.checkpoint: ', args.checkpoint)
if args.top_k:
  top_k = args.top_k
  #print('arags.top_k: ', args.top_k)
if args.category_names:
  category_names = args.category_names
  #print('args.category_names', args.category_names)
if args.gpu:
  gpu = args.gpu
  #print('args.gpu', args.gpu)

# 开始加载检查点
def load_ckp(filepath):
    ckp = torch.load(filepath)
    model = ckp['model']
    class_to_idx = ckp['class_to_idx']
    return model, class_to_idx

model, class_to_idx = load_ckp(checkpoint)

# 图像处理
def process_image(image):
    im = Image.open(image)
    w, h = im.size
    if w < h:
        pair = (256, int(256/w * h))
    else:
        pair = (int(256/h * w), 256)
    im = im.resize(pair)
    # 重新获取 w,h
    w, h = im.size
    # 你需要从图像的中心裁剪出 224x224 的部分
    w_crop = (w - 224) / 2
    h_crop = (h - 224) / 2
    # (left, upper, right, lower)
    box = (w_crop, h_crop, w - w_crop, h - h_crop)
    # print('box', box)
    #裁剪
    region = im.crop(box) 
    # print(region.size)
    # 图片转np
    np_image = np.array(region)
    # 图片除255进行归一化 标准化
    ave = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    np_image_norm = (np_image / 255 - ave) / std
    #print(np_image_norm)
    res = np_image_norm.transpose(2, 0, 1)
    return torch.from_numpy(res)

#显示图片功能
def imshow(image, ax=None, title=None):
    if ax is None:
        fig, ax = plt.subplots()
    image = image.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    image = std * image + mean
    image = np.clip(image, 0, 1)
    ax.imshow(image)
    return ax

# 显示图片
img_tensor = process_image(input)
imshow(img_tensor)

# 预测图片函数
def predict(image_path, model, topk=5):
    model.eval()
    # 处理图片
    img_tensor = process_image(image_path)
    # 加一维数据，让它变成一个4-D的Tensor
    fourDTensor = img_tensor.unsqueeze(0)
     # .type(torch.FloatTensor)
    fourDTensor = fourDTensor.type(torch.cuda.FloatTensor)
    # target = Variable(fourDTensor)
    target = Variable(fourDTensor.cuda(), volatile=True)
    output = model(target)
    # pre = torch.exp(output).data
    pre = torch.exp(output)
    probs, index = pre.topk(topk)
    # 再次处理
    probs = probs.cpu().detach().numpy().tolist()[0]
    index = index.cpu().detach().numpy().tolist()[0]
    res_index = []
    for i in index:
        res_index.append(class_to_idx[i])
    return probs, res_index

# 标签映射
with open(category_names, 'r') as f:
    cat_to_name = json.load(f)

# 预测图片
probs, classes = predict(input, model, top_k)
names = [cat_to_name[item] for item in classes]

print(probs)
print(names)