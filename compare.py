import difflib, os, re, sys
pattern = r"\/\/\s*(<>|[<>-])?\s*#WJ\s*\d{4}-\d{2}-\d{2}\s*([\s\S]*?)?\s*(\/\/.*)?"

def check_file(base_file, modified_file):
    for p in (base_file, modified_file):
        if not os.path.exists(p):
            print(f"[Error] {p} does not exist.")
            return False
        if os.path.getsize(p) == 0:
            print(f"[Error] {p} is empty.")
            return False
    return True

def read_files(base_file, modified_file):
    with open(base_file, 'r') as f1, open(modified_file, 'r') as f2:
        base_file_content = f1.readlines()
        modified_file_content = f2.readlines()
    return base_file_content, modified_file_content

def check_changes(base_file_content, modified_file_content):
    if base_file_content == modified_file_content:
        print("[INFO] No changes were made.")
        return False
    return True

def check_replace(modified_file_content, j1, j2, modified_file):
    diff_lines = modified_file_content[j1:j2]
    tag_found = False
    for diff_line in diff_lines:
        match = re.match(pattern, diff_line)
        if match:
            tag_found = True
            print("[INFO] Change in {file} is correctly tagged".format(file=modified_file))
    if not tag_found:
        print(f"[ERROR] Line {j2} have been changed without tagging. Please add a tag to indicate the change.")

def check_insert(modified_file_content, j1, j2, modified_file):
    inserted_lines = modified_file_content[j1:j2]
    tag_found = False
    multiline = []
    n = 0
    for line in inserted_lines:
        match = re.match(pattern, line)
        if match:
            tag_found = True
            if match.group(1) == '<' or match.group(1) == '>':
                n += 1
                multiline.append(n)
    if tag_found:
        if n == 2:
            print("[INFO] Change in {file} is correctly tagged.".format(file=modified_file))
        elif not n == 2:
            print ("[Error] Change in {file} is not constructed correctly".format(file=modified_file))
    elif not tag_found:
        print(f"Line {j2} have been inserted without tagging. Please add a tag to indicate the change.")

def check_tags(base_file, modified_file, base_file_content, modified_file_content):
    matcher = difflib.SequenceMatcher(None, base_file_content, modified_file_content)
    for op, i1, i2, j1, j2 in matcher.get_opcodes():
        if op == 'equal':
            continue
        if op == 'replace':
            check_replace(modified_file_content, j1, j2, modified_file)
        elif op == 'delete':
            print(f"[ERROR] Line {i2} have been removed without tagging. Please add a tag to indicate the change.")
        elif op == 'insert':
            check_insert(modified_file_content, j1, j2, modified_file)

def check_files(base_file, modified_file):
    if not check_file(base_file, modified_file):
        return False
    base_file_content, modified_file_content = read_files(base_file, modified_file)
    if not check_changes(base_file_content, modified_file_content):
        return False
    check_tags(base_file, modified_file, base_file_content, modified_file_content)
    return True

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <base_file> <modified_file>")
        sys.exit(1)
    base_file = sys.argv[1]
    modified_file = sys.argv[2]
    if not check_files(base_file, modified_file):
        sys.exit(1)
