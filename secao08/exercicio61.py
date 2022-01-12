from collections import Counter


def anagrama(str1, str2):
    if len(str1) == len(str2):
        dic_str1 = Counter(list(str1))
        dic_str2 = Counter(list(str2))
        if dic_str1 == dic_str2:
            return True
    return False


str1 = input('Informe a primeira palavra: ')
str2 = input('Informe a segunda palavra: ')

if anagrama(str1, str2):
    print(f'A palavra {str1} é anagrama de {str2}')
else:
    print(f'Não existe anagrama')
