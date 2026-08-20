import json
from pathlib import Path

OUT_FILE = Path('/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_4_out.ndjson')

def append_items(items):
    with open(OUT_FILE, 'a', encoding='utf-8') as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    print(f"Appended {len(items)} items. Total lines: {len(OUT_FILE.read_text(encoding='utf-8').splitlines())}")

if __name__ == '__main__':
    # Initialize empty file if needed
    OUT_FILE.write_text('', encoding='utf-8')
    print("Reset out file.")
