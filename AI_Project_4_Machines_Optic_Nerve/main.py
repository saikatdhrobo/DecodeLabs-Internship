"""
Project 4: Building the Machine's Optic Nerve
DecodeLabs Internship

IPO Model

INPUT:
    - Image
    - Pretrained MobileNet SSD model

PROCESS:
    - Read image
    - Create 300x300 blob
    - Detect objects
    - Keep detections with confidence >= 80%
    - Scale coordinates to original image
    - Draw bounding boxes

OUTPUT:
    - Image with labeled bounding boxes
"""

import cv2
import os

# -----------------------------
# Model Files
# -----------------------------
PROTOTXT = "models/MobileNetSSD_deploy.prototxt"
MODEL = "models/MobileNetSSD_deploy.caffemodel"

IMAGE = "images/street.jpg"

OUTPUT = "output"
os.makedirs(OUTPUT, exist_ok=True)

# ImageNet Classes
CLASSES = [
    "background", "aeroplane", "bicycle", "bird",
    "boat", "bottle", "bus", "car", "cat",
    "chair", "cow", "diningtable", "dog",
    "horse", "motorbike", "person",
    "pottedplant", "sheep", "sofa",
    "train", "tvmonitor"
]

print("Loading Model...")
net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)

image = cv2.imread(IMAGE)

if image is None:
    print("Image not found!")
    exit()

(h, w) = image.shape[:2]

# -----------------------------
# Pre-processing
# -----------------------------
blob = cv2.dnn.blobFromImage(
    image,
    scalefactor=0.007843,
    size=(300, 300),
    mean=127.5
)

net.setInput(blob)

print("Detecting Objects...")
detections = net.forward()

for i in range(detections.shape[2]):

    confidence = detections[0, 0, i, 2]

    # Gatekeeper Rule (80%)
    if confidence >= 0.80:

        idx = int(detections[0, 0, i, 1])

        box = detections[0, 0, i, 3:7]

        startX = int(box[0] * w)
        startY = int(box[1] * h)
        endX = int(box[2] * w)
        endY = int(box[3] * h)

        label = f"{CLASSES[idx]} : {confidence*100:.1f}%"

        cv2.rectangle(image,
                      (startX, startY),
                      (endX, endY),
                      (0, 255, 0), 2)

        cv2.putText(image,
                    label,
                    (startX, startY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 0, 255),
                    2)

output_path = os.path.join(OUTPUT, "detected_objects.jpg")
cv2.imwrite(output_path, image)

print("\nDetection Complete!")
print("Saved:", output_path)

# cv2.imshow("Object Detection", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()