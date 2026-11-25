"""Write the funniest git commit message before breaking production on Friday.

The joke is the motive: the deploy is not an accident, it is a gift —
the weekend was getting lonely, so Friday afternoon gets an incident.
"""

import os

TEXT = "fix: deploy to production on Friday afternoon, because the weekend was getting lonely without an incident"

# Entry rule: exactly one line, at most 200 characters (commit-message cap).
assert "\n" not in TEXT and len(TEXT) <= 200, f"entry violates rules: {len(TEXT)} chars"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")

print(TEXT)
