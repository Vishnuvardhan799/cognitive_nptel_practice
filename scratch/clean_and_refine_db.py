import json
import re

def clean_text(text):
    if not text:
        return ""
    # Remove [cite_start], [cite: 123], [cite: 123, 456], etc.
    text = re.sub(r'\[cite_start\]', '', text)
    text = re.sub(r'\[cite: [\d, ]+\]', '', text)
    # Remove formatting artifacts like ** and _
    text = re.sub(r'\*\*', '', text)
    # Remove trailing underscores and spaces
    text = text.strip().strip('_').strip()
    return text

def fix_options(options, correct_answer_text):
    cleaned_options = []
    for opt in options:
        cleaned = clean_text(opt)
        if not cleaned or "obscured" in cleaned.lower() or cleaned == "*":
            continue
        if cleaned not in cleaned_options:
            cleaned_options.append(cleaned)
    
    # If correct answer is not in there, add it
    correct_clean = clean_text(correct_answer_text)
    if correct_clean and correct_clean not in cleaned_options:
        cleaned_options.append(correct_clean)
    
    # Fill up to 4 options
    distractors = ["Functionalism", "Structuralism", "Behaviorism", "Gestalt psychology", "None of the above", "Information processing approach"]
    for d in distractors:
        if len(cleaned_options) >= 4:
            break
        if d not in cleaned_options:
            cleaned_options.append(d)
            
    return cleaned_options

# Process 2018
with open('/Users/vishnu/Desktop/cognitive/scratch/2018_questions.json', 'r') as f:
    db_2018 = json.load(f)

for q in db_2018:
    original_options = q['options']
    ans_idx = q['correctAnswer']
    ans_text = original_options[ans_idx] if ans_idx >= 0 and ans_idx < len(original_options) else ""
    
    q['question'] = clean_text(q['question'])
    q['options'] = fix_options(original_options, ans_text)
    
    # Re-find correct index
    correct_clean = clean_text(ans_text)
    new_idx = -1
    for i, opt in enumerate(q['options']):
        if correct_clean.lower() == opt.lower() or (correct_clean and correct_clean.lower() in opt.lower()):
            new_idx = i
            break
    q['correctAnswer'] = new_idx if new_idx != -1 else 0

# Process 2020
with open('/Users/vishnu/Desktop/cognitive/scratch/2020_questions.json', 'r') as f:
    db_2020 = json.load(f)

for q in db_2020:
    original_options = q['options']
    ans_idx = q['correctAnswer']
    ans_text = original_options[ans_idx] if ans_idx >= 0 and ans_idx < len(original_options) else ""
    
    q['question'] = clean_text(q['question'])
    q['options'] = fix_options(original_options, ans_text)
    
    # Re-find correct index
    correct_clean = clean_text(ans_text)
    new_idx = -1
    for i, opt in enumerate(q['options']):
        if correct_clean.lower() == opt.lower() or (correct_clean and correct_clean.lower() in opt.lower()):
            new_idx = i
            break
    q['correctAnswer'] = new_idx if new_idx != -1 else 0

# Save cleaned versions
with open('/Users/vishnu/Desktop/cognitive/scratch/2018_questions_clean.json', 'w') as f:
    json.dump(db_2018, f, indent=2)

with open('/Users/vishnu/Desktop/cognitive/scratch/2020_questions_clean.json', 'w') as f:
    json.dump(db_2020, f, indent=2)

print("Cleaned 2018 and 2020 datasets.")
