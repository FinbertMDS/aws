#!/usr/bin/env python3
import re


def add_answer_toggle(input_file, output_file):
    """
    Add toggle functionality to hide/show Answer and Suggested Answer lines
    """
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add CSS and JavaScript to the head section
    css_js = '''
<style>
.answer-section {
    display: none;
    margin: 10px 0;
    padding: 10px;
    background-color: #f8f9fa;
    border-left: 4px solid #007bff;
    border-radius: 4px;
}

.show-answer-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    margin: 10px 0;
}

.show-answer-btn:hover {
    background-color: #0056b3;
}

.show-answer-btn:focus {
    outline: none;
    box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
}
</style>

<script>
function toggleAnswer(buttonId) {
    const button = document.getElementById(buttonId);
    const answerSection = document.getElementById('answer-section-' + buttonId);
    
    if (answerSection.style.display === 'none' || answerSection.style.display === '') {
        answerSection.style.display = 'block';
        button.textContent = 'Hide Answer';
    } else {
        answerSection.style.display = 'none';
        button.textContent = 'Show Answer';
    }
}
</script>
'''
    
    # Insert CSS and JavaScript after the opening <head> tag
    if '<head>' in content:
        content = content.replace('<head>', '<head>' + css_js)
    else:
        # If no head tag, add it at the beginning
        content = '<head>' + css_js + '</head>' + content
    
    # Find and replace Answer and Suggested Answer sections
    # Pattern to match: <p><strong>Answer: X</strong></p>\n<p>Suggested Answer: X 🗳️</p>
    pattern = r'(<p><strong>Answer: [A-Z]</strong></p>\s*<p>Suggested Answer: [A-Z] 🗳️</p>)'
    
    def replace_with_toggle(match):
        answer_text = match.group(1)
        # Generate unique ID for this section
        import uuid
        section_id = str(uuid.uuid4())[:8]
        
        # Create the toggle structure
        toggle_html = f'''
<button id="{section_id}" class="show-answer-btn" onclick="toggleAnswer('{section_id}')">Show Answer</button>
<div id="answer-section-{section_id}" class="answer-section">
{answer_text}
</div>'''
        
        return toggle_html
    
    # Apply the replacement
    modified_content = re.sub(pattern, replace_with_toggle, content)
    
    # Write the modified content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"Modified file saved as: {output_file}")

if __name__ == "__main__":
    input_file = "aws-sap-c02-new.html"
    output_file = "aws-sap-c02-new_toggle.html"
    add_answer_toggle(input_file, output_file) 
