import json

html_path = '/Users/vishnu/Desktop/cognitive/quiz-app/CogniQuiz.html'

with open('/Users/vishnu/Desktop/cognitive/scratch/2018_questions_clean.json', 'r') as f:
    db_2018 = json.load(f)

with open('/Users/vishnu/Desktop/cognitive/scratch/2020_questions_v2.json', 'r') as f:
    db_2020 = json.load(f)

with open('/Users/vishnu/Desktop/cognitive/scratch/2022_questions.json', 'r') as f:
    db_2022 = json.load(f)

with open('/Users/vishnu/Desktop/cognitive/scratch/2025_questions_correct.json', 'r') as f:
    db_2025 = json.load(f)

with open('/Users/vishnu/Desktop/cognitive/scratch/2026_questions.json', 'r') as f:
    db_2026 = json.load(f)

with open(html_path, 'r') as f:
    content = f.read()

# Define the full QUESTIONS_DB object
db_obj = {
    "2018": db_2018,
    "2020": db_2020,
    "2022": db_2022,
    "2025": db_2025,
    "2026": db_2026
}

# Stringify with indentation
db_str = "const QUESTIONS_DB = " + json.dumps(db_obj, indent=2) + ";"

marker_start = "const QUESTIONS_DB = {"
marker_end = "};"

# Find the start of the DB
start_idx = content.find(marker_start)
if start_idx == -1:
    print("Could not find marker_start")
    exit(1)

# Find the end of the DB after the start
end_idx = content.find(marker_end, start_idx)
if end_idx == -1:
    print("Could not find marker_end")
    exit(1)

# The end_idx is the start of "};", so we need to include those 2 characters
end_idx += 2

new_content = content[:start_idx] + db_str + content[end_idx:]

with open(html_path, 'w') as f:
    f.write(new_content)

print("Successfully injected 2018, 2020 (v2), and 2022 data into CogniQuiz.html")
