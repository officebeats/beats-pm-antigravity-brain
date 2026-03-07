with open('.agent/rules/GEMINI.md', 'r', encoding='utf-8') as f:
    content = f.read()
with open('KERNEL.md', 'w', encoding='utf-8') as f:
    f.write(content)
print("File copied successfully")
