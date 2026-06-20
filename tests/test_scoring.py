from src.scoring import calculate_score


def test_score_with_warhead_no_violations():
    assert calculate_score(["acrylamide"], 0) == 70


def test_score_penalizes_lipinski_violations():
    assert calculate_score(["acrylamide"], 2) == 50


def test_score_without_warhead():
    assert calculate_score([], 0) == 0


def test_score_penalizes_pains():
    assert calculate_score(["acrylamide"], 0, pains_alert=True) == 40
