def calculate_score(warheads, lipinski_violations, pains_alert=False):
    """
    Calculate a simple covalent-inhibitor prioritization score.

    This is not a biological activity prediction. It is a transparent first-pass
    prioritization score for early screening.
    """
    score = 0

    if warheads:
        score += 70

    score -= 10 * lipinski_violations

    if len(warheads) > 1:
        score -= 5 * (len(warheads) - 1)

    if pains_alert:
        score -= 30

    return max(score, 0)
