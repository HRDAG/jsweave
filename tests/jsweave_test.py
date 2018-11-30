import imp
jsweave = imp.load_source("jsweave", "../bin/jsweave")
from jsweave import *

def test_replace():
    TeX = "\\jsonsub[40]{datacrime}"
    JS = {'datacrime':'30'}
    replaced_str = replace(TeX, JS)
    expected_str = '30'
    assert replaced_str == expected_str

def test_replace_percent():
    TeX = "\\jsonsub[40\%]{datacrime}"
    JS = {'datacrime':'30%'}
    replaced_str = replace(TeX, JS)
    expected_str = '30\%'
    assert replaced_str == expected_str

def test_update():
    TeX = "\\jsonsub[40\%]{datacrime}"
    JS = {'datacrime':'30%'}
    updated_str = update(TeX, JS)
    expected_str = '\\jsonsub[40\%]{datacrime}'
