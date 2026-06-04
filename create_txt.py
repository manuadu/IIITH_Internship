import os

base = r"C:\Users\manma\people_detection"

for split in ['train', 'val']:
    img_dir = os.path.join(base, 'images', split)
    txt_file = os.path.join(base, f'{split}.txt')
    with open(txt_file, 'w') as f:
        for img in sorted(os.listdir(img_dir)):
            if img.endswith('.jpg') or img.endswith('.png'):
                f.write(os.path.join(img_dir, img) + '\n')
    print(f"{split}.txt created!")