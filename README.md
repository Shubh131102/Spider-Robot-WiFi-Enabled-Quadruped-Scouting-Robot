# 12-DOF Quadruped Robot — Mechanical Design & Fabrication

A 12-DOF quadruped robot designed for traversing rough and uneven terrain, 
featuring FEA-optimized leg structures, servo-driven gait control, thermal 
management solutions, and WiFi-based remote operation with live video streaming.

---

## Key Results
- **25% stiffness-to-weight improvement** via ANSYS FEA-driven leg geometry iteration
- **Walking Speed** ≈ 8.55 cm/s (0.8s step cycle)
- **Stride Length** ≈ 6.84 cm (calculated via swing angle and leg length)
- **Power Usage** ≈ 7.5W (1.5A × 5V during 6-servo load)
- Successfully demonstrated stable locomotion on uneven terrain with hip 
adduction for lateral balance

---

## Mechanical Design
- Designed chassis and articulated leg linkages in **SolidWorks**
- Iterated leg geometry through **ANSYS FEA** — removed material from 
low-stress regions, reinforced high-stress areas achieving 25% 
stiffness-to-weight improvement
- Selected 12 servo actuators based on torque requirements derived from 
leg geometry and weight analysis
- Resolved thermal buildup by redesigning chassis geometry to improve 
heat dissipation
- Implemented hip adduction mechanism for lateral balance during locomotion
- Diagnosed and resolved voltage sag causing Arduino resets by upgrading 
power wiring gauge
- Manufactured 12 3D printed PLA leg components across 4 legs through 
multi-iteration fabrication

---

## Features
- 12-DOF — 3 degrees of freedom per leg across 4 legs
- SolidWorks-designed, 3D-printed PLA body
- Python Tkinter GUI for manual and sequence-based control
- Tripod gait walking via JSON pose playback
- ESP32-CAM integration for live video streaming
- WiFi-based control over local network
- Hip adduction for lateral stability on uneven terrain

---

## Tech Stack
- **Mechanical:** SolidWorks · ANSYS FEA · 3D Printing (PLA)
- **Software:** Python · Tkinter · Arduino C++ · JSON
- **Hardware:** Arduino UNO R4 WiFi · PCA9685 · ESP32-CAM · 12× MG996R/SG90
- **Control:** Servo Control · Tripod Gait · WiFi Communication

---

## File Structure
├── walk.py                 # Main Python GUI for control
├── cam.py                  # ESP32-CAM video stream viewer
├── poses/                  # JSON pose files (start.json to 5.json)
├── Arduino/                # Arduino sketch for servo control
├── servo_positions.json    # Saved servo poses
├── cad/                    # SolidWorks CAD files
├── images/                 # Screenshots, diagrams, photos
├── LICENSE
└── README.md

---

## Future Enhancements
- IMU-based gait adaptation and stability
- Autonomous path planning (A*/SLAM)
- Ultrasonic obstacle detection
- Object/person detection using OpenCV or YOLO
- Power-efficient gait transitions

---

## Contributors
- [Shubham Jangle](https://github.com/Shubh131102)
- Shubham Dehrgave
- Soumya Mondal

---

## License
This project is licensed under the MIT License.

---

**Resources:**
- [Project Presentation](docs/Spider%20Robot%20Presentation.pptx)
- [CAD Files](cad/)
- [Firmware](Arduino/)
