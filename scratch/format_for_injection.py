import json

with open('/Users/vishnu/Desktop/cognitive/scratch/2018_questions.json', 'r') as f:
    data = json.load(f)

# Format each object with 4 spaces indent, and the whole thing indented by 4 spaces
formatted = json.dumps(data, indent=4)
# Indent the whole block
indented = ""
for line in formatted.split('\n'):
    if line.strip() == '[' or line.strip() == ']':
        continue
    indented += "    " + line + "\n"

# Remove trailing newline
indented = indented.rstrip()

with open('/Users/vishnu/Desktop/cognitive/scratch/replacement_2018.txt', 'w') as f:
    f.write(indented)
