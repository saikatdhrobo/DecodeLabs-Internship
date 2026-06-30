# Building the Machine's Optic Nerve

## Project Objective

This project detects objects from an input image using OpenCV's DNN module and the pre-trained MobileNet-SSD model.

## Technologies

- Python
- OpenCV
- NumPy

## IPO Model

### Input
- Street image
- MobileNet-SSD model

### Process
- Load image
- Create 300×300 blob
- Perform object detection
- Filter detections with confidence ≥80%
- Scale coordinates
- Draw bounding boxes

### Output
- Annotated image saved in the `output` folder

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

## Output

```
output/
└── detected_objects.jpg
```

## Features

- MobileNet SSD
- OpenCV DNN
- 300×300 Blob
- 80% Confidence Threshold
- Bounding Boxes
- Coordinate Scaling