# Documentation — 12-DOF Quadruped Robot

Technical documentation covering mechanical design, inverse kinematics, 
gait planning, control architecture, and performance results.

---

## Contents

- Technical_Report.pdf — Complete project documentation and analysis
- Assembly_Instructions.pdf — Step-by-step assembly and wiring guide
- User_Manual.pdf — Operation, control interface, and troubleshooting
- presentation.pdf — Project overview, design process, and results

---

## Project Overview

12-DOF quadruped robot designed for stable locomotion on uneven terrain 
featuring FEA-optimized leg structures, servo-driven gait control, and 
WiFi-based remote operation with live video streaming.

Hardware stack:
- Arduino UNO R4 WiFi — Main controller
- PCA9685 — 16-channel PWM servo driver
- 12x MG90S/MG996R servos — Actuation
- ESP32-CAM — Vision and WiFi control
- 7.4V LiPo battery with BEC

---

## Inverse Kinematics

Kinematic chain per leg:
Body → Hip (θ₁, yaw) → Thigh (θ₂, pitch) → Knee (θ₃, pitch) → Foot

Link lengths: L₁ = 30mm | L₂ = 60mm | L₃ = 80mm

Joint angle solutions:

θ₁ = atan2(y, x)
θ₃ = acos((D² - L₂² - L₃²) / (2·L₂·L₃))
θ₂ = atan2(z, r) + acos((L₂² + D² - L₃²) / (2·L₂·D))

Workspace:
- Radial reach: ~150mm
- Height range: 40–120mm
- Hip rotation: ±45°

IK computation time: <1ms per leg

---

## Gait Patterns

| Gait  | Legs Grounded | Duty Cycle | Use Case |
|-------|--------------|------------|----------|
| Walk  | 3 of 4       | 75%        | Stable flat terrain |
| Trot  | 2 of 4       | 50%        | Faster movement |
| Crawl | 3-4 of 4     | 90%        | Rough terrain, inclines |

Walk sequence — one leg lifts per step:
LF → RF → LH → RH

Trot pairs — diagonal legs move together:
Pair 1: LF + RH | Pair 2: RF + LH

---

## System Architecture

User Command (WiFi/Serial)
        ↓
Arduino UNO R4 (Gait + IK computation)
        ↓ I2C
PCA9685 PWM Driver
        ↓
12 Servo Actuators

ESP32-CAM handles WiFi communication and video streaming in parallel.

---

## Performance Results

| Metric           | Value        |
|-----------------|--------------|
| Walking Speed   | 5–10 cm/s    |
| Step Height     | 20–40mm      |
| Stride Length   | 30–60mm      |
| IK Computation  | <1ms per leg |
| Control Rate    | 50Hz         |
| Total Weight    | ~850g        |
| Battery Life    | 30–60 min    |

IK accuracy: <2mm position error | <2° joint angle error
Crawl gait stable on 15° inclines

---

## Control Interface

WiFi Web Interface:
1. Connect to "SpiderBot" WiFi network
2. Open browser: http://192.168.4.1
3. Controls: joystick, gait selection, speed slider, camera feed, e-stop

Serial command protocol:
- GAIT:walk — Set gait mode
- SPEED:1.5 — Set speed multiplier
- MOVE:100,0 — Forward/turn command
- STOP — Emergency stop

Python GUI:
python python_gui/control_panel.py

---

## Bill of Materials

| Part                  | Qty | Est. Cost |
|-----------------------|-----|-----------|
| MG90S/MG996R Servo    | 12  | ~$24      |
| PCA9685 PWM Driver    | 1   | ~$8       |
| Arduino UNO R4 WiFi   | 1   | ~$27      |
| ESP32-CAM             | 1   | ~$10      |
| 7.4V LiPo Battery     | 1   | ~$15      |
| BEC (5V/3A)           | 1   | ~$5       |
| Hardware/Screws       | -   | ~$10      |
| PLA Filament (~400g)  | -   | ~$8       |

Total estimated cost: ~$107 USD

---

## Assembly Time Estimates

- 3D Printing: ~38 hours
- Mechanical Assembly: 4–6 hours
- Wiring: 2–3 hours
- Programming: 1–2 hours
- Testing and Calibration: 2–4 hours

---

## Future Improvements

- IMU integration for active balance control
- Ultrasonic sensors for obstacle avoidance
- Autonomous navigation with SLAM
- Adaptive gait learning via reinforcement learning
- Carbon fiber legs for weight reduction

---

## Contact

Shubham Jangle
Email: sjang041@ucr.edu
GitHub: github.com/Shubh131102
LinkedIn: linkedin.com/in/shubham-jangle-43081b27a
