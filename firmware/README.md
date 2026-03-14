# Firmware — 12-DOF Quadruped Robot

Arduino and ESP32 firmware for servo control, inverse kinematics, 
gait generation, and WiFi-based remote operation.

---

## File Structure

firmware/
├── arduino/
│   ├── main/
│   │   ├── main.ino
│   │   ├── config.h
│   │   ├── servo_control.cpp/.h
│   │   ├── kinematics.cpp/.h
│   │   ├── gait.cpp/.h
│   │   └── communication.cpp
│   └── libraries/
│       ├── Adafruit_PWMServoDriver/
│       └── ArduinoJson/
└── esp32/
    └── camera_webserver/
        ├── camera_webserver.ino
        ├── camera_pins.h
        └── app_httpd.cpp

---

## Arduino Firmware

Main controller: Arduino UNO R4 WiFi

Responsibilities:
- Servo control via PCA9685 over I2C
- Inverse kinematics computation (<1ms per leg)
- Gait pattern generation and execution
- Serial communication with ESP32

Key modules:

| File | Responsibility |
|------|---------------|
| main.ino | Setup and 50Hz control loop |
| servo_control | PCA9685 PWM driver and interpolation |
| kinematics | IK/FK solver |
| gait | Gait pattern generator |
| communication | Serial protocol handler |

Control loop runs at 50Hz with smooth interpolation 
across 10 steps between target poses.

---

## ESP32 Firmware

Module: ESP32-CAM

Responsibilities:
- WiFi Access Point (SSID: SpiderBot)
- Camera video streaming
- Web server control interface
- WebSocket communication
- Command relay to Arduino via Serial

Default IP: 192.168.4.1

---

## Serial Command Protocol

Format: COMMAND:VALUE\n

| Command | Example      | Description           |
|---------|-------------|-----------------------|
| GAIT    | GAIT:walk   | Set gait pattern      |
| SPEED   | SPEED:1.5   | Set speed multiplier  |
| MOVE    | MOVE:100,0  | Forward, turn values  |
| POSE    | POSE:90,90,90 | Set all joints      |
| STOP    | STOP        | Emergency stop        |
| STATUS  | STATUS      | Request status        |

---

## Building and Uploading

### Arduino

Requirements:
- Arduino IDE 1.8.19+
- Adafruit PWM Servo Driver Library
- ArduinoJson Library

Steps:
1. Open firmware/arduino/main/main.ino
2. Select Board: Arduino UNO R4
3. Select Port: /dev/ttyACM0 (Linux) or COM3 (Windows)
4. Upload

### ESP32-CAM

Requirements:
- Arduino IDE with ESP32 board support
- Board package: https://dl.espressif.com/dl/package_esp32_index.json

Steps:
1. Select Board: AI Thinker ESP32-CAM
2. Connect FTDI programmer: GND-GND, 5V-5V, TX-RX, RX-TX
3. Bridge IO0 to GND for programming mode
4. Upload
5. Remove IO0-GND bridge
6. Press RESET

---

## Key Implementation Details

### Servo Interpolation

Smooth movement via angle interpolation:
- Max angle change per update: 30°
- Interpolation steps: 10
- Update rate: 50Hz

Pulse width formula:
pulse = 150 + (angle * 2.5)
Range: 150 (0°) → 307 (90°) → 600 (180°)

### Inverse Kinematics

Solves per-leg joint angles given target foot position:

θ₁ = atan2(y, x)                          // Hip yaw
θ₃ = acos((D² - L₂² - L₃²) / 2L₂L₃)    // Knee
θ₂ = atan2(z, r) + acos(...)              // Thigh

Returns false if target is out of workspace (>170mm reach).

---

## Testing

Servo test — sweep single channel:
```cpp
servos.setAngle(channel, 0);   delay(1000);
servos.setAngle(channel, 90);  delay(1000);
servos.setAngle(channel, 180); delay(1000);
```

IK test — verify foot position solving:
```cpp
Vector3 target = {100, 0, -80};
LegAngles angles;
bool success = ik.solveIK(target, angles);
```

---

## Troubleshooting

Servo not moving:
- Check PCA9685 I2C address (default 0x40)
- Verify power supply voltage (7.4V)
- Confirm correct channel mapping in config.h

