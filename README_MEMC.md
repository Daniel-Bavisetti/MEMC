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
```

### Usage

1. Replace the video path in the code:

```python
video_path = "your_video.mp4"  # Replace with your video file path
```

2. Run the script:

```bash
python memc.py
```

3. The following frames will be displayed:
   - Original Frame 1
   - Original Frame 2
   - Motion Compensated Frame (reconstructed from Frame 1 using motion vectors)

## ⚙️ Parameters

You can adjust the following parameters in the code to see different results:

- `block_size`: Size of the block (e.g., 8x8, 16x16)
- `search_range`: How far to search in the neighboring region for block matching

Example:

```python
block_size = 16
search_range = 32
```

## 🖼️ Output

- Motion-compensated frame mimics Frame 2 by warping Frame 1 using estimated motion.
- Useful in applications like video compression, frame interpolation, and motion analysis.

## 📚 Concepts Used

- Block Matching
- Mean Absolute Difference (MAD)
- Motion Vector Calculation
- Grayscale Image Processing
- Frame Reconstruction

## 📌 Sample Visual

```
[Frame 1] ---> [Motion Vectors] ---> [Motion Compensated Frame ≈ Frame 2]
```

## 🧑‍💻 Author

Daniel Bavisetti

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
