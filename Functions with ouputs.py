def format_name(first_name, last_name):
    formated_fname = first_name.title()
    formated_lname = last_name.title()

    return f"{formated_fname} {formated_lname}"

final_text = format_name("vINCENT", "muCHIri")
print(final_text)