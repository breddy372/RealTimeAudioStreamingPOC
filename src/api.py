from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse, HTMLResponse
import numpy as np
import io
import soundfile as sf
from noise_cancellation import remove_noise
from logger import app_logger

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Serve the frontend HTML page
    with open("frontend/index.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)

import os

@app.post("/process-audio")
async def process_audio(file: UploadFile = File(...)):
    app_logger.info("Audio processing endpoint accessed")
    try:
        audio_data, samplerate = sf.read(file.file)
        noise_clip = audio_data[:samplerate]  # Assume first second is noise
        processed_data = remove_noise(audio_data, noise_clip)
        
        # Ensure the data directory exists
        os.makedirs("../data", exist_ok=True)
        
        # Save the processed audio to a file
        output_path = "../data/output.wav"
        sf.write(output_path, processed_data, samplerate)
        
        buffer = io.BytesIO()
        sf.write(buffer, processed_data, samplerate, format='WAV')
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="audio/wav")
    except Exception as e:
        app_logger.error(f"Error processing audio: {e}")
        return {"error": "Failed to process audio"}
@app.get("/download-audio")
async def download_audio():
    return FileResponse("data/output.wav", media_type="audio/wav", filename="output.wav")

from fastapi.staticfiles import StaticFiles

# Mount the static files directory
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")