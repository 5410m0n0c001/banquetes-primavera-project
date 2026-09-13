import json

# Define the merged, cleaned roster manually to ensure 100% accuracy based on our analysis.
# We apply:
# 1. Contact name as display name if available.
# 2. Exclude: Anet Guarneros, Viajando con la música, and Redes/Red.
# 3. Associate each with its logo path (from C:\Users\Lenovo\Documents\expo expositores\assets\) if it exists.
# 4. If no contact name, use the Brand/Business name.

final_roster = [
    # 1. From Excel (with contact names)
    {
        "displayName": "Abigail Jiménez Sandoval",
        "brandName": "Aby Decora",
        "logoName": "logo_new4.png"
    },
    {
        "displayName": "Griselda Anaid Villanueva Bailón",
        "brandName": "La Princesa Paletería",
        "logoName": "logo_new1.png"
    },
    {
        "displayName": "Humberto Carranza Núñez",
        "brandName": "Academia de Baile Dance Queens",
        "logoName": "logo_new5.png"
    },
    {
        "displayName": "Renata Salazar",
        "brandName": "Mariachi Xiuhtépetl",
        "logoName": "logo_new12.jpeg"
    },
    {
        "displayName": "Licky Baut",
        "brandName": "Licky Baut Photo",
        "logoName": "logo_new2.png"
    },
    {
        "displayName": "Isabel Santibáñez Alanis",
        "brandName": "Kataleya Florist",
        "logoName": "logo_new9.png"
    },
    {
        "displayName": "Carlos Arturo Sánchez Chávez",
        "brandName": "Tequila Personalizado Don Ramón",
        "logoName": "logo_new3.png"
    },
    {
        "displayName": "Ismael Cuevas",
        "brandName": "Scanner DJ",
        "logoName": "logo_new19.png"
    },
    {
        "displayName": "Diego Corona Vega",
        "brandName": "Corona Music",
        "logoName": "logo_new8.png"
    },
    
    # 2. From Excel (without contact names)
    {
        "displayName": "Andrea Lozano Beauty Salon",
        "brandName": "Andrea Lozano Beauty Salon",
        "logoName": None
    },
    {
        "displayName": "Jardín de Eventos Calesa",
        "brandName": "Jardín de Eventos Calesa",
        "logoName": None
    },
    {
        "displayName": "Letras Gigantes LG",
        "brandName": "Letras Gigantes LG",
        "logoName": None
    },
    {
        "displayName": "Mía Concept Store",
        "brandName": "Mía Concept Store", # Matches 'mia pasteleria' in Excel
        "logoName": "logo_new17.png"
    },
    {
        "displayName": "Producciones DJ Classic",
        "brandName": "Producciones DJ Classic",
        "logoName": None
    },
    {
        "displayName": "Coreografías Bailes y Vals David",
        "brandName": "Coreografías Bailes y Vals David",
        "logoName": "logo_new18.jpeg"
    },

    # 3. Missing exhibitors from Roster/Logos
    {
        "displayName": "Banquetes Delicatessen",
        "brandName": "Banquetes Delicatessen",
        "logoName": "logo_new6.png"
    },
    {
        "displayName": "DJ & Proyecciones",
        "brandName": "DJ & Proyecciones",
        "logoName": "logo_new7.png"
    },
    {
        "displayName": "Arreglos Florales",
        "brandName": "Arreglos Florales",
        "logoName": "logo_new10.png"
    },
    {
        "displayName": "Invitaciones Elegantes",
        "brandName": "Invitaciones Elegantes",
        "logoName": "logo_new11.png"
    },
    {
        "displayName": "Iluminación Led",
        "brandName": "Iluminación Led",
        "logoName": "logo_new13.png"
    },
    {
        "displayName": "Cabina de Fotos",
        "brandName": "Cabina de Fotos",
        "logoName": "logo_new14.png"
    },
    {
        "displayName": "Barra de Postres",
        "brandName": "Barra de Postres",
        "logoName": "logo_new15.png"
    },
    {
        "displayName": "Saxofonista Solista",
        "brandName": "Saxofonista Solista",
        "logoName": "logo_new16.png"
    },

    # 4. Activity performers not in roster/logos
    {
        "displayName": "Espectáculo de Marimba",
        "brandName": "Espectáculo de Marimba",
        "logoName": None
    },
    {
        "displayName": "Banda Instrumental",
        "brandName": "Banda Instrumental",
        "logoName": None
    },
    {
        "displayName": "Grupo Bonanza",
        "brandName": "Grupo Bonanza",
        "logoName": None
    },
    {
        "displayName": "Banda Lago Negro",
        "brandName": "Banda Lago Negro",
        "logoName": None
    },
    {
        "displayName": "Paola (Academia JHANADE)",
        "brandName": "Paola (Academia JHANADE)",
        "logoName": None
    },

    # 5. Organizers
    {
        "displayName": "Primavera Events Group",
        "brandName": "Primavera Events Group",
        "logoName": "logo_presidente.png" # Let's use the presidente logo as organizer logo
    }
]

with open(r"scratch\final_roster.json", "w", encoding="utf-8") as f:
    json.dump(final_roster, f, indent=2, ensure_ascii=False)

print(f"final_roster.json created with {len(final_roster)} entries.")
