def sort_on(dict):
    return dict["num"]
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def letter_count(book_text):
    counts = {}
    for char in book_text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def chars_dict_to_list(chars):
	organize = []
	for key, value in chars.items():
		new_list = {"char": key, "num": value}
		organize.append(new_list)
		organize.sort(reverse=True, key=sort_on)
	return organize
