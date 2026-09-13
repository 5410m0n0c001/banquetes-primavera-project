import os
import json

base_dir = r"C:\Users\Lenovo\Documents\primavera brain"
json_path = os.path.join(base_dir, "base_de_datos_primavera.json")
md_path = os.path.join(base_dir, "base_de_datos_primavera.md")

def main():
    print("Running database validation checks...")
    
    # Check file existence
    assert os.path.exists(json_path), "JSON database file does not exist!"
    assert os.path.exists(md_path), "Markdown database file does not exist!"
    print("- Database files exist.")

    # Load JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
    print("- JSON database parsed successfully.")

    # Validate keys
    required_keys = ['metadata', 'packages', 'venues', 'cotizaciones_reales', 'expo_boda_2026', 'croquis_y_planos', 'agentes_conversacionales']
    for k in required_keys:
        assert k in db, f"Key '{k}' is missing from the master database!"
    print("- All required keys are present.")

    # Validate venues
    venue_names = [v.get("nombre_venue") or v.get("name") for v in db["venues"]]
    assert "Villa Di Fiori" in venue_names or "Villa di Fiori" in venue_names, "Villa Di Fiori is missing from venues!"
    assert "Jardín Solaire" in venue_names or "Salón & Jardín Solaire" in venue_names, "Jardín Solaire is missing from venues!"
    print(f"- Venues validated: Found {len(db['venues'])} venues.")

    # Validate cotizaciones
    clients = [c.get("cliente") for c in db["cotizaciones_reales"]]
    expected_clients = [
        "XV Años Antonio (Propuesta Premium)",
        "Aniversario Viviana (Propuesta Premium)",
        "Sistema DIF / Lic. Claudia López",
        "Edimael Becerra",
        "Sra. Sandra",
        "Viky (Propuesta Premium Solaire)"
    ]
    for client in expected_clients:
        assert any(client in c for c in clients), f"Cotización for '{client}' is missing!"
    print(f"- Cotizaciones validated: Found {len(db['cotizaciones_reales'])} real quotes.")

    # Validate croquis
    assert "yolomecatl" in db["croquis_y_planos"], "Yolomecatl croquis is missing!"
    assert "centro_presidente" in db["croquis_y_planos"], "Centro Presidente croquis is missing!"
    assert "jardin_la_flor" in db["croquis_y_planos"], "Jardin La Flor plano is missing!"
    print("- Croquis layouts validated.")

    # Validate expo Boda
    expo = db["expo_boda_2026"]
    assert "leads_capturados" in expo, "Leads capturados list is missing in expo!"
    assert len(expo["leads_capturados"]) == 52, f"Leads count mismatch! Expected 52, found {len(expo['leads_capturados'])}."
    assert "proveedores_expositores" in expo, "Exhibitors list is missing in expo!"
    assert len(expo["proveedores_expositores"]) == 11, f"Exhibitor count mismatch! Expected 11, found {len(expo['proveedores_expositores'])}."
    print("- Expo Boda 2026 leads and exhibitors validated.")

    # Validate agent Sofia
    assert db["agentes_conversacionales"].get("agente") == "Agente Sofía", "Agent Sofia data is invalid!"
    print("- Sofia Legacy Agent validated.")

    print("\nDATABASE INTEGRITY CHECKS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
