#!/usr/bin/env python3
import re


def fix_suggested_answers(input_file, output_file):
    """
    Move all "Suggested Answer:" lines to appear after "**Answer: **" lines 
    with a blank line in between.
    """
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into sections (each question)
    sections = content.split('\n\n----------------------------------------\n\n')
    
    fixed_sections = []
    
    for section in sections:
        if not section.strip():
            fixed_sections.append(section)
            continue
            
        lines = section.split('\n')
        fixed_lines = []
        suggested_answer = None
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check if this is a "Suggested Answer:" line
            if line.strip().startswith('Suggested Answer:'):
                suggested_answer = line
                i += 1
                continue
            
            # Check if this is the "**Answer: **" line
            if line.strip().startswith('**Answer:'):
                fixed_lines.append(line)
                if suggested_answer:
                    fixed_lines.append('')  # Add blank line
                    fixed_lines.append(suggested_answer)
                    suggested_answer = None
                i += 1
                continue
            
            # Regular line, just add it
            fixed_lines.append(line)
            i += 1
        
        # Handle any remaining suggested answer at the end
        if suggested_answer:
            fixed_lines.append(suggested_answer)
        
        fixed_sections.append('\n'.join(fixed_lines))
    
    # Write the fixed content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n----------------------------------------\n\n'.join(fixed_sections))
    
    print(f"Fixed file saved as: {output_file}")

if __name__ == "__main__":
    input_file = "aws-sap-c02-new-csa.md"
    output_file = "aws-sap-c02-new-csa_fixed.md"
    fix_suggested_answers(input_file, output_file) 
