from representation import create_minhash

def detect_plagiarism(suspicious_segments, source_segments, threshold=0.5):
    """
    Compare les segments suspects avec les sources.
    """
    detections = []
    # Pré-calcul des MinHash pour les sources
    source_minhashes = [(seg, create_minhash(seg)) for seg in source_segments]

    for sus_seg in suspicious_segments:
        sus_hash = create_minhash(sus_seg)
        best_match = None
        best_score = 0.0

        for src_seg, src_hash in source_minhashes:
            # Similarité de Jaccard
            score = sus_hash.jaccard(src_hash) 
            if score > best_score:
                best_score = score
                best_match = src_seg

        # Si le score dépasse le seuil, on considère que c'est du plagiat
        if best_score >= threshold:
            detections.append({
                "suspicious": sus_seg,
                "source": best_match,
                "score": best_score
            })
    return detections