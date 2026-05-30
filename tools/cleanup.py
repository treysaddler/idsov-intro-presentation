import re

with open('research/2026-05-21-carson-intro-to-idsov-transcript.txt', 'r') as f:
    text = f.read()

# Replace specific misspellings/terms based on context
replacements = {
    r'\bInry\b': 'INBRE',
    r'\bINRI\b': 'INBRE',
    r'\binbre\b': 'INBRE',
    r'\bPBLO\b': 'Pueblo',
    r'\bpblo\b': 'Pueblo',
    r'\boking\b': 'Ohkay Owingeh',
    r'\bOKing\b': 'Ohkay Owingeh',
    r'\bOkawing\b': 'Ohkay Owingeh',
    r'\bTaywa\b': 'Tewa',
    r'\btaywa\b': 'Tewa',
    r'\bMelan Enid Zuckermanman\b': 'Mel and Enid Zuckerman',
    r'\bpost-doal\b': 'post-doctoral',
    r'\bpostto\b': 'postdoc',
    r'\bHoni\b': 'Haudenosaunee',
    r'\bco 19\b': 'COVID-19',
    r'\bco\b': 'COVID-19',  # "co pandemic" etc
    r'\btri\b': 'tribe',
    r'\bCBP CBPR\b': 'CBPR',
    r'\bTonal Awesome\b': 'Tohono O\'odham',
    r'\bMariam\b': 'Meriam',
    r'\bDA\b': 'Dawes Act',
    r'\bKenho\b': 'Cayetano',
    r'\bLeo\b': 'Alito',
    r'\bHIPPA\b': 'HIPAA',
    r'\bFURba\b': 'FERPA',
    r'\bhorny\b': 'Hopi',
    r'\bsta\b': 'Stata',
    r'\bbeta forward\b': 'Native Forward',
}

for old, new in replacements.items():
    text = re.sub(old, new, text, flags=re.IGNORECASE)

# Remove filler words
text = re.sub(r'\b(um|uh|you know|like|basically|kind of|sort of)\b,?\s*', '', text, flags=re.IGNORECASE)

# Fix double words
text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text, flags=re.IGNORECASE)

# Sentence case
def sentence_case(match):
    return match.group(1) + match.group(2).upper()

text = re.sub(r'(^|[.!?]\s+|\n+)([a-z])', sentence_case, text)

# Write back
with open('research/2026-05-21-carson-intro-to-idsov-transcript.txt', 'w') as f:
    f.write(text)
