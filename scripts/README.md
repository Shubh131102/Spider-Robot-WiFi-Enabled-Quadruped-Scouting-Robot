# Scripts — 12-DOF Quadruped Robot

Utility scripts for calibration, testing, and robot operation.

---

## File Structure

scripts/
├── calibration/
│   ├── calibrate_servos.py
│   ├── find_neutral.py
│   └── test_range.py
├── testing/
│   ├── test_servo.py
│   ├── test_ik.py
│   ├── test_gait.py
│   └── hardware_check.py
├── utilities/
│   ├── upload_firmware.sh
│   ├── monitor_serial.py
│   └── generate_poses.py
└── requirements.txt

---

## Requirements
```bash
pip install -r scripts/requirements.txt
# pyserial>=3.5 | numpy>=1.19 | pyyaml>=5.4 | matplotlib>=3.3
```

---

## Calibration Scripts

### calibrate_servos.py
Calibrate all 12 servos to find neutral position offsets.
```bash
python scripts/calibration/calibrate_servos.py --port /dev/ttyACM0
```
Saves offsets to config/control.yaml automatically.

### find_neutral.py
Automated neutral position finding using IMU feedback.
```bash
python scripts/calibration/find_neutral.py --port /dev/ttyACM0 --imu
```
Requires MPU6050 IMU attached to suspended robot.

### test_range.py
Test full range of motion for each servo.
```bash
# Single servo
python scripts/calibration/test_range.py --port /dev/ttyACM0 --servo 0

# All servos
python scripts/calibration/test_range.py --port /dev/ttyACM0 --all
```

---

## Testing Scripts

### test_servo.py
Test individual servo functionality.
```bash
# Sweep test
python scripts/testing/test_servo.py --port /dev/ttyACM0 --channel 0 --sweep

# Set specific angle
python scripts/testing/test_servo.py --port /dev/ttyACM0 --channel 0 --angle 90
```

### test_ik.py
Test inverse kinematics calculations.
```bash
# Single position
python scripts/testing/test_ik.py --x 100 --y 0 --z -80

# Full workspace test
python scripts/testing/test_ik.py --test-workspace
```

### test_gait.py
Test gait patterns.
```bash
python scripts/testing/test_gait.py --gait walk --duration 10
python scripts/testing/test_gait.py --gait trot --visualize
```

### hardware_check.py
Full hardware diagnostics — serial, I2C, servos, camera, battery.
```bash
python scripts/testing/hardware_check.py --port /dev/ttyACM0
```

Checks: Serial | PCA9685 I2C | All 12 servos | ESP32-CAM | Battery voltage

---

## Utility Scripts

### upload_firmware.sh
```bash
./scripts/utilities/upload_firmware.sh arduino
./scripts/utilities/upload_firmware.sh esp32
```

### monitor_serial.py
Timestamped serial monitor with log file support.
```bash
python scripts/utilities/monitor_serial.py --port /dev/ttyACM0
```

### generate_poses.py
```bash
python scripts/utilities/generate_poses.py --type sit --output config/poses/sit.yaml
```

---

## Recommended Workflows

Initial setup:
```bash
python scripts/testing/hardware_check.py --port /dev/ttyACM0
python scripts/calibration/calibrate_servos.py --port /dev/ttyACM0
python scripts/testing/test_ik.py --test-workspace
python scripts/testing/test_gait.py --gait walk --duration 5
```

Debugging:
```bash
python scripts/utilities/monitor_serial.py --port /dev/ttyACM0 --log debug.log
python scripts/testing/test_servo.py --port /dev/ttyACM0 --channel 5 --angle 90
python scripts/testing/hardware_check.py --port /dev/ttyACM0 --verbose
```

---

## Troubleshooting

Permission denied on serial port:
```bash
sudo chmod 666 /dev/ttyACM0
# Permanent fix:
sudo usermod -aG dialout $USER
```

Find serial port:
```bash
python -m serial.tools.list_ports
ls /dev/tty*
```

---

## Notes

- Always test with robot suspended before floor operation
- Use --help flag on any script for detailed usage
- Scripts assume 115200 baud serial settings
- Keep backup of calibration values before modifying
