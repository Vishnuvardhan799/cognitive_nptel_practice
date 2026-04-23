import json

with open('/Users/vishnu/Desktop/cognitive/scratch/2025_questions.json') as f:
    db_pasted = json.load(f)

with open('/Users/vishnu/Desktop/cognitive/scratch/2025_questions_from_link.json') as f:
    db_link = json.load(f)

def normalize(text):
    return ''.join([c.lower() for c in text if c.isalnum()])

pasted_normalized = {normalize(q['question']) for q in db_pasted}
pasted_map = {normalize(q['question']): q for q in db_pasted}

link_normalized = {normalize(q['question']) for q in db_link}
link_map = {normalize(q['question']): q for q in db_link}

mismatches = []

# Questions in link but not pasted
for norm_q in link_normalized:
    if norm_q not in pasted_normalized:
        q = link_map[norm_q]
        mismatches.append(f"IN LINK BUT NOT PASTED: Week {q['week']} - {q['question']}")

# Questions pasted but not in link
for norm_q in pasted_normalized:
    if norm_q not in link_normalized:
        q = pasted_map[norm_q]
        mismatches.append(f"PASTED BUT NOT IN LINK: Week {q['week']} - {q['question']}")

# Check if same questions have different answers or options
for norm_q in link_normalized:
    if norm_q in pasted_normalized:
        q_link = link_map[norm_q]
        q_pasted = pasted_map[norm_q]
        
        ans_link_text = q_link['options'][q_link['correctAnswer']] if 'correctAnswer' in q_link else ""
        ans_link = normalize(ans_link_text)
        ans_pasted = normalize(q_pasted['answer'])
        
        if ans_link != ans_pasted:
            mismatches.append(f"ANSWER MISMATCH: Week {q_link['week']} - '{q_link['question']}' | Link Answer: {ans_link_text} | Pasted Answer: {q_pasted['answer']}")

if not mismatches:
    print("0 mismatches found. The questions and answers match perfectly!")
else:
    print(f"Found {len(mismatches)} mismatches:")
    for m in mismatches:
        print(f"- {m}")
