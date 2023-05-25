
import numpy as np
from torchvision import models, datasets, transforms
import torch, os
from PIL import Image

def image_preprocessing(img_pth):
	
	pil_image = Image.open(img_pth)
	
	if pil_image.size[0] > pil_image.size[1]:
		pil_image.thumbnail((10000000, 256))
	else:
		pil_image.thumbnail((256, 100000000))
	
	left_margin = (pil_image.width - 224) / 2
	bottom_margin = (pil_image.height - 224) / 2
	right_margin = left_margin + 224
	top_margin = bottom_margin + 224
	
	pil_image = pil_image.crop((left_margin, bottom_margin, right_margin, top_margin))
	
	np_image = np.array(pil_image) / 255
	mean = np.array([0.485, 0.456, 0.406])
	std = np.array([0.229, 0.224, 0.225])
	np_image = (np_image -mean) / std
	
	np_image = np_image.transpose([2, 0, 1])
	
	return np_image


def load_model(chkpt_path):
    chkpt = torch.load(chkpt_path, map_location=torch.device('cpu'))
    model = models.vgg19(pretrained = True)
    for params in model.parameters():
        params.requires_grad = False
    model.classifier = chkpt['classifier']
    model.load_state_dict(chkpt['state_dict'])
	
    return model

def predict(image_path, model, idx_class_mapping, device, topk=5):
    model.to(device)
    model.eval()
    img = image_preprocessing(image_path)
    img = np.expand_dims(img, axis=0)
    img_tensor = torch.from_numpy(img).type(torch.FloatTensor).to(device)
    
    with torch.no_grad():
        log_probabilities = model.forward(img_tensor)
    
    probabilities = torch.exp(log_probabilities)
    probs, indices = probabilities.topk(topk)

    probs = probs.numpy().squeeze()
    indices = indices.numpy().squeeze()
    classes = [idx_class_mapping[index] for index in indices]
    
    return probs, classes


import config.settings as settings
import json

def image_mache(imgpath):
    deviceFlag = torch.device('cpu')
    # 꽃이미지 디렉토리 ex.static/img/flowers
    data_dir = "static/flowers"
    training_transforms = transforms.Compose([
        transforms.RandomRotation(30),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(), 
        transforms.Normalize([0.485, 0.456, 0.406], 
                            [0.229, 0.224, 0.225])
    ])
    
    training_imagefolder = datasets.ImageFolder(data_dir, transform = training_transforms)
    with open('flower_to_name.json', 'r') as f:
        flower_to_name = json.load(f)
    class_idx_mapping = training_imagefolder.class_to_idx
    idx_class_mapping = {v: k for k, v in class_idx_mapping.items()}
    
    img_path = "media/"+str(imgpath)
    
    model = settings.AI_MODEL
    
    probs, classes = predict(image_path=img_path, model=model, device=deviceFlag, idx_class_mapping=idx_class_mapping)
    class_names = [flower_to_name[c] for c in classes]
    
    flower_match = {}
    probs_end = []
    for i in probs:
        probs_end.append(i)
    for i, name in enumerate(class_names):
        flower_match[name] = int(probs_end[i]*100)

    return flower_match