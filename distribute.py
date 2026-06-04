import os
import shutil

base = f"C:\\Users\\{os.getenv('USERNAME')}\\people_detection"
frames_dir = os.path.join(base, "frames")
all_frames = sorted(os.listdir(frames_dir))

# Train: every 30th frame from first 3000
train_frames = all_frames[0:3000:30]

# Val: every 30th frame from 3001-5200
val_frames = all_frames[3000:5200:30]

# Test: every 15th frame from 5201 onwards
test_frames = all_frames[5200::15]

def copy_frames(frame_list, split):
    dest = os.path.join(base, "images", split)
    for f in frame_list:
        shutil.copy(os.path.join(frames_dir, f), os.path.join(dest, f))
    print(f"{split}: {len(frame_list)} frames copied")

copy_frames(train_frames, "train")
copy_frames(val_frames, "val")
copy_frames(test_frames, "test")
print("All done!")