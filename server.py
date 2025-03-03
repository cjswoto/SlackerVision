from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack
import eventlet
import cv2

eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

pcs = set()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('offer')
def handle_offer(data):
    async def process_offer():
        pc = RTCPeerConnection()
        pcs.add(pc)

        @pc.on('icecandidate')
        def on_icecandidate(candidate):
            emit('candidate', {'candidate': candidate.to_json()})

        @pc.on('track')
        def on_track(track):
            if (track.kind == 'video'):
                local_video = VideoStreamTrack()
                pc.addTrack(local_video)

        offer = RTCSessionDescription(sdp=data['sdp'], type=data['type'])
        await pc.setRemoteDescription(offer)

        answer = await pc.createAnswer()
        await pc.setLocalDescription(answer)

        emit('answer', {'sdp': pc.localDescription.sdp, 'type': pc.localDescription.type})

    eventlet.spawn_n(process_offer)

@socketio.on('candidate')
def handle_candidate(data):
    async def process_candidate():
        candidate = RTCIceCandidate(sdp=data['candidate']['sdp'], sdpMid=data['candidate']['sdpMid'], sdpMLineIndex=data['candidate']['sdpMLineIndex'])
        await pcs[-1].addIceCandidate(candidate)

    eventlet.spawn_n(process_candidate)

if __name__ == '__main__':
    socketio.run(app, debug=True)
