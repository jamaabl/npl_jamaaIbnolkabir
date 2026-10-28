from datasketch import MinHash

def get_shingles(text, k=3):
    """
    Génère des n-grammes (shingles) de caractères.
    Le cours (Chapitre 3) parle des N-grammes.
    Ici on prend k=3 pour capter le contexte.
    """
    text = text.replace(" ", "") # On enlève les espaces pour les shingles de caractères
    return set(text[i:i+k] for i in range(len(text) - k + 1))

def create_minhash(text, num_perm=128):
    """Crée une signature MinHash pour un texte donné."""
    m = MinHash(num_perm=num_perm)
    for shingle in get_shingles(text):
        m.update(shingle.encode('utf-8'))
    return m