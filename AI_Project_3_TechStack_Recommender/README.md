# AI Tech Stack Recommender

A content-based recommendation system that suggests the most suitable tech careers based on a user's skills and interests. Uses **TF-IDF vectorization** and **cosine similarity** to match user-provided skills against a curated dataset of career paths.

---

## Features

- Interactive CLI onboarding for collecting user name and skills
- TF-IDF based skill-to-career matching
- Top-3 career recommendations with similarity scores
- Pre-loaded dataset covering **21+ tech careers** (AI Engineer, Data Scientist, DevOps, etc.)
- Easily extendable dataset (`dataset/raw_skills.csv`)

---

## How It Works

```
User Input (Skills) → TF-IDF Vectorization → Cosine Similarity → Ranked Careers
```

1. **User enters at least 3 skills** (e.g., Python, Machine Learning, Django)
2. The system converts all career skill-sets and the user input into TF-IDF vectors
3. Cosine similarity is computed between the user vector and each career vector
4. The top 3 careers with the highest similarity scores are displayed

---

## Dataset

The dataset (`dataset/raw_skills.csv`) contains 21 tech careers with their associated skills:

| Career | Skills |
|---|---|
| AI Engineer | Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, NLP, Computer Vision, Git, Linux |
| Data Scientist | Python, Pandas, NumPy, Statistics, Machine Learning, SQL, Data Visualization |
| Backend Developer | Python, Django, Flask, REST API, SQL, Git, Docker |
| Frontend Developer | HTML, CSS, JavaScript, React, Bootstrap, UI, UX |
| ... and 17 more | |

---

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Steps

```bash
# Clone the repository
git clone <repo-url>
cd AI_Project_3_TechStack_Recommender

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

- `pandas` — Data manipulation
- `scikit-learn` — TF-IDF Vectorizer & Cosine Similarity
- `numpy` — Numerical operations

---

## Usage

```bash
python main.py
```

**Example session:**

```
==================================================
Welcome to AI Tech Stack Recommender
==================================================
Enter your name: Alice

Hello Alice!

Please answer a few questions.

Enter at least THREE skills/interests.

Skill 1: Python
Skill 2: Machine Learning
Skill 3: Django

============================================================
Top Career Recommendations for Alice
============================================================

1. Backend Developer
   Similarity Score : 0.419
   Required Skills  : Python Django Flask REST API SQL Git Docker

2. Full Stack Developer
   Similarity Score : 0.385
   Required Skills  : HTML CSS JavaScript React Node.js Express MongoDB SQL Git

3. Software Engineer
   Similarity Score : 0.326
   Required Skills  : Java Python C++ OOP Git Data Structures Algorithms SQL

Thank you for using the recommender!
```

---

## Project Structure

```
.
├── main.py                  # Entry point / CLI interface
├── recommender.py           # TechStackRecommender class (TF-IDF + cosine similarity)
├── requirements.txt         # Python dependencies
├── dataset/
│   └── raw_skills.csv       # Career-skills dataset
└── README.md                # This file
```

---

## Extending the Dataset

Add new careers by appending rows to `dataset/raw_skills.csv`:

```csv
Career,Skills
Robotics Engineer,"ROS C++ Python SLAM Computer Vision Embedded Linux"
```

---

## License

MIT
