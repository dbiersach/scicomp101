# write_json.py

import json


uranium_isotopes = {
    "Uranium 233": {
        "atomic_mass": "233.03963 u",
        "neutrons": 141,
        "half-life": 5.015e12,
    },
    "Uranium 234": {
        "atomic_mass": "234.04095 u",
        "neutrons": 142,
        "half-life": 7.758e12,
    },
    "Uranium 235": {
        "atomic_mass": "235.04393 u",
        "neutrons": 143,
        "half-life": 2.208e16,
    },
    "Uranium 236": {
        "atomic_mass": "236.04557 u",
        "neutrons": 144,
        "half-life": 7.379e14,
    },
    "Uranium 237": {
        "atomic_mass": "237.04873 u",
        "neutrons": 145,
        "half-life": 583200,
    },
    "Uranium 238": {
        "atomic_mass": "238.05079 u",
        "neutrons": 146,
        "half-life": 1.407e17,
    },
}

outfile = open("uranium_isotopes.json", "w", encoding="ascii")
json.dump(uranium_isotopes, outfile, indent=4)
outfile.close()

print('The file "uranium_isotopes.json" was created')
