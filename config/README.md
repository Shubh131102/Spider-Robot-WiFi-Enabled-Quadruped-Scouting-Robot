# Configuration Files — 12-DOF Quadruped Robot

Configuration parameters for servo control, gait planning, kinematics, 
and network communication.

---

## File Structure

config/
├── servos.yaml          # Servo channel mapping and PWM parameters
├── gait_params.yaml     # Gait patterns and walking modes
├── kinematics.yaml      # Robot dimensions and joint limits
├── control.yaml         # Control loop and safety parameters
└── wifi.yaml            # WiFi and camera configuration

---

## servos.yaml — Servo Channel Mapping

PCA9685 I2C address: 0x40 | Neutral PWM: 307 (~1.5ms at 50Hz)

Channel mapping:

Leg    Hip  Thigh  Knee
LF:     0     1      2
RF:     3     4      5
LH:     6     7      8
RH:     9    10     11

Joint naming:
- hip: Yaw rotation
- thigh: Forward/backward pitch
- knee: Up/down pitch

---

## gait_params.yaml — Gait Parameters

| Gait  | Step Height | Stride | Duty Cycle | Speed |
|-------|-------------|--------|------------|-------|
| Walk  | 30mm        | 50mm   | 0.75       | 1.0x  |
| Trot  | 40mm        | 60mm   | 0.50       | 1.5x  |
| Crawl | 20mm        | 30mm   | 0.90       | 0.5x  |

Default gait: walk

Gait selection:
- Walk: Stable, energy efficient, 3 legs always grounded
- Trot: Faster, diagonal pairs move together
- Crawl: Maximum stability, slow, for rough terrain

---

## kinematics.yaml — Robot Dimensions

Link lengths:
- Coxa: 30mm
- Femur: 60mm
- Tibia: 80mm
- Total reach: 170mm | Workspace radius: ~150mm

Body dimensions:
- Length: 120mm | Width: 80mm

Joint limits:
- Hip: -45° to +45°
- Thigh: 30° to 150°
- Knee: 30° to 150°

Default standing pose:
- Hip: 0° | Thigh: 90° | Knee: 90°
- Foot position: ~100mm below body

---

## control.yaml — Control Parameters

PWM configuration:
- Frequency: 50Hz
- Min pulse: 150 (~0.5ms, 0°)
- Neutral pulse: 307 (~1.5ms, 90°)
- Max pulse: 600 (~2.5ms, 180°)

Pulse width formula:
pulse = 150 + (angle * 2.5)

Control loop:
- Update rate: 50Hz
- Interpolation steps: 10

Safety limits:
- Max angle change per update: 30°
- Emergency stop height: 20mm
- Max current draw: 2000mA

---

## wifi.yaml — Network Configuration

Mode: Access Point (AP)
- SSID: SpiderBot
- IP: 192.168.4.1
- Control server port: 80
- WebSocket port: 81

Camera settings:
- Resolution: VGA
- Quality: 12 (0-63, lower = better)
- Framerate: 10fps

---

## Calibration Procedure

1. Center all servos:
   python scripts/calibrate_servos.py --center

2. Adjust offsets in control.yaml:
   Positive offset = clockwise rotation
   Negative offset = counter-clockwise rotation

3. Test standing pose:
   python scripts/test_pose.py --pose standing

4. Fine-tune until all legs are symmetrical

---

## Troubleshooting

Servo not responding:
- Verify channel in servos.yaml
- Check I2C address (default 0x40)
- Confirm power supply (7.4V, sufficient current)

Robot not standing level:
- Adjust calibration offsets in control.yaml
- Measure actual servo positions and correct

Jerky movement:
- Increase interpolation_steps to 20
- Increase update_rate to 100Hz
- Check power supply voltage stability

---

## Default Configuration Summary

| Parameter       | Value | Unit |
|----------------|-------|------|
| PWM Frequency  | 50    | Hz   |
| Neutral Pulse  | 307   | counts |
| Control Rate   | 50    | Hz   |
| Default Gait   | walk  | -    |
| Standing Height| 100   | mm   |
| Max Reach      | 150   | mm   |
| Total DOF      | 12    | -    |

---

## Notes

- All angles in degrees, all lengths in millimeters
- Calibration values are robot-specific — save original before modifying
- Test with robot suspended before floor operation
- Monitor servo temperatures during extended use
