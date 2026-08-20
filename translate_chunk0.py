import json
import re
import os

input_file = "/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0.json"
output_file = "/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0_out.ndjson"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Loaded {len(data)} items.")
