text = "X-DSPAM-Confidence:    0.8475"
fnum = text.find("0")
numbers = float(text[fnum:])
print(numbers)