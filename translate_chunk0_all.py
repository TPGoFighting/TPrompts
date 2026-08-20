# -*- coding: utf-8 -*-
import json
import re
import os

input_path = "/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0.json"
output_path = "/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_0_out.ndjson"

with open(input_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

print(f"Total raw items: {len(raw_data)}")
