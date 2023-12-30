# Art-Genre-Classifier
Classifies art genre (abstract, landscape, portrait, etc...)
- with 87.19% accuracy when classifying b/w 5 classes
- with 97.03% accuracy when classifying b/w 3 classes

# Technique
We are using transfer learning in this. The Resnet 152 is used as the base model, the last 30 layers are trained according to the current dataset, finetuning the model according to out dataset, and the other untrainable layers of the model are trained on the imagenet dataset.

# Limitations
We only had access to 30GB RAM, and due to that, we were only able to train the model on 10000 items, 2000 from each class.


##### Note: The repo doesn't contain the model weights, because of GitHub size limitations (Max model size = 100MBs, Our model weights = 246MBs), if you need the model weights, open an issue on this repo and I'll contact you, and send the model weights
