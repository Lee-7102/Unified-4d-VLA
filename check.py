import cv2


def first_frame(index):
    video_path = "/vast/projects/jgu32/lab/han/data/maniskill/PickCube-v1/videox/ee_gripper/ee_gripper_0252.mp4"
    output_path = "first_frame_gripper.jpg"
    extract_frame(video_path,output_path)
    video_path = "/vast/projects/jgu32/lab/han/data/maniskill/PickCube-v1/videox/ee_rpy/ee_rpy_0252.mp4"
    output_path = "first_frame_rpy.jpg"
    extract_frame(video_path,output_path)
    video_path = "/vast/projects/jgu32/lab/han/data/maniskill/PickCube-v1/videox/ee_xyz/ee_xyz_0252.mp4"
    output_path = "first_frame_xyz.jpg"
    extract_frame(video_path,output_path)
    video_path = "/vast/projects/jgu32/lab/han/data/maniskill/PickCube-v1/videox/pointmap/pointmap_0252.mp4"
    output_path = "first_frame_pointmap.jpg"
    extract_frame(video_path,output_path)
    video_path = "/vast/projects/jgu32/lab/han/data/maniskill/PickCube-v1/videox/rgb/rgb_0252.mp4"
    output_path = "first_frame_rgb.jpg"
    extract_frame(video_path,output_path)

def extract_frame(video_path,output_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_path, frame)
        print(f"Saved the first frame to {output_path}")
    else:
        print("Error: Could not read video or video is empty.")

    # Release the video capture object
    cap.release()

first_frame()