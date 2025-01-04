let mediaRecorder;
let audioChunks = [];

document.getElementById('recordButton').addEventListener('click', async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
    };

    mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        audioChunks = [];
        const formData = new FormData();
        formData.append('file', audioBlob, 'recording.wav');

        const response = await fetch('/process-audio', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            const audioElement = document.getElementById('processedAudio');
            audioElement.src = url;
            audioElement.style.display = 'block';
        } else {
            alert("Failed to process audio.");
        }
    };

    document.getElementById('recordButton').disabled = true;
    document.getElementById('stopButton').disabled = false;
});

document.getElementById('stopButton').addEventListener('click', () => {
    mediaRecorder.stop();
    document.getElementById('recordButton').disabled = false;
    document.getElementById('stopButton').disabled = true;
});

async function uploadAudio() {
    const fileInput = document.getElementById('audioFile');
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select an audio file.");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/process-audio', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        const audioElement = document.getElementById('processedAudio');
        audioElement.src = url;
        audioElement.style.display = 'block';
    } else {
        alert("Failed to process audio.");
    }
}