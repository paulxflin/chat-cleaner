with open('msg.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    clean = ':'.join(lines[i].split(':')[2:]).strip()
    lines[i] = clean
    
with open('clean-msg.txt','w') as f:
    f.write('\n'.join(lines))
