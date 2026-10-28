from preprocess import clean_text, remove_stopwords, segment_text
from model import detect_plagiarism
from data_loader import charger_donnees_locales

def main():
    print("--- DÉMARRAGE DU PIPELINE ---")
    
    # 1. Acquisition (Chapitre 2)
    documents = charger_donnees_locales()
    if not documents:
        print("Arrêt : pas de données trouvées.")
        return

    if len(documents) < 2:
        print("Il faut au moins 2 documents pour comparer.")
        return

    # On prend les deux premiers documents
    doc_source = documents[0]
    doc_suspect = documents[1]

    # 2. Prétraitement (Chapitre 2)
    print("Prétraitement en cours...")
    src_clean = remove_stopwords(clean_text(doc_source))
    sus_clean = remove_stopwords(clean_text(doc_suspect))

    # 3. Segmentation
    source_segments = segment_text(src_clean, window_size=2)
    sus_segments = segment_text(sus_clean, window_size=2)

    # 4. Représentation et Modélisation (Chapitre 3 & 4)
    print("Détection de plagiat...")
    resultats = detect_plagiarism(sus_segments, source_segments, threshold=0.5)

    # 5. Évaluation (Chapitre 4)
    print(f"\n--- RÉSULTATS ({len(resultats)} détections) ---")
    if not resultats:
        print("Aucun plagiat détecté.")
    else:
        for i, res in enumerate(resultats[:5]):
            print(f"\nMatch {i+1} (Score: {res['score']:.2f})")
            print(f"Suspect : {res['suspicious'][:150]}...")
            print(f"Source  : {res['source'][:150]}...")

if __name__ == "__main__":
    main()