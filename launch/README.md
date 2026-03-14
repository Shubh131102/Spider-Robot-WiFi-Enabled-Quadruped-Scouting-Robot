# Arduino Firmware — 12-DOF Quadruped Robot

Main controller firmware handling servo control, inverse kinematics, 
gait generation, and serial communication.

---

## Quick Start

1. Install Arduino IDE and required libraries
2. Open main/main.ino
3. Select Board: Arduino UNO R4
4. Select Port: /dev/ttyACM0 (Linux) or COM3 (Windows)
5. Upload and open Serial Monitor at 115200 baud

---

## Required Libraries

- Adafruit PWM Servo Driver Library
- Wire (built-in)

Install via Arduino IDE: Tools → Manage Libraries → Search "Adafruit PWM Servo"

---

## Features

- 50Hz servo control loop with smooth interpolation
- Inverse kinematics solver (<1ms per leg)
- Multiple gait patterns: walk, trot, crawl
- Serial command interface
- Safety limits: max 30° angle change per update

---

## Pin Connections

| Arduino | PCA9685 / ESP32 |
|---------|----------------|
| A4 (SDA) | SDA (PCA9685) |
| A5 (SCL) | SCL (PCA9685) |
| D1 (TX)  | RX (ESP32)    |
| D0 (RX)  | TX (ESP32)    |

---

## Serial Commands

Format: COMMAND:VALUE
```
GAIT:walk       Set walk gait
GAIT:trot       Set trot gait
GAIT:crawl      Set crawl gait
SPEED:1.5       Set speed multiplier
MOVE:50,0       Move forward, turn
STOP            Emergency stop
STATUS          Request system status
```

---

## Notes

- Test with robot suspended before floor operation
- Calibrate servos before first use
- Monitor servo temperatures during extended use
