import json

with open('/Users/vishnu/Desktop/cognitive/scratch/2025_questions.json') as f:
    db_2025 = json.load(f)

with open('/Users/vishnu/Desktop/cognitive/scratch/2026_questions.json') as f:
    db_2026 = json.load(f)

# Create a set of normalized questions for 2026
def normalize(text):
    return ''.join([c.lower() for c in text if c.isalnum()])

q2026_normalized = {normalize(q['question']) for q in db_2026}
q2026_id_map = {normalize(q['question']): q['id'] for q in db_2026}

differences = []

for q25 in db_2025:
    norm_q25 = normalize(q25['question'])
    if norm_q25 not in q2026_normalized:
        differences.append(f"Week {q25['week']} - Question '{q25['question']}'")

print(f"Out of 120 questions in 2025, {len(differences)} questions do NOT match the 2026 dataset.")
for diff in differences:
    print(f"- {diff}")
