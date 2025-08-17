from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
from ultralytics import YOLO
import cv2

app = FastAPI(title="Object Detection API")

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture(0)


def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        #run Yolo inferences
        results = model(frame)

        #draw detectiom on the frame
        annotated_frame = results[0].plot()

        #encode as jpeg
        ret, buffer = cv2.imencode(".jpg", annotated_frame)
        frame_bytes = buffer.tobytes()
        # Yield frame in MJPEG format
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")


@app.get("/live")
def live_feed():
    return StreamingResponse(generate_frames(),
                             media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/")
def root():
    return {"Hey there": "am up"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

