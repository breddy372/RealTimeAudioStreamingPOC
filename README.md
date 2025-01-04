# Real-Time Noise Cancellation System

This project implements a real-time noise cancellation system using spectral gating. The system processes audio in real-time, allowing users to record or upload audio files, apply noise cancellation, and download the processed audio.

## Features

- **Real-Time Processing**: Capture audio from a microphone and process it in real-time.
- **Noise Cancellation**: Use spectral gating to reduce noise in audio files.
- **File Upload**: Upload audio files for processing.
- **Download Processed Audio**: Download the noise-cancelled audio file.
![image](https://github.com/user-attachments/assets/c7519c2f-0730-4c11-8e5d-1c745456e053)


## Project Structure

real_time_noise_cancellation/
│
├── src/
│ ├── init.py
│ ├── main.py
│ ├── audio_processing.py
│ ├── noise_cancellation.py
│ ├── utils.py
│ ├── logger.py
│ └── api.py
│
├── frontend/
│ ├── index.html
│ └── static/
│ ├── style.css
│ └── script.js
│
├── data/
│ └── output.wav
│
├── requirements.txt
├── Dockerfile
└── README.md



## Setup Instructions

### Prerequisites

- Python 3.9 or later
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/real-time-noise-cancellation.git
   cd real-time-noise-cancellation


2. **Create a Virtual Environment**
     ```bash
     python -m venv venv

3. **Activate the Virtual Environment**
     ```bash
     .\venv\Scripts\activate
     
4. **Install Dependencies**
     ```bash
     pip install -r requirements.txt
5. **Create a Virtual Environment**
     ```bash
     python -m venv venv


### Running the application

1. **Run Locally**
    ```bash
    python src/main.py
  Access the application at http://localhost:8000.

2. **Run with Docker**

- Build the Docker Image
  ```bash
  docker build -t real-time-noise-cancellation .
- Run the Docker Container
  ```bash
  docker run -p 8000:80 real-time-noise-cancellation
Access the application at http://localhost:8000.


## Usage
Record Audio: Click the "Record" button to capture audio from your microphone.
Upload Audio: Use the file input to upload an audio file for processing.
Download Processed Audio: After processing, download the noise-cancelled audio file.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact bhargavreddy483@gmail.com.
   
