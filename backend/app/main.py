import random
from typing import Annotated

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    alpha: float
    delta: float
    u: float
    g: float
    r: float
    i: float
    z: float
    redshift: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "alpha": 1.0,
                    "delta": 1.0,
                    "u": 1.0,
                    "g": 1.0,
                    "r": 1.0,
                    "i": 1.0,
                    "z": 1.0,
                    "redshift": 1.0,
                }
            ]
        }
    }


classes = ["GALAXY", "STAR", "QSO"]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/analyzer/object-input/")
def object_input(item: Item):
    print(item)
    return random.choice(classes)


@app.post("/analyzer/image-input/")
def image_input(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    return {"filename": file.filename}
