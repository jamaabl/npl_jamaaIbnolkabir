import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Télécharger les ressources nécessaires de NLTK
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

def clean_text(text):
    """
    Normalisation et nettoyage complet.
    1. Supprime les métadonnées XML (balises <...>)
    2. Met en minuscules
    3. Supprime les caractères spéciaux
    """
    # 1. Suppression des métadonnées XML (balises HTML/XML)
    text = re.sub(r'<[^>]+>', ' ', text)
    
    # 2. Mise en minuscules
    text = text.lower()
    
    # 3. Suppression des caractères spéciaux (garde les lettres et les espaces)
    text = re.sub(r'[^a-zàâçéèêëîïôûùüÿñæœ\s]', ' ', text)
    
    # 4. Suppression des espaces multiples
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text, lang='english'):
    """Suppression des stopwords (Chapitre 2)"""
    stop_words = set(stopwords.words(lang))
    tokens = word_tokenize(text)
    # Garder les mots qui ne sont pas des stopwords et qui sont alphabétiques
    filtered_tokens = [w for w in tokens if w not in stop_words and w.isalpha()]
    return " ".join(filtered_tokens)
def segment_text(text, window_size=2, step=1):
    """
    Découpe en blocs de phrases (fenêtres glissantes).
    Si le texte n'a plus de ponctuation (à cause du nettoyage), 
    on découpe par blocs de mots pour éviter les erreurs.
    """
    # On essaie de découper par phrases
    sentences = sent_tokenize(text)
    
    # Si on n'a qu'une seule phrase (car la ponctuation a été supprimée)
    if len(sentences) <= 1:
        # On découpe par mots (par exemple, des blocs de 20 mots)
        mots = text.split()
        taille_bloc = 20
        sentences = [" ".join(mots[i:i+taille_bloc]) for i in range(0, len(mots), taille_bloc)]

    segments = []
    for i in range(0, len(sentences) - window_size + 1, step):
        segment = " ".join(sentences[i:i + window_size])
        segments.append(segment)
    return segments