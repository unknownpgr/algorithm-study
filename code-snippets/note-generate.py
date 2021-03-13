'''
Generate a markdown note for print
'''

from os import listdir, path
file = path.basename(__file__)
dir = path.dirname(__file__)
with open('Note.md', 'w', encoding='utf-8') as o:
    o.write('# Algorithm Code Snippets\n')
    for source in listdir(dir):
        if not source.endswith('.py'):
            continue
        if source == file:
            continue
        o.write('## '+source.replace('.py', '').capitalize()+'\n')
        o.write('```python\n')
        with open(path.join(dir, source), 'r', encoding='utf-8') as s:
            for line in s:
                o.write(line)
        o.write('```\n')
