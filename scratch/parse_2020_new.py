import json
import re

with open('/Users/vishnu/Desktop/cognitive/scratch/2020_raw_new.txt', 'r', encoding='utf-8') as f:
    content = f.read()

questions = []
# split into assessments
assessments = re.split(r'## Assessment (\d+):[^\n]*\n', content)

for i in range(1, len(assessments), 2):
    week_num = int(assessments[i])
    week_text = assessments[i+1]
    
    # split into questions
    # matches "* **1) " or "* **10) "
    q_blocks = re.split(r'\* \*\*(\d+)\) (.*?)\*\*\n', week_text)
    
    for j in range(1, len(q_blocks), 3):
        q_num = int(q_blocks[j])
        q_text = q_blocks[j+1].strip()
        q_body = q_blocks[j+2]
        
        options = []
        correct_ans_text = ""
        
        lines = q_body.strip().split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('* [cite_start]**Correct Answer:**'):
                correct_ans_text = line.split('**Correct Answer:**')[1].split('[cite:')[0].strip()
            elif line.startswith('* '):
                options.append(line[2:].strip())
        
        # find correct answer index
        correct_idx = -1
        for idx, opt in enumerate(options):
            if opt.lower() == correct_ans_text.lower():
                correct_idx = idx
                break
        
        if correct_idx == -1:
            print(f"Warning: Correct answer not found in options for W{week_num}Q{q_num}")
            print(f"Options: {options}")
            print(f"Correct ans: '{correct_ans_text}'")
        
        questions.append({
            "id": f"w{week_num}q{q_num}",
            "week": week_num,
            "question": q_text,
            "options": options,
            "correctAnswer": correct_idx,
            "explanation": ""
        })

print(f"Parsed {len(questions)} questions.")

with open('/Users/vishnu/Desktop/cognitive/scratch/2020_questions_clean_new.json', 'w') as f:
    json.dump(questions, f, indent=2)
