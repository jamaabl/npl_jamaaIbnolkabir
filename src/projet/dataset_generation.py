import os
import xml.etree.ElementTree as ET
import pandas as pd

def generer_dataset():
    print("--- EXTRACTION DU DATASET PAN-PC-11 ---")
    
    chemin_data = r"C:\Users\GM\Desktop\projet nlp\projet\data\pan-plagiarism-corpus-2011"
    
    # 1. Trouver UNIQUEMENT les fichiers XML dans le dossier 'suspicious-documents'
    print("Recherche des fichiers XML suspects...")
    fichiers_xml = []
    for root, dirs, files in os.walk(chemin_data):
        # On ne garde que les fichiers dans un dossier contenant 'suspicious'
        if 'suspicious' in root.lower():
            for file in files:
                if file.endswith('.xml'):
                    fichiers_xml.append(os.path.join(root, file))

    print(f"✅ {len(fichiers_xml)} fichiers XML suspects trouvés.")
    
  
    
    donnees = []
    fichiers_analyses = 0
    
    for xml_file in fichiers_xml:
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # Le nom du document suspect
            doc_suspect = os.path.basename(xml_file).replace('.xml', '.txt')
            
            # On va chercher TOUTES les balises qui ont un attribut 'source_reference'
            # C'est la méthode la plus fiable pour ce corpus
            for elem in root.iter():
                source_ref = elem.get('source_reference')
                if source_ref:
                    type_plagiat = elem.get('type', 'inconnu')
                    this_offset = int(elem.get('this_offset', 0))
                    this_length = int(elem.get('this_length', 0))
                    
                    donnees.append({
                        'document_suspect': doc_suspect,
                        'source_reference': source_ref,
                        'type_plagiat': type_plagiat,
                        'offset_debut': this_offset,
                        'longueur': this_length
                    })
            fichiers_analyses += 1
            
        except Exception as e:
            pass

    # Créer le DataFrame
    df = pd.DataFrame(donnees)
    
    if df.empty:
        print("❌ Toujours aucune annotation trouvée.")
        if fichiers_xml:
            print(f"\n--- Aperçu du fichier XML : {os.path.basename(fichiers_xml[0])} ---")
            with open(fichiers_xml[0], 'r', encoding='utf-8', errors='ignore') as f:
                print(f.read()[:1000])
    else:
        print(f"\n✅ Dataset généré ! {len(df)} annotations trouvées dans {fichiers_analyses} fichiers.")
        print("\nAperçu des données :")
        print(df.head(10))
        
        # Sauvegarde en CSV
        chemin_csv = os.path.join(os.path.dirname(__file__), "../../dataset_plagiat.csv")
        df.to_csv(chemin_csv, index=False)
        print(f"\n💾 Dataset sauvegardé dans : {chemin_csv}")

if __name__ == "__main__":
    generer_dataset()