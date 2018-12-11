import imp
jsweave = imp.load_source("jsweave", "../bin/jsweave")
from jsweave import sub, check, update, get_tex, get_json


def test_sub():
    TeX = r"\jsonsub[40]{datacrime}"
    JS = {'datacrime': '30'}
    subd_str = sub(TeX, JS)
    expected_str = '30'
    assert subd_str == expected_str

def test_sub_plus_text():
    TeX = r"a value of \jsonsub[40]{datacrime} is too high"
    JS = {'datacrime': '30'}
    subd_str = sub(TeX, JS)
    expected_str = 'a value of 30 is too high'
    assert subd_str == expected_str

def test_sub_no_default():
    TeX = "\\jsonsub{datacrime} is too high"
    JS = {'datacrime': '30'}
    subd_str = sub(TeX, JS)
    expected_str = '30 is too high'
    assert subd_str == expected_str

def test_sub_percent():
    TeX = r"\jsonsub[40\%]{datacrime}"
    JS = {'datacrime': '30%'}
    subd_str = sub(TeX, JS)
    expected_str = '30\\%'
    assert subd_str == expected_str

def test_sub_integer():
    TeX = r"\jsonsub[40]{datacrime}"
    JS = {'datacrime': 30}
    subd_str = sub(TeX, JS)
    expected_str = '30'
    assert subd_str == expected_str

# def test_sub_escaped_percent():
#     TeX = r"\\jsonsub[40\%]{datacrime}"
#     JS = {'datacrime': r'30\%'}
#     subd_str = sub(TeX, JS)
#     expected_str = r'30\\%'
#     assert subd_str == expected_str

def test_update():
    TeX = r"\jsonsub[40\%]{datacrime}"
    JS = {'datacrime': '30%'}
    updated_str = update(TeX, JS)
    expected_str = r'\jsonsub[30\%]{datacrime}'
    assert updated_str == expected_str

def test_check():
    TeX = r"\jsonsub[40\%]{datacrime}"
    JS = {'datacrime':'30%'}
    check_output = check(TeX, JS)
    expected_result = [(1, "40\\%", "30\\%")]
    assert check_output == expected_result

# if no change, then don't report anything
def test_check2():
    TeX = r"\jsonsub[40\%]{datacrime}"
    JS = {'datacrime':'40%'}
    check_output = check(TeX, JS)
    expected_result = []
    assert check_output == expected_result

def test_acceptance_sub():
    before_tex = get_tex("data/before.tex")
    fake_json = get_json("data/fake-json.json")
    res = sub(before_tex, fake_json)
    assert res == get_tex("data/expected.tex")

def test_acceptance_update():
    before_tex = get_tex("data/before.tex")
    updated_json = get_json("data/updated-json.json")
    result = update(before_tex, updated_json)
    assert result == get_tex("data/expected-updated.tex")

def test_acceptance_check():
    before_tex = get_tex("data/before.tex")
    updated_json = get_json("data/updated-json.json")
    check_result = check(before_tex, updated_json)
    expected_result = [
            (11, "20", "77"),
            (13, "204,337.73", "197,283.11"),
            (15, r"55\%", r"1\%")
        ]
    assert check_result == expected_result
