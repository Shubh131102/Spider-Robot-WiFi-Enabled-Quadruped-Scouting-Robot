# CAD Files — 12-DOF Quadruped Robot

Mechanical design files for the 12-DOF quadruped robot, including SolidWorks 
source files, STL files for 3D printing, and assembly documentation.

---

## File Structure

cad/
├── assembly/
│   ├── full_assembly.step
│   ├── full_assembly.stl
│   └── assembly_instructions.pdf
├── body/
│   ├── main_chassis.stl
│   ├── electronics_mount.stl
│   └── battery_holder.stl
├── legs/
│   ├── coxa.stl
│   ├── femur.stl
│   ├── tibia.stl
│   └── foot.stl
├── servo_mounts/
│   ├── servo_bracket.stl
│   └── servo_horn_adapter.stl
└── source_files/
    ├── solidworks/
    └── step/

---

## Parts Overview

### Body Components

**main_chassis.stl**
- Central body platform with mounting points for 4 legs
- Electronics compartment with cable management
- Dimensions: 120mm x 80mm x 20mm | Weight: ~45g (PLA)

**electronics_mount.stl**
- Mounting plate for Arduino and PCA9685
- Cable management channels and PCB standoffs

**battery_holder.stl**
- Secure battery compartment with access panel
- Fits 7.4V LiPo battery

---

### Leg Components (4 sets required)

Each leg consists of 3 segments with 3 DOF:

**coxa.stl** — Hip joint | Length: 30mm | Weight: ~8g
**femur.stl** — Upper leg | Length: 60mm | Weight: ~12g
**tibia.stl** — Lower leg | Length: 80mm | Weight: ~10g
**foot.stl** — Replaceable foot | Weight: ~3g

---

### Specifications

**Overall Dimensions:**
- Body: 120mm x 80mm x 20mm
- Total span leg to leg: 250mm
- Standing height: 120mm
- Total weight: ~850g

**Leg Kinematic Chain:**
Body → Coxa (yaw) → Femur (pitch) → Tibia (pitch) → Foot

**Joint Ranges:**
- Coxa: ±45° from center
- Femur: 30–150°
- Tibia: 30–150°

---

## 3D Printing Guidelines

**Material:** PLA (recommended) or PETG

**Settings:**
- Layer height: 0.2mm (0.15mm for small parts)
- Infill: Body 40% | Legs 30% | Servo mounts 50%
- Wall thickness: 3 perimeters minimum

**Print Orientation:**
- Legs: Print vertically for strength along load axis
- Body: Print flat for dimensional accuracy
- Servo mounts: Orient for minimal supports

**Total Print Time:** ~37.5 hours
**Total Filament:** ~400g PLA

---

## Hardware Required

- M2 x 8mm screws: 48 (servo mounting)
- M3 x 10mm screws: 20 (body assembly)
- M3 x 20mm screws: 8 (leg attachment)
- M3 nuts: 28
- Heat-set inserts M3: 16 (optional)

---

## Assembly Sequence

1. Remove supports and sand mating surfaces
2. Install servos into brackets and secure with M2 screws
3. Assemble each leg: coxa → femur → tibia → foot
4. Mount electronics plate with Arduino and PCA9685
5. Route and secure all servo cables
6. Install battery holder and connect power distribution

---

## Design Iterations

**Version 1.0:** Initial prototype — basic leg design, fixed electronics mount

**Version 2.0:** Current — reinforced leg joints, modular servo mounts, 
improved cable routing, battery access panel, thermal management via 
chassis geometry redesign

---

## Opening Files

**SolidWorks:**
File → Open → Select .sldprt or assembly.step | Set units to mm

**FreeCAD (Open Source):**
File → Open → assembly.step

---

## Notes

- All dimensions in millimeters
- Designed for MG996R/SG90 servos
- Test print one leg assembly before printing all parts
- Increase infill or wall count if legs show weakness under load
