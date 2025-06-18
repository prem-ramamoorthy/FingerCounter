# Finger Counter

A real-time finger counting application built using **OpenCV** and **MediaPipe**, capable of detecting the number of fingers held up using hand landmark tracking.

## Tech Stack

- Python
- OpenCV
- MediaPipe

## Features

- Real-time hand detection
- Accurate finger state recognition
- Lightweight and responsive
- Works with webcam input

## How It Works

1. MediaPipe tracks 21 hand landmarks in real time.
2. Joint positions are analyzed to determine which fingers are open.
3. The total number of raised fingers is displayed live on the screen.

## Installation

```bash
git clone https://github.com/your-username/finger-counter.git
cd finger-counter
pip install -r requirements.txt
```

## Usage
```bash
python finger_counter.py
```
