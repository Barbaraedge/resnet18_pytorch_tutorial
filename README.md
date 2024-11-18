# ResNet18 Pytorch Tutorial for Barbara Platform

## Deploy and Serve a Deep Learning Model on the Edge

This tutorial guides you through deploying a pre-trained ResNet18 model for image classification on a Barbara Platform Edge Node. You'll learn how to:

1) **Download and Convert the Model**: Use the provided `resnet_torchscript_export.py` script to download the ResNet18 model and save it in a format optimized for edge deployment (TorchScript).
2) **Upload the Model to Barbara Library and serve it in a node**: Upload the converted ResNet18 model to your Barbara edge node for serving.
3) **Perform Inference**: Run inference requests using the REST API to classify images stored in the `images` folder. Utilize the provided `synset.txt` file for model label interpretation.

## Detailed Explanation

For a comprehensive step-by-step walkthrough, refer to the dedicated article on our Academy Platform: (Link to the article).

## Resources

PyTorch ResNet18 Model Reference: https://pytorch.org/hub/pytorch_vision_resnet/

## Note

This repository contains the necessary scripts for model conversion and potentially additional resources relevant to the tutorial on the Academy platform.
