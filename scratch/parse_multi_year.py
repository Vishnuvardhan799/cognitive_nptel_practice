import json
import re

def clean_text(text):
    if not text: return ""
    text = re.sub(r'\[cite_start\]', '', text)
    text = re.sub(r'\[cite: [\d, \-]+\]', '', text)
    text = re.sub(r'\*\*', '', text)
    text = text.replace('"', '\"')
    text = text.strip().strip('_').strip()
    return text

def parse_file(filepath, year):
    with open(filepath, 'r') as f:
        content = f.read()
    
    sections = re.split(r'### \*\*.*?\*\*', content)
    # The first split is usually empty or intro text
    if len(sections) > 1:
        sections = sections[1:]
    
    all_questions = []
    
    for i, section in enumerate(sections):
        week_num = i + 1
        # Each question starts with *
        q_blocks = re.split(r'\n\* ', section)
        if len(q_blocks) > 1:
            q_blocks = q_blocks[1:]
        
        for j, block in enumerate(q_blocks):
            lines = [l.strip() for l in block.split('\n') if l.strip()]
            if not lines: continue
            
            # Question line
            q_text = ""
            options = []
            ans_text = ""
            
            for line in lines:
                if 'Question' in line and ':' in line:
                    q_text = clean_text(line.split(':', 1)[1])
                elif 'Options:' in line:
                    opts_raw = line.split(':', 1)[1]
                    # Options can be separated by ; or , or [cite]
                    # First remove cites
                    opts_clean = clean_text(opts_raw)
                    # Split by common separators
                    opts_semi = [clean_text(o) for o in opts_clean.split(';')]
                    opts_comma = [clean_text(o) for o in opts_clean.split(',')]
                    
                    # Choose the separator that yields exactly 4 options
                    if len(opts_semi) == 4 and len(opts_comma) != 4:
                        options = opts_semi
                    elif len(opts_comma) == 4:
                        options = opts_comma
                    else:
                        options = opts_comma
                elif 'Accepted Answer:' in line:
                    ans_text = clean_text(line.split(':', 1)[1])
            
            # Final cleanup
            if not q_text and lines:
                # Fallback for questions without "Question X:" prefix
                q_text = clean_text(lines[0])
            
            # Ensure at least 4 options
            cleaned_options = []
            for opt in options:
                opt = clean_text(opt)
                if not opt or "obscured" in opt.lower() or opt == "*": continue
                if opt not in cleaned_options: cleaned_options.append(opt)
            
            if clean_text(ans_text) and clean_text(ans_text) not in cleaned_options:
                cleaned_options.append(clean_text(ans_text))
            
            distractors = ["Functionalism", "Structuralism", "Behaviorism", "Gestalt psychology", "None of the above", "Information processing approach"]
            for d in distractors:
                if len(cleaned_options) >= 4: break
                if d not in cleaned_options: cleaned_options.append(d)
            
            # Find correct index
            correct_idx = 0
            for idx, opt in enumerate(cleaned_options):
                if clean_text(ans_text).lower() == opt.lower() or (ans_text and clean_text(ans_text).lower() in opt.lower()):
                    correct_idx = idx
                    break
            
            all_questions.append({
                "id": f"w{week_num}q{j+1}",
                "week": week_num,
                "question": q_text,
                "options": cleaned_options,
                "correctAnswer": correct_idx,
                "explanation": ""
            })
            
    return all_questions

db_2020 = parse_file('/Users/vishnu/Desktop/cognitive/scratch/2020_raw.txt', 2020)
db_2022 = parse_file('/Users/vishnu/Desktop/cognitive/scratch/2022_raw.txt', 2022)

with open('/Users/vishnu/Desktop/cognitive/scratch/2020_questions_v2.json', 'w') as f:
    json.dump(db_2020, f, indent=2)

with open('/Users/vishnu/Desktop/cognitive/scratch/2022_questions.json', 'w') as f:
    json.dump(db_2022, f, indent=2)

print(f"Parsed {len(db_2020)} questions for 2020 and {len(db_2022)} questions for 2022.")
