#!/usr/bin/env python3
"""Generate the # hash URL for pro_companion.html."""
import base64
import pathlib

html_path = pathlib.Path(__file__).parent / "pro_companion.html"
content = html_path.read_bytes()
b64 = base64.b64encode(content).decode("ascii")

base_url = "index.html"
full_url = f"{base_url}#{b64}"

print("=== pro_companion # URL ===")
print()
print(f"Base URL  : {base_url}")
print(f"Hash len  : {len(b64)} chars")
print()
print("Full URL:")
print(full_url)
print()
print("GitHub Pages URL (배포 후):")
print(f"https://minjoooolee.github.io/dr.answer-pro/#{b64}")
