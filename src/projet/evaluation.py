from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

def evaluer_modeles(y_true, y_pred):
    """
    Calcule les métriques vues en cours (Chapitre 4).
    y_true : les vraies étiquettes (1 = plagiat, 0 = non plagiat)
    y_pred : les prédictions de notre modèle
    """
    print("\n--- RAPPORT D'ÉVALUATION ---")
    
    # Calcul des métriques
    precision = precision_score(y_true, y_pred, zero_division=0)
    rappel = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    
    print(f"Précision : {precision:.4f}")
    print(f"Rappel    : {rappel:.4f}")
    print(f"F1-Score  : {f1:.4f}")
    
    # Matrice de confusion (comme vu dans la diapositive 34)
    print("\nMatrice de confusion :")
    print(confusion_matrix(y_true, y_pred))

# Exemple de test pour vérifier que le script fonctionne (sans les vraies données)
if __name__ == "__main__":
    print("Test du script d'évaluation...")
    # Vraies étiquettes (ex: 1=plagiat, 0=original)
    y_vrai = [1, 0, 1, 1, 0, 0, 1, 0]
    # Prédictions de notre modèle
    y_predit = [1, 0, 0, 1, 0, 1, 1, 0]
    
    evaluer_modeles(y_vrai, y_predit)