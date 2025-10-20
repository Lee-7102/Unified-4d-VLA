import cv2
from PIL import Image
import os

def extract_frame(video_path, output_path):
    """Extracts and saves the first frame from a video."""
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_path, frame)
        print(f"Saved the first frame to {output_path}")
    else:
        print(f"Error: Could not read {video_path}")
    cap.release()


def first_frame(index):
    """Extract first frames from all modalities and combine them."""
    base_dir = "/vast/projects/jgu32/lab/han/data/maniskill/PickCube-v1/videox"
    output_dir = "/vast/projects/jgu32/lab/yiqian/VideoX-Fun"
    os.makedirs(output_dir, exist_ok=True)

    # Format index as 4 digits, e.g. 252 -> 0252
    idx_str = f"{index:04d}"

    # Define video categories
    modalities = ["rgb", "pointmap", "ee_xyz", "ee_rpy", "ee_gripper"]

    # Extract first frames
    frame_paths = []
    for mod in modalities:
        video_path = f"{base_dir}/{mod}/{mod}_{idx_str}.mp4"
        output_path = f"{output_dir}/first_frame_{mod}.jpg"
        extract_frame(video_path, output_path)
        frame_paths.append(output_path)

    # Load, resize, and concatenate frames horizontally
    frames = [Image.open(p).resize((256, 256)) for p in frame_paths]
    combined = Image.new("RGB", (256 * len(frames), 256))
    for i, frame in enumerate(frames):
        combined.paste(frame, (i * 256, 0))

    combined_path = os.path.join(output_dir, f"first_frame.jpg")
    combined.save(combined_path)
    print(f"Saved combined image to {combined_path}")


# Example usage:
first_frame(252)
