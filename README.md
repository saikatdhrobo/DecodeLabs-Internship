# Decode Labs AI Internship Projects

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

A portfolio of 4 AI projects built during an internship at **Decode Labs**. Covers rule-based chatbots, machine learning classification, content-based recommendation systems, and computer vision object detection.

## Projects Overview

| # | Project | Category | Algorithm / Technique | Key Libraries |
|---|---------|----------|----------------------|---------------|
| 1 | **SaikatMate Bot** | Rule-based Chatbot | Dictionary intent matching | Python stdlib |
| 2 | **Iris Classification** | ML Classification | K-Nearest Neighbors (k=5) | scikit-learn, pandas, numpy |
| 3 | **TechStack Recommender** | Content-based Recommender | TF-IDF + Cosine Similarity | scikit-learn, pandas, numpy |
| 4 | **Machines Optic Nerve** | Computer Vision | MobileNet-SSD (Caffe) | OpenCV, numpy |

---

## 1. SaikatMate Bot

A conversational chatbot that responds to user input using a predefined intent–response dictionary. Supports 15 intents (greetings, motivation, jokes, study tips, etc.) and runs in an interactive CLI loop.

**Run:**
```bash
cd AI_Project_1_SaikatMate_Bot
python main.py
```

---

## 2. Iris Classification

Classifies Iris flowers into three species (*Setosa*, *Versicolor*, *Virginica*) using the K-Nearest Neighbors algorithm. The full ML pipeline includes data loading, train/test splitting, feature scaling, training, and evaluation (accuracy, precision, recall, F1, confusion matrix). Achieves **100% accuracy** on the test set.

**Run:**
```bash
cd AI_Project_2_Classification
pip install -r requirements.txt
python main.py
```

---

## 3. TechStack Recommender

A content-based recommendation system that suggests the top 3 tech careers based on a user's entered skills. Uses TF-IDF vectorization and cosine similarity to match user input against 21 career profiles (AI Engineer, Data Scientist, Backend Developer, etc.).

**Run:**
```bash
cd AI_Project_3_TechStack_Recommender
pip install -r requirements.txt
python main.py
```

---

## 4. Machines Optic Nerve

An object detection pipeline using a pre-trained MobileNet-SSD model (Caffe) via OpenCV's DNN module. Detects 20 object classes (person, car, bus, dog, etc.) in images, draws bounding boxes with confidence labels, and saves the annotated output.

**Run:**
```bash
cd AI_Project_4_Machines_Optic_Nerve
pip install -r requirements.txt
python main.py
```

---

## Getting Started

1. **Clone the repo:**
   ```bash
   git clone https://github.com/saikatdhrobo/DecodeLabs-Internship.git
   cd DecodeLabs-Internship
   ```
2. Navigate into any project folder and follow its run instructions above.

## Tech Stack

- **Language:** Python 3.x
- **ML / AI:** scikit-learn, OpenCV, Caffe (MobileNet-SSD)
- **Data:** pandas, numpy
- **No external deps:** Project 1 uses only Python standard library

## License

[MIT](LICENSE)
