import torch
from torchvision import models

# Download the pre-trained ResNet18 model
model = models.resnet18(weights=True)

# Change the model to evaluation mode
model.eval()

# Convert the model to TorchScript format
# Option 1: Trace your model using a random input
dummy_input = torch.randn(1, 3, 224, 224)
traced_script_module = torch.jit.trace(model, dummy_input)

# Option 2: Export your model without tracing (faster, but more flexible)
script_module = torch.jit.script(model)

# Save the model in TorchScript format
torch.jit.save(traced_script_module, "resnet18_traced.pt")
# or
torch.jit.save(script_module, "resnet18.pt")
