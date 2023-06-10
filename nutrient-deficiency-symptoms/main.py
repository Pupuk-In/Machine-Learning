import os
import uvicorn
import traceback
import tensorflow as tf

from pydantic import BaseModel
from urllib.request import Request
from fastapi import FastAPI, Response, UploadFile, File
from utils import load_image_into_numpy_array

model = tf.keras.models.load_model('./my_model.h5')

app = FastAPI()

@app.get("/")
def index():
    return "Hello world endpoint!"

@app.post("/predict_image")
def predict_image(uploaded_file: UploadFile, response: Response):
    try:
        # Checking if it's an image
        if uploaded_file.content_type not in ["image/jpeg", "image/png"]:
            response.status_code = 400
            return "File is Not an Image"
        
        image = load_image_into_numpy_array(uploaded_file.file.read())
        print("Image shape:", image.shape)
        
        pp_input = preprocessing.image.load_img(uploaded_file.file_name, target_size=(224, 224))
        pp_input = tf.expand_dims(pp_input, axis=0)
        result = model.predict(pp_input)
        
        return "Insert result here"
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return "Internal Server Error"

port = os.environ.get("PORT", 8080)
print(f"Listening to http://0.0.0.0:{port}")

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0',port=port)