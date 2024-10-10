from pypdf import PdfReader 
reader = PdfReader('11261.pdf')

page1 = reader.pages[1]
page2 = reader.pages[2]
page3 = reader.pages[3]


all_text = [reader.pages[i].extract_text() for i in range(4)]

print(type(all_text))
print(len(all_text))

print(all_text)
