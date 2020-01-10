def extract_speaker(stringy):
    name_candidate = stringy.split(":")[0]
    if " " in name_candidate or not name_candidate.isupper():
        return ""
    return name_candidate

def create_quote_dict():
    global quotes
    if 'quotes' not in globals():
        quotes = {}
    most_recent_speaker = ""
    with open("test transcript.txt","r", encoding="utf8") as transcript:
        for line in transcript:
            cleaned_line = line.rstrip()
            if cleaned_line == "":
                continue
            if cleaned_line.startswith("("):
                continue
            speaker = extract_speaker(cleaned_line)
            if speaker == "":
                quotes[most_recent_speaker].append(cleaned_line)
            else:
                removable_name = len(speaker) + 2 #the 2 is for the colon and the space
                trimmed_line = cleaned_line[removable_name:]
                if speaker in quotes:
                    quotes[speaker].append(trimmed_line)
                else:
                    quotes[speaker] = [trimmed_line]
                most_recent_speaker = speaker
    return quotes

create_quote_dict()

import re 


sanders_word_list = []
warren_word_list = []

for q in quotes:
    speaker_strings = quotes.get(q)
    for string in speaker_strings:
        res = re.findall(r'\w+', string)
        for word in res:
            if str(word) not in sanders_word_list:
                sanders_word_list.append(word)

print(sanders_word_list)