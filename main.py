import re
import vars
import survey

def format_clean_code(survey_code):
    only_numbers = re.sub('[^0-9]+', '*', survey_code)
    return only_numbers


def validate_code(cleaned_survey_code):
    return len(cleaned_survey_code) == 20


def split_code(code):
    code_dicts = {dicts_iter: "" for dicts_iter in range(1, 8)}
    counter = 1
    for char in code:
        code_dicts[counter] += char
        if len(code_dicts[counter]) == 3:
            counter += 1
    return code_dicts


only_numbers_code = format_clean_code(vars.SURVEY_CODE)
validation_of_code = validate_code(vars.SURVEY_CODE)
code_split_up = None
if validation_of_code:
    print("Valid Code. Will Proceed")
    code_split_up = split_code(only_numbers_code)
    print("Automation Beginning Now....")
    survey_results = survey.run_survey(code_split_up)
    print(survey_results)

