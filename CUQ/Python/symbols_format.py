""" symbols_format
manage string substitution for symbols
"""
import os
import re
from ruamel.yaml import YAML
from settings import XLS_FILES_FOLDER
yaml = YAML()

# Load symbols data
with open(os.path.join(XLS_FILES_FOLDER, 'symbols.yaml')) as fp:
    symbols = yaml.load(fp)


def formattxt(txt, fmt='html'):
    """
    formats a text string with symbols replaced in any of the following formats
    html, latex, json, text
    """
    if fmt not in ['html', 'latex', 'json', 'text']:
        return txt
    if txt is None or txt == "":
        return txt
    depth = 0
    while '@' in txt and depth < 3:
        for symcode in symbols.keys():
            if f'@{symcode}@' in txt:
                txt = txt.replace(f'@{symcode}@', symbols[symcode][fmt])
        depth += 1
    if fmt == "latex":
        txt = "${}$".format(txt)
    """
    # Previous version : obsolete ?
    matches = re.findall(f"@(.*?)@", txt)
    # order matches by length of substituting string (smallest first) so that
    # replacement of substrings
    # at the top level does not result in multiple replacements at top level
    # (resulting in $$)
    tmatches = {}
    for match in matches:
        strlen = len(syms[fmt][match])
        tmatches.update({match: strlen})
    omatches = dict(sorted(tmatches.items(), key=lambda item: item[1]))
    if omatches:
        for grp in omatches:
            if lvl == 0 and fmt == 'latex':
                # add latex delimiters at the top level
                if symtypes[grp] == 'symbol':
                    txt = txt.replace(
                        '@' + grp + '@', "$" + syms[fmt][grp] + "$")
                elif symtypes[grp] == 'equation':
                    txt = txt.replace(
                        '@' + grp + '@', "$$" + syms[fmt][grp] + "$$")
            else:
                txt = txt.replace('@' + grp + '@',  syms[fmt][grp])
        txt = txt.replace('\n', ' ')
    """
    return txt
