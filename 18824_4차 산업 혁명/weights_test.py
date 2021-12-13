import torch


model_state_dict = torch.load('./model/CNN.pth')

with open('weights.txt', 'w') as f:
    for layer in model_state_dict:
        f.write(f'layer: {layer}\n')
        f.write(f'weight: {model_state_dict[layer].tolist()}\n')
