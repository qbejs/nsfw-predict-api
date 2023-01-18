from pathlib import Path

from fastapi import FastAPI
import opennsfw2 as n2
app = FastAPI()


@app.get("/")
async def root():
    return {"NSFW Predict Api v. PoC"}


@app.get("/poc")
async def say_hello():
    path = Path(__file__).with_name("nsfw.jpg")

    probability = n2.predict_image(str(path))

    return {"Probability: %.2f" % probability}
