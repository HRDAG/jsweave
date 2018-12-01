import imp
jsweave = imp.load_source("jsweave", "../bin/jsweave")
from jsweave import *
from subprocess import call

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
    assert updated_str == expected_str

def test_check():
    TeX = "\\jsonsub[40\%]{datacrime}"
    JS = {'datacrime':'30%'}
    check_output = check(TeX, JS)
    expected_result = [(1, "40%", "30%")]
    assert check_output == expected_result

def test_acceptance_replace():
    before_tex = getTeX("data/before.tex")
    fake_json = getJson("data/fake-json.json")
    res = replace(before_tex, fake_json)
    assert res == getTeX("data/expected.tex")    

def test_acceptance_update():
    before_tex = getTeX("data/before.tex")
    updated_json = getJson("data/updated-json.json")
    result = update(before_tex, updated_json)
    assert result == getTeX("data/expected-updated.tex")

def test_acceptance_check():
    before_tex = getTeX("data/before.tex")
    updated_json = getJson("data/updated-json.json")
    check_result = check(Tex, JS)
    expected_result = 
        [
            (11, "20", "77"),
            (13, "204,337.73", "197,283.11"),
            (15, "55%", "1%")
        ]
    assert check_result == expected_result
