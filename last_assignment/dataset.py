import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader

def calculate_mean_std(dataset):
    loader = DataLoader(dataset, batch_size=128, shuffle=False)

    channel_sum = 0.0
    channel_squared_sum = 0.0
    total_pixel_count = 0

    for images, _ in loader:
        batch_pixel_count = images.numel() // images.size(1)
        total_pixel_count += batch_pixel_count

        channel_sum += images.sum(dim=[0,2,3])
        channel_squared_sum += (images ** 2).sum(dim=[0,2,3])

    mean = channel_sum /  total_pixel_count
    std  = (channel_squared_sum / total_pixel_count - mean ** 2) ** 0.5

    return mean.tolist(), std.tolist()

def cifar_datasets():

    raw_train_data = datasets.CIFAR10(
        root='./', 
        train=True, 
        transform=transforms.ToTensor(), 
        download=True
    )

    calculated_mean, calculated_std = calculate_mean_std(raw_train_data)

    train_transforms = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(calculated_mean, calculated_std),
    ])

    test_transforms = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(calculated_mean, calculated_std),
    ])

    train_data = datasets.CIFAR10(
        root='./',
        train=True,
        transform=train_transforms,
        download=True
        )
    
    test_data = datasets.CIFAR10(
        root='./',
        train=False,
        transform=test_transforms,
        download=True
    )
    return train_data, test_data

if __name__=='__main__':
    train_data, test_data = cifar_datasets()

    image, label = train_data[0]
    print(f"image size: {image.size()}")
    print(f'label: {label}')