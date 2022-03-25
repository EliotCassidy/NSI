def swap(text: list) -> list:
  assert isinstance(text, list)
  for i in range(len(text)):
    charcode = ord(text[i])
    if charcode > 64 and charcode < 91:
      text[i] = chr(charcode + 32)
    elif charcode > 96 and charcode < 123:
      text[i] = chr(charcode - 32)
      

text_input = list(input("Text à modifier : "))
swap(text_input)
print("".join(text_input))