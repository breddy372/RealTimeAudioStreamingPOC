import uvicorn
from logger import app_logger

def main():
    app_logger.info("Starting the FastAPI server...")
    uvicorn.run("api:app", host="0.0.0.0", port=80, reload=True)

if __name__ == "__main__":
    main()