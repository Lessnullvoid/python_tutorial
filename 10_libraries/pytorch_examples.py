# PyTorch Examples
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

class SimpleNN(nn.Module):
    """Simple neural network for MNIST classification"""
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )
    
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

def basic_tensor_operations():
    """Demonstrate basic tensor operations"""
    print("Basic Tensor Operations:")
    
    # Create tensors
    x = torch.tensor([[1, 2], [3, 4]])
    y = torch.tensor([[5, 6], [7, 8]])
    
    print(f"Tensor x:\n{x}")
    print(f"Tensor y:\n{y}")
    
    # Basic operations
    print(f"\nAddition:\n{x + y}")
    print(f"Multiplication:\n{x * y}")
    print(f"Matrix multiplication:\n{torch.matmul(x, y)}")
    
    # GPU availability
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"\nUsing device: {device}")
    x = x.to(device)

def train_mnist_model():
    """Train a simple neural network on MNIST dataset"""
    # Load and transform MNIST dataset
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    trainset = torchvision.datasets.MNIST(
        root='./data', train=True, download=True, transform=transform
    )
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=64, shuffle=True
    )
    
    # Create model, loss function, and optimizer
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = SimpleNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    
    # Training loop
    print("\nTraining MNIST model:")
    for epoch in range(2):  # Just 2 epochs for demonstration
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data[0].to(device), data[1].to(device)
            
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            if i % 100 == 99:
                print(f"[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 100:.3f}")
                running_loss = 0.0
    
    print("Finished Training")
    return model

def visualize_predictions(model):
    """Visualize some predictions on test data"""
    # Load test data
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    
    testset = torchvision.datasets.MNIST(
        root='./data', train=False, download=True, transform=transform
    )
    testloader = torch.utils.data.DataLoader(
        testset, batch_size=4, shuffle=True
    )
    
    # Get some test images
    dataiter = iter(testloader)
    images, labels = next(dataiter)
    
    # Make predictions
    device = "cuda" if torch.cuda.is_available() else "cpu"
    outputs = model(images.to(device))
    _, predicted = torch.max(outputs, 1)
    
    # Plot images and predictions
    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    for i in range(4):
        axes[i].imshow(images[i].squeeze(), cmap='gray')
        axes[i].set_title(f'Pred: {predicted[i].item()}')
        axes[i].axis('off')
    plt.show()

def save_and_load_model(model):
    """Demonstrate model saving and loading"""
    print("\nSaving and loading model:")
    
    # Save model
    torch.save(model.state_dict(), "mnist_model.pth")
    print("Model saved")
    
    # Load model
    new_model = SimpleNN()
    new_model.load_state_dict(torch.load("mnist_model.pth"))
    new_model.eval()
    print("Model loaded")

if __name__ == "__main__":
    basic_tensor_operations()
    model = train_mnist_model()
    visualize_predictions(model)
    save_and_load_model(model) 