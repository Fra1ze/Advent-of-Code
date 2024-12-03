# Ensure day3.txt ends with 2 empty lines!
print('Part1')
import re
this_line_idx_vals = []
prev_line = ''
this_line = ''
next_line = ''
total = 0
lineno = 1
with open('day3.txt') as f:
    for line in f:
        prev_line = this_line
        this_line = next_line
        next_line = line
        matches = list(re.finditer(r'(\d+)', this_line))
        this_line_idx_vals = [(match.start(0)-1, match.end(0), int(match.group(0))) for match in matches]
        print('##################################')
        print(f'prevli={lineno-1}: {prev_line}', end='')
        print(f'lineno={lineno}: {this_line}', end='')
        print(f'nextli={lineno+1}: {next_line}', end='')
        for begin, end, val in this_line_idx_vals:
            print(f'begin={begin} end={end} val={val}')
            found = False
            if begin >= 0 and re.search(r'[^0-9.]', str(this_line[begin])) is not None:
                print('matched begin')
                total += val
                continue
            if this_line[end] != '\n' and re.search(r'[^0-9.]', str(this_line[end])) is not None:
                print('matched end')
                total += val
                continue
            if re.search(r'[^0-9.]', prev_line[begin:end+1]) is not None:
                print('matched prev_line')
                total += val
                continue
            if re.search(r'[^0-9.]', next_line[begin:end+1]) is not None:
                print('matched next_line')
                total += val
                continue
        lineno += 1
print(f'total={total}')

print('Part2')
this_line_idx_vals = []
prev_line = '\n'
this_line = '\n'
next_line = '\n'
total = 0
lineno = 1
with open('day3.txt') as f:
    for line in f:
        prev_line = this_line
        this_line = next_line
        next_line = line
        matches = list(re.finditer(r'\*', this_line))
        this_line_idx_vals = [(match.start(0)-1, match.end(0)) for match in matches]
        print('##################################')
        print(f'prevli={lineno-1}: {prev_line}', end='')
        print(f'lineno={lineno}: {this_line}', end='')
        print(f'nextli={lineno+1}: {next_line}', end='')
        for begin, end in this_line_idx_vals:
            print(f'begin={begin} end={end} val={val}')
            found = False
            parts = []
            if begin >= 0 and this_line[begin].isdigit():
                print('matched begin')
                idx = begin-1
                s = this_line[begin]
                while idx >= 0 and this_line[idx].isdigit():
                    s = this_line[idx] + s
                    idx -= 1
                parts.append(int(s))
            if this_line[end].isdigit():
                print('matched end')
                idx = end+1
                s = this_line[end]
                while this_line[idx].isdigit():
                    s = s + this_line[idx]
                    idx += 1
                parts.append(int(s))
            for adj_line in (prev_line, next_line):
                if adj_line[begin].isdigit():
                    print('matched adj_line (1)')
                    idx = begin-1
                    s = adj_line[begin]
                    while idx >= 0 and adj_line[idx].isdigit():
                        s = adj_line[idx] + s
                        idx -= 1
                    idx = begin+1
                    while adj_line[idx].isdigit():
                        s = s + adj_line[idx]
                        idx += 1
                    parts.append(int(s))
                # elif ensures "if" didnt add this number yet
                elif adj_line[begin+1].isdigit():
                    print('matched adj_line (2)')
                    idx = begin+2
                    s = adj_line[begin+1]
                    while adj_line[idx].isdigit():
                        s = s + adj_line[idx]
                        idx += 1
                    parts.append(int(s))
                # "not" condition ensures "elif" didnt add this yet
                if adj_line[begin+2].isdigit() and not adj_line[begin+1].isdigit():
                    print('matched adj_line (3)')
                    idx = begin+3
                    s = adj_line[begin+2]
                    while adj_line[idx].isdigit():
                        s = s + adj_line[idx]
                        idx += 1
                    parts.append(int(s))
            if len(parts) is 2:
                print(f'add gear ratio {parts[0]}*{parts[1]}')
                total += parts[0]*parts[1]
        lineno += 1
print(f'total={total}')