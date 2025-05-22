from rest_framework.decorators import api_view
from rest_framework.response import Response

# Dummy university data
universities = [
    {
        "name": "MIT",
        "country": "United States",
        "ranking": 1,
        "tuition": 53000,
        "notes": "Top-ranked globally, excellent Computer Science program."
    },
    {
        "name": "Stanford University",
        "country": "United States",
        "ranking": 2,
        "tuition": 54000,
        "notes": "Strong research culture and tech startup connections."
    },
    {
        "name": "University of Cambridge",
        "country": "United Kingdom",
        "ranking": 3,
        "tuition": 40000,
        "notes": "Prestigious with rigorous academics in sciences."
    },
    {
        "name": "University of Toronto",
        "country": "Canada",
        "ranking": 18,
        "tuition": 32000,
        "notes": "Highly ranked in North America with diverse programs."
    },
    {
        "name": "National University of Singapore (NUS)",
        "country": "Singapore",
        "ranking": 11,
        "tuition": 28000,
        "notes": "Leading Asian university with strong engineering focus."
    },
]

@api_view(['POST'])
def recommend_universities(request):
    return Response({"recommendation":universities})