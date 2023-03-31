import regex as re

def search_regex(text, regex):
    
    if found_text := re.search(regex, text):
        # print(found_text.group(0))
        return found_text.group(0)

    return None