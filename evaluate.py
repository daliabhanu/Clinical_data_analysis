import torch

def evaluate_model(model, test_loader):
    model.eval()
    correct_predictions = 0
    total_predictions = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 2)
            total_predictions += labels.view(-1).size(0)
            correct_predictions += (predicted == labels).sum().item()

    accuracy = correct_predictions / total_predictions
    print(f"Accuracy on test data: {accuracy:.2f}")
