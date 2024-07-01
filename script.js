let mediaRecorder;
let audioChunks = [];
let mediaStream = null;
let wavesurfer = null;

function getMediaStream() {
    if (!mediaStream) {
        return navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                mediaStream = stream;
                return stream;
            })
            .catch(error => {
                console.error('Media devices error:', error);
                throw error;
            });
    }
    return Promise.resolve(mediaStream);
}

document.getElementById('startButton').addEventListener('click', () => {
    getMediaStream().then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const audioUrl = URL.createObjectURL(audioBlob);

            // Wavesurfer setup
            if (!wavesurfer) {
                wavesurfer = WaveSurfer.create({
                    container: '#waveform',
                    waveColor: '#007bff',
                    progressColor: '#4a90e2'
                });
            }
            wavesurfer.load(audioUrl);

            document.getElementById('playPauseButton').disabled = false;

            // Audio upload setup
            const formData = new FormData();
            formData.append('audio', audioBlob, 'recording.wav');

            fetch('http://localhost:5000/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').innerText = 'Başarıyla yüklendi: ' + data.message;
            })
            .catch(error => {
                document.getElementById('result').innerText = 'Hata: ' + error;
            });

            audioChunks = [];
        };

        document.getElementById('startButton').disabled = true;
        document.getElementById('stopButton').disabled = false;
    });
});

document.getElementById('stopButton').addEventListener('click', () => {
    mediaRecorder.stop();
    document.getElementById('startButton').disabled = false;
    document.getElementById('stopButton').disabled = true;
});

document.getElementById('playPauseButton').addEventListener('click', () => {
    if (wavesurfer) {
        wavesurfer.playPause();
    }
});