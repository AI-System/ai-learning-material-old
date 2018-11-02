
# 定义文件夹
train_dir = 'flowers/train'
valid_dir = 'flowers/valid'
test_dir = 'flowers/test'

# 训练集
data_transforms_train = transforms.Compose([
    transforms.RandomResizedCrop(244), # 此处224是图片尺寸
    transforms.RandomRotation(45),
    transforms.RandomHorizontalFlip(), # RandomResizedCrop 
    transforms.ToTensor(), # 转换成Torch张量
    transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225]) # 标准化张量图片
])

# 测试数据集
data_transforms_test = transforms.Compose([
    transforms.RandomResizedCrop(244), # 此处224是图片尺寸
    transforms.ToTensor(), # 转换成Torch张量
    transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225]), # 标准化张量图片
])

# TODO: Load the datasets with ImageFolder
image_datasets_train = datasets.ImageFolder(train_dir, transform = data_transforms_train)
image_datasets_valid = datasets.ImageFolder(valid_dir, transform = data_transforms_test)
image_datasets_test = datasets.ImageFolder(test_dir, transform = data_transforms_test)

# TODO: Using the image datasets and the trainforms, define the dataloaders

dataloaders_train = DataLoader(image_datasets_train, batch_size=64, shuffle=True)
dataloaders_valid = DataLoader(image_datasets_valid, batch_size=64)
dataloaders_test = DataLoader(image_datasets_test, batch_size=64)

# 标签映射
with open('cat_to_name.json', 'r') as f:
    cat_to_name = json.load(f)

# 构建和训练分类器

# 初始化 requires_grad 为 False 冻结参数
for param in model.parameters():
    # print(param)
    param.requires_grad = False


model.classifier = nn.Sequential(OrderedDict([
    ('fcl', nn.Linear(1024, 500)),
    ('relu', nn.ReLU()),
    ('drop', nn.Dropout(p=0.5)),
    ('fc2', nn.Linear(500, len(cat_to_name))),
    ('output', nn.LogSoftmax(dim=1))]))

# 迁移到GPU     
model.cuda()  
criterion = nn.NLLLoss().cuda()
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