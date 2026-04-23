import sys

html_path = '/Users/vishnu/Desktop/cognitive/quiz-app/CogniQuiz.html'
replacement_path = '/Users/vishnu/Desktop/cognitive/scratch/replacement_2018.txt'

with open(html_path, 'r') as f:
    lines = f.readlines()

with open(replacement_path, 'r') as f:
    replacement = f.read()

# Lines are 1-indexed in view_file
# 5268 to 6561 (0-indexed: 5267 to 6560)
start_idx = 5267
end_idx = 6560

new_lines = lines[:start_idx] + [replacement + "\n"] + lines[end_idx+1:]

with open(html_path, 'w') as f:
    f.writelines(new_lines)

print("Successfully updated CogniQuiz.html")
