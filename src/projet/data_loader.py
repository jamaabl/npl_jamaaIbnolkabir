import os
import glob

def charger_donnees_locales():
    # On définit le chemin exact vers votre dossier 'data'
    # D'après votre capture, il est ici : C:\Users\GM\Desktop\projet nlp\projet\data
    chemin_du_dossier_data = r"C:\Users\GM\Desktop\projet nlp\projet\data"
    
    print(f"🔍 Recherche de fichiers dans : {chemin_du_dossier_data}")
    
    if not os.path.exists(chemin_du_dossier_data):
        print("❌ Le dossier 'data' est introuvable à ce chemin.")
        return []

    # Chercher tous les fichiers .txt et .xml
    fichiers_txt = glob.glob(os.path.join(chemin_du_dossier_data, "**", "*.txt"), recursive=True)
    fichiers_xml = glob.glob(os.path.join(chemin_du_dossier_data, "**", "*.xml"), recursive=True)
    tous_les_fichiers = fichiers_txt + fichiers_xml
    
    if not tous_les_fichiers:
        print("❌ Aucun fichier .txt ou .xml trouvé.")
        print("👉 Avez-vous bien extrait les fichiers .rar avec 7-Zip/WinRAR dans le dossier 'data' ?")
        return []

    print(f"✅ {len(tous_les_fichiers)} fichiers trouvés au total.")
    
    documents = []
    # On limite à 100 fichiers pour que le test soit rapide
    for fichier in tous_les_fichiers[:100]: 
        try:
            with open(fichier, 'r', encoding='utf-8', errors='ignore') as f:
                contenu = f.read()
                if len(contenu) > 200: 
                    documents.append(contenu)
        except Exception as e:
            pass
            
    print(f"📚 Chargement terminé. {len(documents)} documents valides en mémoire.")
    return documents

if __name__ == "__main__":
    docs = charger_donnees_locales()
    if docs:
        print("\n--- Extrait du premier document chargé ---")
        print(docs[0][:500])