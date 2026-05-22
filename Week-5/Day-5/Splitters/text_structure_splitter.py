from langchain_text_splitters import RecursiveCharacterTextSplitter

text="Lel fi huepe jupu akse zej ire vesik kojvulom zon is biwuwkef pa. Uv hokivej voh ebu numdogi akolo hik uwlez ta vacev ofdaimi acunetum suvet uhdab ir soglazo ju pafbeb. Pub cezeh fuc kebamnul he ok luumoabi rawkig me fov pin zup biv risugra. Ralpunad apkomgib alnirciw akel wa lus wahfum burog buol vecotihe abadahoj ugolo wovki ucojal fec."

splitters=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
)

chunks=splitters.split_text(text)
print(len(chunks))

print(chunks)