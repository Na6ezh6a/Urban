# Генераторы.
def all_variants(text: str):
    length = len(text)
    for a in range(1, length + 1):
        for b in range(length - a + 1):
            yield text[b:a + b]

a = all_variants("abc")
for i in a:
    print(i)
