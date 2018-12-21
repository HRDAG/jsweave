#!/usr/bin/env python
#
# vim: ft=python:
# -*- coding: utf-8 -*-
#
# Author: Daniel Manrique-Vallier
# Maintainer(s): Tarak Shah, Patrick Ball, Daniel Manrique-Vallier
#
# License: (c) Daniel Manrique-Vallier 2018, GPL v2 or newer
#
#
# replace occurrences of \jsonsub[xxx]{code} in TeX file with
# the content of "code" from JSON file
# In TeX file include:
#
#      \usepackage{color}
#      \newcommand{\jsonsub}[2][XXXX]{ \textcolor{red}{#1} }
#
# Use in TeX file: \jsonsub[<default value>]{<code for substitution>}

import json
import re
import pylatexenc.latexencode


def get_json(file_name):
    with open(file_name, "r") as f:
        d = json.load(f)
    return d


def get_tex(file_name):
    with open(file_name, "r") as f_tex:
        tex = f_tex.read()
    return tex


def tex_escape(text):
    return pylatexenc.latexencode.utf8tolatex(str(text), brackets = False)


def jsonsub_regex(obj_name, escape = True):
    if escape:
        obj = re.escape(obj_name)
    else:
        obj = obj_name
    pattern = r"\\jsonsub(\[([^\]]+)\])?\{" + obj + r"\}"
    return re.compile(pattern)


def sub(tex, js):
    for key, value in js.items():
        pattern = jsonsub_regex(key)
        tex = pattern.sub(tex_escape(value), tex)
    return tex


def check(tex, js):
    texlines = tex.splitlines()
    check_results = []
    for key, value in js.items():
        pattern = jsonsub_regex(key)
        data_value = tex_escape(value)
        diffs = [ (line[0] + 1, pattern.search(line[1]).group(2), data_value)
                  for line in enumerate(texlines)
                  if pattern.search(line[1]) is not None and
                     data_value != pattern.search(line[1]).group(2) ]
        check_results.extend(diffs)
    return check_results


def check_term(tex, js):
    result = check(tex, js)
    output = ["lineno|old_value|new_value"]
    for ln in result:
        output.append(str(ln[0]) + "|" + str(ln[1]) + "|" + str(ln[2]))
    return("\n".join(output))


def update(tex, js):
    for key, value in js.items():
        pattern = jsonsub_regex(key)
        replacement = r"\\jsonsub[" + tex_escape(value) + "]{" + key + "}"
        tex = pattern.sub(replacement, tex)
    return tex


def verify_substitution(tex):
    non_sub_line_nbrs = []
    details = []
    non_sub_cnt = 0
    jsonsub_pattern = jsonsub_regex("(.*)", escape = False)
    for line in enumerate(tex.splitlines()):
        line_txt = line[1]
        line_nbr = line[0] + 1
        matches = jsonsub_pattern.findall(line_txt)
        if matches:
            non_sub_line_nbrs.append(line_nbr)
            non_sub = [match[0] + '\t<-->\t' + match[2] for match in matches]
            details.append("> line " + str(line_nbr) + ":\n\t\t" +
                    '\n\t\t'.join(non_sub))
            non_sub_cnt = non_sub_cnt + len(matches)
    non_sub_line_cnt = len(non_sub_line_nbrs)
    details.insert(0, 'Non substituted entries: ' + str(non_sub_cnt) + '\n')
    details.insert(0, 'Lines with no Substitutions: ' + str(non_sub_line_cnt))
    return [non_sub_line_nbrs, details]


def write_logfile(substituted, filename):
    log = verify_substitution(substituted)
    n_undefined = len(log[0])
    log_details = log[1]
    with open(filename, 'w') as logfile:
        if n_undefined > 0:
            log_details.insert(0, 'Undefined Codes:' + str(n_undefined))
            logfile.write('\n'.join(log_details))
        else:
            logfile.write('Success!')


# done.

