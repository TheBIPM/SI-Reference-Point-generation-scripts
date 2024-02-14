"""
symbols_format
manage string substitution for symbols
"""

import os
import re
import yaml
from si_ref_point.settings import CUQ_FILES_FOLDER

# Load symbols data
with open(os.path.join(CUQ_FILES_FOLDER, 'symbols.yaml'), encoding="utf8") as fp:
    symbols = yaml.safe_load(fp)


def formattxt(txt, fmt='latex', add_delim=True, decimal_sep="."):
    """
    formats a text string with symbols replaced in any of the following formats
    html, latex, json, text

    txt : input string
    fmt : one of ['html', 'latex', 'json', 'text']
    add_delim : boolean, adds delimiter at beginning and end (e.g. "$")
    """
    if fmt not in ['html', 'latex', 'json', 'text']:
        return txt
    if txt is None or txt == "" or '@' not in txt:
        return txt
    # Change decimal separator to coma if needed (french style)
    if decimal_sep != ".":
        matches = re.findall(r"\d\.\d", txt)
        for decsep in matches:
            txt = txt.replace(decsep, decsep[0] + decimal_sep + decsep[1])

    matches = re.findall(r"@(.*?)@", txt)
    for symcode in matches:
        if fmt == 'latex' and symbols[symcode]['type'] == 'symbol':
            delim = ['$', '$']
        elif fmt == 'latex' and symbols[symcode]['type'] == 'equation':
            delim = ['$$', '$$']
        else:
            delim = ['', '']
        depth = 0
        replacement = symbols[symcode][fmt]
        while '@' in replacement:
            # Handle nested macros up to 3 levels
            if depth > 3:
                print('Error, too many levels of @')
                break
            inner_matches = re.findall(r"@(.*?)@", replacement)
            for inner_symcode in inner_matches:
                replacement = replacement.replace(f"@{inner_symcode}@",
                                                  symbols[inner_symcode][fmt])
            depth += 1
        if add_delim:
            replacement = delim[0] + replacement + delim[1]
        txt = txt.replace(f"@{symcode}@", replacement)

    return txt
