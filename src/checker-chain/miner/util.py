from .llm import ReviewScoreSchema, ScoreBreakdown

def get_overall_score(ai_response: ReviewScoreSchema):
    if (isinstance(ai_response, ReviewScoreSchema)):
        breakdown = ai_response.breakdown
    else:
        return None
    # Default weights (Modify these as needed)
    # Sum of Weights should always equal 10 for proper overall weight to be within 100
    weights = {
        "project": 1,
        "userbase": 1,
        "utility": 1,
        "security": 1.5,
        "team": 0.5,
        "tokenomics": 1,
        "marketing": 1.5,
        "roadmap": 1,
        "clarity": 0.5,
        "partnerships": 1
    }

    field_names = ScoreBreakdown.model_fields.keys()
    scores = {field: getattr(breakdown, field) for field in field_names}

    overall_score: float = sum(
        float(scores[key]) * weights[key] for key in scores)

    return round(overall_score, 2)  # Rounds the score to 2 decimal places

