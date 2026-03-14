# Media — 12-DOF Quadruped Robot

Demonstration videos, images, and GIFs for the quadruped robot project.

---

## File Structure

media/
├── videos/
│   ├── walking_demo.mp4
│   ├── gait_comparison.mp4
│   ├── assembly_timelapse.mp4
│   └── terrain_test.mp4
├── images/
│   ├── robot_assembled.jpg
│   ├── leg_mechanism.jpg
│   ├── electronics_layout.jpg
│   ├── cad_rendering.png
│   └── kinematics_diagram.png
└── gifs/
    ├── walking_loop.gif
    ├── trot_gait.gif
    └── servo_test.gif

---

## Videos

| File | Description |
|------|-------------|
| walking_demo.mp4 | Standard walk gait — forward, backward, turning |
| gait_comparison.mp4 | Walk vs trot vs crawl side-by-side |
| assembly_timelapse.mp4 | Full assembly from parts to working robot |
| terrain_test.mp4 | Flat ground, carpet, obstacles, inclines |

---

## Useful FFmpeg Commands

Create GIF from video:
```bash
ffmpeg -i walking_demo.mp4 -vf "fps=10,scale=640:-1:flags=lanczos" \
  -t 3 walking_loop.gif
```

Optimize GIF:
```bash
gifsicle -O3 --colors 128 walking_loop.gif -o walking_loop_optimized.gif
```

Trim video:
```bash
ffmpeg -i input.mp4 -ss 00:00:10 -t 00:00:30 -c copy output.mp4
```

Extract thumbnail:
```bash
ffmpeg -i walking_demo.mp4 -ss 00:00:05 -frames:v 1 thumbnail.jpg
```

---

## Embedding in README

Images:
```markdown
![Robot Assembly](media/images/robot_assembled.jpg)
```

GIFs:
```markdown
![Walking Demo](media/gifs/walking_loop.gif)
```

Videos:
```markdown
[![Walking Demo](thumbnail.jpg)](https://youtube.com/watch?v=...)
```

---

## File Naming Convention

YYYYMMDD_description_version.ext

Examples:
- 20240215_walking_demo_v1.mp4
- 20240215_leg_mechanism_front.jpg
- 20240216_trot_gait_loop.gif

---

## Notes

- Compress GIFs to under 5MB before committing
- Use Git LFS for large video files
- Keep raw files backed up before editing
