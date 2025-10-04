# 🕷️ Spider Robot – WiFi-Enabled Quadruped Scouting Robot

A 12-DOF spider-inspired quadruped robot designed for traversing rough terrain and performing remote surveillance during disaster situations. Built using Arduino UNO R4 WiFi, PCA9685 servo driver, ESP32-CAM, and a custom Python GUI for pose control.

---

## 🚀 Features

- 4-legged robot with 3 degrees of freedom per leg
- SolidWorks-designed, 3D-printed PLA body
- Python Tkinter GUI for manual and sequence-based control
- Tripod gait walking via JSON pose playback
- ESP32-CAM integration for live video streaming
- WiFi-based control over local network

---

## 🛠️ Tech Stack

- **Software**: Python · Tkinter · Arduino C++ · JSON
- **Hardware**: Arduino UNO R4 WiFi · PCA9685 · ESP32-CAM · 12× MG996R/SG90
- **Design**: SolidWorks · 3D Printing (PLA)

---

## 📸 Demo

> 📹 [Insert YouTube or Google Drive demo video link here]

---

## 📐 Quantitative Results

- **Stride Length** ≈ 6.84 cm (calculated via swing angle and leg length)
- **Walking Speed** ≈ 8.55 cm/s (0.8s step cycle)
- **Power Usage** ≈ 7.5W (1.5 A × 5V during 6-servo load)

---

## 🧠 Future Enhancements

- Add ultrasonic obstacle detection
- IMU-based gait adaptation and stability
- Autonomous path planning (A*/SLAM)
- Power-efficient gait transitions
- Object/person detection using OpenCV or YOLO

---

## 📁 File Structure
├── walk.py # Main Python GUI for control
├── cam.py # ESP32-CAM video stream viewer
├── poses/ # JSON pose files (start.json to 5.json)
├── Arduino/ # Arduino sketch for servo control
├── servo_positions.json # Saved servo poses
├── images/ # Screenshots, diagrams, etc.
├── LICENSE
└── README.md


---

## 👥 Contributors

- [Shubham Jangle](https://github.com/Shubh131102)  
- Shubham Dehrgave  
- Soumya Mondal

---

## 📜 License

This project is licensed under the MIT License.

---

📂 **Resources:**  
- [Project Presentation (Slides)](docs/Spider%20Robot%20Presentation.pptx)  
- [CAD Files](cad/)  
- [Firmware](firmware/)  
- [Launch Files](launch/) 

