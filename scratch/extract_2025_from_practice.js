const fs = require('fs');

const content = fs.readFileSync('/Users/vishnu/Library/Containers/net.whatsapp.WhatsApp/Data/tmp/documents/251CFBDA-8CD6-4DCD-BC1E-85B33DAE1804/practice-2025.html', 'utf8');

const match = content.match(/const WEEKS = ({[\s\S]*?});/);
if (!match) {
    console.error("Could not find WEEKS object");
    process.exit(1);
}

const weeksStr = match[1]
    .replace(/opts:/g, '"opts":')
    .replace(/ans:/g, '"ans":')
    .replace(/q:/g, '"q":')
    .replace(/label:/g, '"label":')
    .replace(/topic:/g, '"topic":')
    .replace(/color:/g, '"color":')
    .replace(/badge:/g, '"badge":')
    .replace(/pfill:/g, '"pfill":')
    .replace(/questions:/g, '"questions":')
    .replace(/(\d+):{/g, '"$1":{');

// evaluate it
const WEEKS = eval("(" + match[1] + ")");

const db_2025 = [];
for (let w = 1; w <= 12; w++) {
    if (WEEKS[w] && WEEKS[w].questions) {
        WEEKS[w].questions.forEach((q, qIdx) => {
            db_2025.push({
                id: `w${w}q${qIdx + 1}`,
                year: "2025",
                week: w,
                question: q.q,
                options: q.opts,
                answer: q.ans
            });
        });
    }
}

fs.writeFileSync('/Users/vishnu/Desktop/cognitive/scratch/2025_questions_correct.json', JSON.stringify(db_2025, null, 2));
console.log(`Extracted ${db_2025.length} correct 2025 questions!`);
