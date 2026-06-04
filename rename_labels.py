import os

labels_dir = r"C:\Users\manma\people_detection\labels\val"

for filename in os.listdir(labels_dir):
    if filename.endswith(".txt"):
        # Remove everything before the last hyphen
        # "00d2ca1a-frame_0691.txt" → "frame_0691.txt"
        if "-" in filename:
            new_name = filename.split("-", 1)[1]
            old_path = os.path.join(labels_dir, filename)
            new_path = os.path.join(labels_dir, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

print("All done!")