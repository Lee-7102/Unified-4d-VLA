import json
import os
from decord import VideoReader

# Load your dataset
json_path = "/vast/projects/jgu32/lab/han/data/maniskill/PickCube-v1/videox/json_of_internal_datasets.json"
data_root = "/vast/projects/jgu32/lab/yiqian/VideoX-Fun"

with open(json_path, 'r') as f:
    dataset = json.load(f)

# Check the problematic samples
problematic_ids = [7599]

print("Checking frame counts for problematic samples:\n")

for idx in problematic_ids:
    if idx < len(dataset):
        data_info = dataset[idx]
        print(f"=== Sample {idx} ===")
        print(f"Text: {data_info['text']}")
        
        video_paths = {
            'rgb': os.path.join(data_root, data_info['file_path']),
            'pointmap': os.path.join(data_root, data_info['pointmap_path']),
            'ee_xyz': os.path.join(data_root, data_info['ee_xyz_path']),
            'ee_rpy': os.path.join(data_root, data_info['ee_rpy_path']),
            'ee_gripper': os.path.join(data_root, data_info['ee_gripper_path'])
        }
        
        frame_counts = {}
        for name, path in video_paths.items():
            try:
                vr = VideoReader(path, num_threads=2)
                frame_counts[name] = len(vr)
                del vr
            except Exception as e:
                frame_counts[name] = f"ERROR: {e}"
        
        print("\nFrame counts:")
        for name, count in frame_counts.items():
            print(f"  {name:12s}: {count}")
        
        # Check if all have same count
        counts = [c for c in frame_counts.values() if isinstance(c, int)]
        if len(set(counts)) > 1:
            print(f"  ⚠️  MISMATCH! Min: {min(counts)}, Max: {max(counts)}")
        else:
            print(f"  ✓ All videos have same frame count")
        print()

print("\n" + "="*60)
print("Checking a few random samples...")
import random
for _ in range(5):
    idx = random.randint(0, len(dataset)-1)
    data_info = dataset[idx]
    
    if data_info.get('type', 'image') == 'video':
        video_paths = {
            'rgb': os.path.join(data_root, data_info['file_path']),
            'pointmap': os.path.join(data_root, data_info['pointmap_path']),
            'ee_xyz': os.path.join(data_root, data_info['ee_xyz_path']),
        }
        
        frame_counts = {}
        for name, path in video_paths.items():
            try:
                vr = VideoReader(path, num_threads=2)
                frame_counts[name] = len(vr)
                del vr
            except:
                frame_counts[name] = 0
        
        counts = list(frame_counts.values())
        if len(set(counts)) > 1:
            print(f"Sample {idx}: Frame count mismatch! {frame_counts}")