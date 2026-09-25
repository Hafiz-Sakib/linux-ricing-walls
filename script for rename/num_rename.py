import os

folder = os.path.dirname(os.path.abspath(__file__))

image_extensions = {
    ".jpg", ".jpeg", ".png", ".webp",
    ".gif", ".bmp", ".tiff", ".tif"
}

all_images = [
    f for f in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, f))
    and os.path.splitext(f)[1].lower() in image_extensions
]

# Sort by modification time (oldest first) so the new numbers reflect
# the order the images were actually added/created, regardless of
# whether the current name is letters, numbers, or anything else.
all_images.sort(key=lambda f: os.path.getmtime(os.path.join(folder, f)))

pad_width = len(str(len(all_images)))  # e.g. 3 digits for up to 999 files

# Phase 1: rename everything to temp names to avoid collisions
temp_files = []
for i, filename in enumerate(all_images, start=1):
    old_path = os.path.join(folder, filename)
    ext = os.path.splitext(filename)[1].lower()
    temp_name = f"__temp_num_{i}{ext}"
    temp_path = os.path.join(folder, temp_name)
    os.rename(old_path, temp_path)
    temp_files.append((temp_path, ext))

# Phase 2: rename to final zero-padded sequential names
for i, (temp_path, ext) in enumerate(temp_files, start=1):
    new_name = f"{i:0{pad_width}d}{ext}"
    new_path = os.path.join(folder, new_name)
    os.rename(temp_path, new_path)

print(f"Done! {len(all_images)} image(s) renamed to {pad_width}-digit sequential numbers (e.g. 001, 002, ...).")