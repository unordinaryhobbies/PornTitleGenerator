from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import markovify

#Load model
def load_model():
    with open('model.json', 'r') as f:
        titleGenModel = markovify.Text.from_json(f.read())
    return titleGenModel

def generate_title(model: markovify.Text):
    return model.make_sentence()

# Create the application instance
app = FastAPI()
model = load_model()


@app.get("/title")
def get_title():
    return {'title' : generate_title(model)}

app.mount("/", StaticFiles(directory="assets", html = True), name="assets")