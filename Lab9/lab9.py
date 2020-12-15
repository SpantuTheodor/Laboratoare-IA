import lightrdf as lightrdf

document = lightrdf.RDFDocument("D:\\ANUL 3\\[IA]\Lab9\\CSO.3.2.owl", 'rb')

for element in document.search_triples('https://cso.kmi.open.ac.uk/topics/hands-free', None, None):
    print(element[0])
