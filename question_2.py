def to_camel_case(text):
    text = text.split()
    new_text=""

    for i in range(len(text)):
        new_text+=text[i].capitalize()
    return new_text
    
print(to_camel_case("tHis Is A tesT string"))

    

