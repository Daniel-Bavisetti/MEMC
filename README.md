# MEMC - Motion Estimation and Motion Compensation using Block Matching

This project demonstrates a simple implementation of **Motion Estimation and Motion Compensation (MEMC)** using block matching and Mean Absolute Difference (MAD). It processes two consecutive frames from a video to estimate motion vectors and uses them to generate a motion-compensated frame.

## 📌 Features

- Motion estimation via **block matching**
- Uses **Mean Absolute Difference (MAD)** for similarity measure
- Motion compensation to reconstruct next frame from previous frame
- Grayscale conversion for simplicity and efficiency
- Simple and readable implementation using Python and OpenCV

## 🧠 How It Works

1. **Block Matching Motion Estimation**  
   Divides the first frame into non-overlapping blocks, and for each block, searches within a defined range in the second frame to find the most similar block using MAD.

2. **Motion Compensation**  
   Applies the estimated motion vectors to the first frame to reconstruct or approximate the second frame.

## 📁 Files

- `memc.py`: The main Python file that contains the implementation of motion estimation and motion compensation.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- NumPy

Install the dependencies:

```bash
pip install opencv-python numpy
