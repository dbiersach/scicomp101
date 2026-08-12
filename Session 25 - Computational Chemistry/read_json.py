#!/usr/bin/env -S uv run
"""read_json.py"""

import json
from pathlib import Path

file_name = "uranium_isotopes.json"
with Path.open(file_name, "rb") as f_in:
    uranium_isotopes = json.load(f_in)

# Compare half-lives of all isotopes
# to find the two with the greatest difference
max_diff = 0.0  # half-life difference in seconds
iso1 = iso2 = None
for k1, v1 in uranium_isotopes.items():
    for k2, v2 in uranium_isotopes.items():
        h1 = float(v1["half-life"])
        h2 = float(v2["half-life"])
        diff = abs(h1 - h2)
        if diff > max_diff:
            iso1 = k1
            iso2 = k2
            max_diff = diff

# Print isotopes with greatest half-life difference
print(iso1, iso2, sep=" <-> ")

# Print neutron count difference
neutrons1 = uranium_isotopes[iso1]["neutrons"]
neutrons2 = uranium_isotopes[iso2]["neutrons"]
neutron_delta = abs(neutrons1 - neutrons2)
print(f"  Neutron difference: {neutron_delta}")

# Convert half-life difference from seconds to years
year_diff = max_diff / (60 * 60 * 24 * 365.25)
print(f"Half-life difference: {year_diff:,.0f} years")
