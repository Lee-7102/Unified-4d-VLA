from PIL import Image

# Load or create your 5 starting frames (each 256×256)
frames = [
    Image.open("first_frame_rgb.jpg").resize((256, 256)),
    Image.open("first_frame_pointmap.jpg").resize((256, 256)),
    Image.open("first_frame_xyz.jpg").resize((256, 256)),
    Image.open("first_frame_rpy.jpg").resize((256, 256)),
    Image.open("first_frame_gripper.jpg").resize((256, 256))
]

# Concatenate horizontally
first_frame = Image.new('RGB', (1280, 256))
for i, frame in enumerate(frames):
    first_frame.paste(frame, (i * 256, 0))

first_frame.save("/vast/projects/jgu32/lab/yiqian/VideoX-Fun/first_frame.jpg")