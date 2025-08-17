# 🦓 Object Counting with YOLOv8 & FastAPI  

A real-time **object detection and counting system** built with **YOLOv8**, **FastAPI**, and **OpenCV**.  
This project can process both **live video feeds** and **uploaded videos** to count multiple object types such as **animals, faces, and pills**.  

As a demonstration, we use an **aerial video of animals in the wild** 🦒 🐘 🦓 to show the model in action.  

---

## 🚀 Live Demo
Try it out here 👉 [Live on Railway](https://your-railway-app-url-here)  

---

## ✨ Features
- 🎥 Works with **live webcam** or **uploaded videos**
- 🦁 Detects and counts animals, faces, pills, and more
- ⚡ Real-time inference with YOLOv8
- 🛠️ FastAPI backend with clean API routes
- 🌐 Simple HTML + CSS frontend
- 📦 Dockerized for easy deployment
- ☁️ Deployed on Railway for live testing

---

## 📊 Example Demo (Aerial Animals Video)
![Demo Screenshot](assets/demo.gif)  
*Model detecting and counting animals from an aerial video feed.*  

---

## 🛠️ Tech Stack
- **Backend:** FastAPI  
- **Frontend:** HTML + CSS  
- **Computer Vision:** YOLOv8 + OpenCV  
- **Deployment:** Docker + Railway  
- **Testing:** Pytest  

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/your-username/object-counter.git
cd object-counter
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run locally:
```bash
uvicorn app.main:app --reload
```

Visit the app at 👉 `http://127.0.0.1:8000`

---

## 🐳 Run with Docker
Build the image:
```bash
docker build -t object-counter .
```

Run the container:
```bash
docker run -p 8000:8000 object-counter
```

---

## 🧪 Running Tests
```bash
pytest -v
```

---

## 🔮 Future Improvements
- ✅ Add object tracking (DeepSORT/ByteTrack) to prevent double-counting  
- ✅ Train YOLOv8 on a **custom pills dataset**  
- ✅ Enhance frontend with Streamlit or React  

---

## 🙌 Acknowledgements
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Railway](https://railway.app/)  

---

👨‍💻 Built with ❤️ by [Your Name]  
