import json
import re

with open('/Users/vishnu/Desktop/cognitive/scratch/2025_raw.txt', 'r') as f:
    content = f.read()

# Remove the cite brackets like [cite_start] and [cite: 35090]
content = re.sub(r'\[cite_start\]|\[cite: \d+\]', '', content)

# Split into weeks using regex
sections = re.split(r'### \*\*Week \d+\*\*', content)
# The first element is empty string or preamble
sections = [s.strip() for s in sections if s.strip()]

db_2025 = []

for week_idx, section in enumerate(sections):
    week_num = week_idx + 1
    
    # Split into questions
    questions = re.split(r'\* \*\*Question \d+:\*\*', section)
    questions = [q.strip() for q in questions if q.strip()]
    
    for q_idx, q_text in enumerate(questions):
        # Extract question, options, and answer
        # Format:
        # <question text>
        # * **Options:** <options>
        # * **Accepted Answer:** <answer>
        
        parts = q_text.split('* **Options:**')
        if len(parts) != 2:
            continue
        
        question = parts[0].strip()
        rest = parts[1]
        
        parts2 = rest.split('* **Accepted Answer:**')
        if len(parts2) != 2:
            continue
            
        options_str = parts2[0].strip()
        answer = parts2[1].strip()
        
        # Split options
        if ';' in options_str:
            options = [o.strip() for o in options_str.split(';')]
        else:
            options = [o.strip() for o in options_str.split(',')]
            
        # Clean options
        options = [o for o in options if o]
        
        # Ensure 4 options
        while len(options) < 4:
            if "Behaviorism" not in options: options.append("Behaviorism")
            elif "Structuralism" not in options: options.append("Structuralism")
            elif "Functionalism" not in options: options.append("Functionalism")
            else: options.append("Gestalt")
            
        # Add to db
        db_2025.append({
            "id": f"w{week_num}q{q_idx+1}",
            "year": "2025",
            "week": week_num,
            "question": question,
            "options": options[:4],
            "answer": answer
        })

with open('/Users/vishnu/Desktop/cognitive/scratch/2025_questions.json', 'w') as f:
    json.dump(db_2025, f, indent=2)

print(f"Parsed {len(db_2025)} questions for 2025.")
