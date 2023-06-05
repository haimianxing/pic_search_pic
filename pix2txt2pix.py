from transformers import AutoImageProcessor, ResNetForImageClassification
import torch
from PIL import Image
from io import BytesIO
from utils import gen_pic

def recognize_image(input,model_path):
    with open(input,'rb') as f:
        img_data = f.read()
    img = Image.open(BytesIO(img_data)).convert('RGB')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    jpg_data = buffered.getvalue()
    img_jpg = Image.open(BytesIO(jpg_data))
    image = img_jpg.resize((224, 224))
    processor = AutoImageProcessor.from_pretrained(model_path)
    model = ResNetForImageClassification.from_pretrained(model_path)
    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_label = logits.argmax(-1).item()
    des = model.config.id2label[predicted_label]
    gen_pic(des)

