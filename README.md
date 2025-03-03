# WebRTC Flask Server

A WebRTC-powered Flask application using Flask-SocketIO and aiortc to enable real-time video communication between peers.

## Features
- Web-based real-time video streaming
- WebRTC signaling with Flask-SocketIO
- Handles ICE candidates for peer connection
- Event-driven, using `eventlet` for async support

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pip` (Python package manager)
- WebRTC-compatible browser (Chrome, Firefox, Edge)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```sh
   python server.py
   ```
2. Open a web browser and navigate to:
   ```sh
   http://localhost:5000
   ```
3. Connect two peers and establish a video call.

## Project Structure
```
├── server.py        # Flask backend server handling WebRTC signaling
├── templates/
│   ├── index.html  # Frontend UI for WebRTC peer connection
└── requirements.txt # Project dependencies
```

## Troubleshooting
- **WebRTC connection fails**: Ensure that both peers can access the signaling server.
- **Camera not working**: Check browser permissions and try restarting the app.
- **ICE candidates not exchanged**: Verify that the signaling server is running properly.

## Future Enhancements
- Add support for audio streaming
- Implement room-based multiple user connections
- Improve UI/UX for better user experience

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---
Maintained by [Your Name](https://github.com/YOUR_USERNAME).
