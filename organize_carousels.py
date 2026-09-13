import os
import shutil
from PIL import Image

base_dir = r"C:\Users\Lenovo\Documents\degustacion 2.0"
img_dir = os.path.join(base_dir, "imagenes")

carrusel1_dir = os.path.join(base_dir, "carrusel_1_personas")
carrusel2_dir = os.path.join(base_dir, "carrusel_2_platillos")

os.makedirs(carrusel1_dir, exist_ok=True)
os.makedirs(carrusel2_dir, exist_ok=True)

cover_4k = os.path.join(img_dir, "IMG_3963_degustacion_primavera_4k.png")

# Selection for Carousel 1: Personas y Experiencia (9 images after cover)
# Selected photos showing guests, family, planners, staff, and tasting interaction:
personas_selection = [
    "IMG_3956.jpg", # 3 faces - Tasting interaction
    "IMG_3958.jpg", # 2 faces - Family at tasting table
    "IMG_3960.jpg", # 2 faces - Smiling at table
    "IMG_3961.jpg", # 2 faces - Table toast / service
    "IMG_3972.jpg", # 2 faces - Conversation at tasting
    "IMG_3976.jpg", # 4 faces - Group tasting experience
    "IMG_3981.jpg", # 3 faces - Family dish presentation
    "IMG_3984.jpg", # 7 faces - Full family group at tasting
    "IMG_3988.jpg"  # 5 faces - Group celebration moment
]

# Selection for Carousel 2: Platillos y Gastronomía (9 images after cover)
# Selected photos showing dishes, food presentations, table details:
platillos_selection = [
    "IMG_3952.jpg", # Food dish detail
    "IMG_3954.jpg", # Appetizer / Course presentation
    "IMG_3968.jpg", # Gourmet main course plate
    "IMG_3970.jpg", # Plated dish closeup
    "IMG_3975.jpg", # Table setting & centerpiece detail
    "IMG_3978.jpg", # Food presentation / loza
    "IMG_3980.jpg", # Gourmet dish plating
    "IMG_3990.jpg", # Dessert / Sweet course
    "IMG_3991.jpg"  # Glassware & wine detail
]

print("--- CAROUSEL 1: PERSONAS EN LA DEGUSTACIÓN ---")
# Copy cover
shutil.copy(cover_4k, os.path.join(carrusel1_dir, "01_portada_degustacion.png"))
print("  01_portada_degustacion.png (IMG_3963_degustacion_primavera_4k.png)")

for idx, fname in enumerate(personas_selection, start=2):
    src = os.path.join(img_dir, fname)
    dst_name = f"{idx:02d}_{fname}"
    dst = os.path.join(carrusel1_dir, dst_name)
    shutil.copy(src, dst)
    print(f"  {dst_name} ({fname})")

print("\n--- CAROUSEL 2: PLATILLOS Y GASTRONOMÍA ---")
# Copy cover
shutil.copy(cover_4k, os.path.join(carrusel2_dir, "01_portada_degustacion.png"))
print("  01_portada_degustacion.png (IMG_3963_degustacion_primavera_4k.png)")

for idx, fname in enumerate(platillos_selection, start=2):
    src = os.path.join(img_dir, fname)
    dst_name = f"{idx:02d}_{fname}"
    dst = os.path.join(carrusel2_dir, dst_name)
    shutil.copy(src, dst)
    print(f"  {dst_name} ({fname})")

print("\nSuccessfully organized both carousels into subfolders!")
