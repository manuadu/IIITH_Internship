import os
import shutil

base = r"C:\Users\manma\people_detection"
val_labels = os.path.join(base, "labels", "val")
train_labels = os.path.join(base, "labels", "train")

# Get val image names (without extension)
val_images = set(f.replace(".jpg", "") for f in os.listdir(os.path.join(base, "images", "val")))
train_images = set(f.replace(".jpg", "") for f in os.listdir(os.path.join(base, "images", "train")))

for filename in os.listdir(val_labels):
    if filename.endswith(".txt"):
        # Remove prefix first
        clean_name = filename.split("-", 1)[1] if "-" in filename else filename
        frame_name = clean_name.replace(".txt", "")
        old_path = os.path.join(val_labels, filename)

        if frame_name in val_images:
            # Belongs to val — just rename it
            new_path = os.path.join(val_labels, clean_name)
            os.rename(old_path, new_path)
            print(f"Val: {filename} → {clean_name}")
        elif frame_name in train_images:
            # Belongs to train — move it there
            new_path = os.path.join(train_labels, clean_name)
            shutil.move(old_path, new_path)
            print(f"Moved to train: {filename} → {clean_name}")
        else:
            print(f"Unknown: {filename} — skipping")

print("Done!")