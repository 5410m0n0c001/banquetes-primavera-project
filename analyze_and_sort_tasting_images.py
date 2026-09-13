import os
import cv2
from PIL import Image

img_dir = r"C:\Users\Lenovo\Documents\degustacion 2.0\imagenes"
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Get unique standard JPG image files
files = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.jpeg')) and f.startswith('IMG_')])

results = []

for f in files:
    path = os.path.join(img_dir, f)
    img_cv = cv2.imread(path)
    if img_cv is None:
        continue
        
    height, width, _ = img_cv.shape
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    
    # Resize for faster face detection if very large
    max_dim = 1200
    if max(height, width) > max_dim:
        scale = max_dim / float(max(height, width))
        gray_scaled = cv2.resize(gray, (0, 0), fx=scale, fy=scale)
    else:
        gray_scaled = gray
        
    faces = face_cascade.detectMultiScale(gray_scaled, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
    face_count = len(faces)
    
    results.append({
        'filename': f,
        'path': path,
        'size': (width, height),
        'faces': face_count
    })

print(f"Total analyzed: {len(results)}")
print("\n--- IMAGES WITH FACES (PERSONAS) ---")
people_imgs = [r for r in results if r['faces'] > 0]
for p in people_imgs:
    print(f"  {p['filename']}: {p['faces']} faces found")

print("\n--- IMAGES WITHOUT FACES (PLATILLOS / DETALLES) ---")
food_imgs = [r for r in results if r['faces'] == 0]
for f in food_imgs:
    print(f"  {f['filename']}")
