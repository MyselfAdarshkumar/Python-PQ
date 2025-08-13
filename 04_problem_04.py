# Template letter
letter = '''Dear <|Name|>,
        You are selected!
        <|Date|>'''

# Replace placeholders
replace_letter = letter.replace("<|Name|>", "Adarsh")
replace_letter = replace_letter.replace("<|Date|>", "22/12/2025")

# Print the final letter
print(replace_letter)
