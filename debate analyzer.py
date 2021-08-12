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
    with open("october dem debate transcript.txt","r", encoding="utf8") as transcript:
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

def create_vocab_dict():
    global vocab_dict
    if 'vocab_dict' not in globals():
        vocab_dict = {}
    for q in quotes:
        candidate_vocab = []
        vocab_key = str(q)
        candidate_paras = quotes.get(q)
        for para in candidate_paras:
            res = re.findall(r'\w+', para)
            for word in res:
                if str(word) not in candidate_vocab:
                    candidate_vocab.append(word)
        vocab_dict[vocab_key] = candidate_vocab

create_vocab_dict()

for x in vocab_dict:
    printable = str(x) + ":" + str(len(vocab_dict[x]))
    print(printable)
print("testing github vscode")