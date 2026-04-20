from fastapi import FastAPI, UploadFile, File
import httpx
import os

app = FastAPI(title="FraudBlock Backend")

HF_SPACE_URL = os.getenv("HF_SPACE_URL", "https://baybus-fraudblock-ml.hf.space")

@app.get("/")
async def root():
          return {"message": "FraudBlock Backend is running", "hf_url": HF_SPACE_URL}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
          if not HF_SPACE_URL:
                        return {"error": "HF_SPACE_URL environment variable not set"}
                    return {
                                  "filename": file.filename,
                                  "status": "received",
                                  "hf_url": HF_SPACE_URL,
                                  "note": "Proxying to HF Space..."
                    }
