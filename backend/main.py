from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
from io import BytesIO
from keras.models import model_from_json
from keras.applications.resnet50 import preprocess_input
import base64
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
)


class ImageParams(BaseModel):
    image: str


with open('model/model_architecture (1).json', 'r') as json_file:
    loaded_model_json = json_file.read()

model = model_from_json(loaded_model_json)

model.load_weights('model/model_weights.h5')


def base64_to_pil_image(base64_string):
    try:
        image_data = base64.b64decode(base64_string)
        img = Image.open(BytesIO(image_data))
        return img
    except Exception as e:
        print(f"An exception occurred while converting base64 to image: {e}")
        return None


def preprocess_image(img):
    try:
        img = img.convert("RGB")
        img = img.resize((300, 300))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        return img_array
    except Exception as e:
        print(f"An exception occurred while preprocessing image: {e}")
        return None


@app.post('/classify/')
async def classify_image(params: ImageParams):
    received_image = params.image
    try:
        img = base64_to_pil_image(received_image)
        img.save('image.png')
        if img is not None:
            img_array = preprocess_image(img)
            if img_array is not None:
                prediction = model.predict(img_array)
                prediction = prediction.tolist(),
                return {
                    "abstract": str(prediction[0][0][0]),
                    "cityscape": str(prediction[0][0][1]),
                    "portrait": str(prediction[0][0][2]),
                    "landscape": str(prediction[0][0][3]),
                    "animal-painting": str(prediction[0][0][4])
                }
            else:
                return {"message": "Failed to preprocess the image"}
        else:
            return {"message": "Failed to convert base64 to image"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