Unstable movement:
- Reduce speed multiplier
- Increase interpolation steps
- Check battery voltage under load

ESP32 not connecting:
- Verify SSID "SpiderBot" is visible
- Default IP: 192.168.4.1
- Confirm ESP32 is in AP mode

---

## Notes

- Always test with robot suspended before floor operation
- Calibrate servos before first use
- Monitor servo temperatures during extended operation
- Start with slow speeds before increasing
Responsibilities:
- Servo control via PCA9685 over I2C
- Inverse kinematics computation (<1ms per leg)
- Gait pattern generation and execution
- Serial communication with ESP32

Key modules:

| File | Responsibility |
|------|---------------|
| main.ino | Setup and 50Hz control loop |
| servo_control | PCA9685 PWM driver and interpolation |
| kinematics | IK/FK solver |
| gait | Gait pattern generator |
| communication | Serial protocol handler |

Control loop runs at 50Hz with smooth interpolation 
across 10 steps between target poses.

---

## ESP32 Firmware

Module: ESP32-CAM

Responsibilities:
- WiFi Access Point (SSID: SpiderBot)
- Camera video streaming
- Web server control interface
- WebSocket communication
- Command relay to Arduino via Serial

Default IP: 192.168.4.1

---

## Serial Command Protocol

Format: COMMAND:VALUE\n

| Command | Example      | Description           |
|---------|-------------|-----------------------|
| GAIT    | GAIT:walk   | Set gait pattern      |
| SPEED   | SPEED:1.5   | Set speed multiplier  |
| MOVE    | MOVE:100,0  | Forward, turn values  |
| POSE    | POSE:90,90,90 | Set all joints      |
| STOP    | STOP        | Emergency stop        |
| STATUS  | STATUS      | Request status        |

---

## Building and Uploading

### Arduino

Requirements:
- Arduino IDE 1.8.19+
- Adafruit PWM Servo Driver Library
- ArduinoJson Library

Steps:
1. Open firmware/arduino/main/main.ino
2. Select Board: Arduino UNO R4
3. Select Port: /dev/ttyACM0 (Linux) or COM3 (Windows)
4. Upload

### ESP32-CAM

Requirements:
- Arduino IDE with ESP32 board support
- Board package: https://dl.espressif.com/dl/package_esp32_index.json

Steps:
1. Select Board: AI Thinker ESP32-CAM
2. Connect FTDI programmer: GND-GND, 5V-5V, TX-RX, RX-TX
3. Bridge IO0 to GND for programming mode
4. Upload
5. Remove IO0-GND bridge
6. Press RESET

---

## Key Implementation Details

### Servo Interpolation

Smooth movement via angle interpolation:
- Max angle change per update: 30°
- Interpolation steps: 10
- Update rate: 50Hz

Pulse width formula:
pulse = 150 + (angle * 2.5)
Range: 150 (0°) → 307 (90°) → 600 (180°)

### Inverse Kinematics

Solves per-leg joint angles given target foot position:

θ₁ = atan2(y, x)                          // Hip yaw
θ₃ = acos((D² - L₂² - L₃²) / 2L₂L₃)    // Knee
θ₂ = atan2(z, r) + acos(...)              // Thigh

Returns false if target is out of workspace (>170mm reach).

---

## Testing

Servo test — sweep single channel:
```cpp
servos.setAngle(channel, 0);   delay(1000);
servos.setAngle(channel, 90);  delay(1000);
servos.setAngle(channel, 180); delay(1000);
```

IK test — verify foot position solving:
```cpp
Vector3 target = {100, 0, -80};
LegAngles angles;
bool success = ik.solveIK(target, angles);
```

---

## Troubleshooting

Servo not moving:
- Check PCA9685 I2C address (default 0x40)
- Verify power supply voltage (7.4V)
- Confirm correct channel mapping in config.h

Unstable movement:
- Reduce speed multiplier
- Increase interpolation steps
- Check battery voltage under load

ESP32 not connecting:
- Verify SSID "SpiderBot" is visible
- Default IP: 192.168.4.1
- Confirm ESP32 is in AP mode

---

## Notes

- Always test with robot suspended before floor operation
- Calibrate servos before first use
- Monitor servo temperatures during extended operation
- Start with slow speeds before increasing
