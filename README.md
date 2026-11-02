# Gesture_Dec
# GestureLens

A small computer vision project exploring hand tracking and gesture detection using Python.

GestureLens uses a webcam to track a hand, identify which fingers are raised, and classify a few predefined hand gestures.

The idea is to build the detection logic myself rather than rely entirely on a pre-trained gesture classifier.

### What it does right now

- Captures live video through a webcam.
- Detects and tracks a hand using CVZone.
- Identifies the state of each finger (raised or lowered).
- Uses simple conditional logic to recognise predefined gestures.

### Built with

- Python
- OpenCV
- CVZone
- MediaPipe

### Running locally

Clone the repository:

```bash
git clone https://github.com/raghavvoid-static/Gesture_Dec.git
cd Gesture_Dec
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the required libraries:

```bash
pip install opencv-python cvzone mediapipe numpy
```

Run the Python script:

```bash
python main.py
```

Replace `main.py` with the name of your actual script if needed.

### A work in progress

This project is still evolving. The current focus is on making gesture detection more consistent, especially when the hand is viewed from different angles.

There is plenty left to figure out, and that's part of the point of building it.

---

*Built as a hands-on exploration of computer vision.*