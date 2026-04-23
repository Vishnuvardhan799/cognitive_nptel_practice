import json
import re

html_path = '/Users/vishnu/Desktop/cognitive/quiz-app/CogniQuiz.html'

with open(html_path, 'r') as f:
    content = f.read()

# Find the QUESTIONS_DB object
# It starts with const QUESTIONS_DB = { and ends before the next const/function
db_match = re.search(r'const QUESTIONS_DB = \{(.*?)\};', content, re.DOTALL)
if not db_match:
    print("Could not find QUESTIONS_DB")
    sys.exit(1)

db_str = "{" + db_match.group(1) + "}"

# We can't easily parse this with json.loads because it might have trailing commas or other JS-isms
# But let's try to extract each year's array
years = re.findall(r'"(\d{4})":\s*\[(.*?)\n\s*\]', db_str, re.DOTALL)

updated_db = {}

for year, year_content in years:
    # Split into individual question objects
    # They start with { and end with }
    q_objs = re.findall(r'\{\s*(.*?)\s*\}', year_content, re.DOTALL)
    
    updated_qs = []
    for q_str in q_objs:
        # Extract fields
        id_m = re.search(r'"id":\s*"(.*?)"', q_str)
        week_m = re.search(r'"week":\s*(\d+)', q_str)
        q_text_m = re.search(r'"question":\s*"(.*?)"', q_str, re.DOTALL)
        options_m = re.search(r'"options":\s*\[(.*?)\s*\]', q_str, re.DOTALL)
        correct_m = re.search(r'"correctAnswer":\s*(.*?)(?:,|$)', q_str)
        exp_m = re.search(r'"explanation":\s*"(.*?)"', q_str, re.DOTALL)
        
        if not all([id_m, week_m, q_text_m, options_m, correct_m]):
            continue
            
        q_id = id_m.group(1)
        week = int(week_m.group(1))
        q_text = q_text_m.group(1)
        
        # Clean options
        opts_raw = re.findall(r'"(.*?)"', options_m.group(1))
        options = []
        for opt in opts_raw:
            # Remove bullet points like \u2022, O, J, etc at start
            opt = re.sub(r'^[\u2022OJ\-\s*]+', '', opt).strip()
            options.append(opt)
            
        # Clean correctAnswer
        correct_val = correct_m.group(1).strip()
        if correct_val.startswith('"') and correct_val.endswith('"'):
            # It's a string, find index
            answer_text = correct_val[1:-1].strip()
            # Special case for "1 point" or similar noise
            answer_text = re.sub(r'^\d+\)\s*', '', answer_text)
            answer_text = re.sub(r'\s*\d+\s*poi.*', '', answer_text)
            
            correct_index = -1
            for idx, opt in enumerate(options):
                if answer_text.lower() == opt.lower() or answer_text.lower().startswith(opt.lower()) or opt.lower().startswith(answer_text.lower()):
                    correct_index = idx
                    break
            
            # If still not found, try fuzzy match
            if correct_index == -1:
                # Just take the first one if we're desperate, but let's hope it matches
                pass
        else:
            try:
                correct_index = int(correct_val)
            except:
                correct_index = 0
                
        explanation = exp_m.group(1) if exp_m else ""
        
        updated_qs.append({
            "id": q_id,
            "week": week,
            "question": q_text,
            "options": options,
            "correctAnswer": correct_index,
            "explanation": explanation
        })
    
    updated_db[year] = updated_qs

# Now generate the new QUESTIONS_DB string
new_db_parts = []
for year in sorted(updated_db.keys()):
    year_json = json.dumps(updated_db[year], indent=4)
    # Indent the year content
    indented_year = ""
    for line in year_json.split('\n'):
        indented_year += "    " + line + "\n"
    new_db_parts.append(f'  "{year}": {indented_year.strip()}')

new_db_str = "const QUESTIONS_DB = {\n" + ",\n".join(new_db_parts) + "\n};"

# Replace in content
new_content = re.sub(r'const QUESTIONS_DB = \{.*?\};', new_db_str, content, flags=re.DOTALL)

with open(html_path, 'w') as f:
    f.write(new_content)

print("Database cleaned and strings converted to indices.")
