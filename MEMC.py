import cv2
import numpy as np

def block_matching_motion_estimation(frame1, frame2, block_size=8, search_range=16):
    """
    Performs block matching motion estimation using Mean Absolute Difference (MAD).

    Args:
        frame1: The previous frame (numpy array).
        frame2: The current frame (numpy array).
        block_size: The size of the blocks to match (e.g., 8x8).
        search_range: The maximum search distance for motion vectors.

    Returns:
        motion_vectors: A numpy array containing the motion vectors for each block.
                         Shape: (num_blocks_vertical, num_blocks_horizontal, 2)
    """
    height, width = frame1.shape
    motion_vectors = np.zeros((height // block_size, width // block_size, 2), dtype=int)  # Store motion vectors (dx, dy)

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            best_match_x = x
            best_match_y = y
            min_mad = float('inf')  # Initialize with a large value

            # Iterate over the search range
            for search_y in range(max(0, y - search_range), min(height - block_size, y + search_range)):
                for search_x in range(max(0, x - search_range), min(width - block_size, x + search_range)):
                    # Calculate Mean Absolute Difference (MAD)
                    block1 = frame1[y:y + block_size, x:x + block_size]
                    block2 = frame2[search_y:search_y + block_size, search_x:search_x + block_size]
                    mad = np.sum(np.abs(block1.astype(np.float64) - block2.astype(np.float64))) / (block_size * block_size)  #Prevent uint8 overflow

                    if mad < min_mad:
                        min_mad = mad
                        best_match_x = search_x
                        best_match_y = search_y

            # Store the motion vector
            motion_vectors[y // block_size, x // block_size, 0] = best_match_x - x  # dx
            motion_vectors[y // block_size, x // block_size, 1] = best_match_y - y  # dy

    return motion_vectors


def motion_compensation(frame1, motion_vectors, block_size=8):
    """
    Performs motion compensation using the estimated motion vectors.

    Args:
        frame1: The previous frame (numpy array).
        motion_vectors: The motion vectors (numpy array).
        block_size: The size of the blocks used for motion estimation.

    Returns:
        compensated_frame: The motion-compensated frame (numpy array).
    """
    height, width = frame1.shape
    compensated_frame = np.zeros_like(frame1)

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            dy, dx = motion_vectors[y // block_size, x // block_size]

            # Calculate the source coordinates
            src_x = x + dx
            src_y = y + dy

            # Handle out-of-bounds cases (simple clamping)
            src_x = np.clip(src_x, 0, width - block_size)
            src_y = np.clip(src_y, 0, height - block_size)

            # Copy the block from the previous frame to the compensated frame
            compensated_frame[y:y + block_size, x:x + block_size] = frame1[src_y:src_y + block_size, src_x:src_x + block_size]

    return compensated_frame.astype(np.uint8)


# Example usage:
if __name__ == "__main__":
    # Load two consecutive frames from a video
    video_path = "your_video.mp4"  # Replace with your video file
    cap = cv2.VideoCapture(video_path)

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    if not ret:
        print("Error reading video frames.")
        exit()

    # Convert to grayscale
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    block_size = 16
    search_range = 32

    # Motion Estimation
    motion_vectors = block_matching_motion_estimation(frame1, frame2, block_size, search_range)

    # Motion Compensation
    compensated_frame = motion_compensation(frame1, motion_vectors, block_size)

    # Display the results
    cv2.imshow("Frame 1", frame1)
    cv2.imshow("Frame 2", frame2)
    cv2.imshow("Compensated Frame", compensated_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cap.release()
