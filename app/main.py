from fastapi import FastAPI, File, UploadFile, HTTPException

import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
