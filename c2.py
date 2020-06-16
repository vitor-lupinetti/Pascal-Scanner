import re

auxStringRead = ""
lexemas = []
pascal_code = ""
isString = False

startStringPattern = r".*\'.*"
endStringPattern = r".*\'.*"
floatPattern = r"^(\+|-)?[0-9]+\.[0-9]+(e(\+|-)?[0-9]+)?$"
integerPattern = r"^(\+|-)?[0-9]+$"



with open("p1.pas", "r") as pcode:
    pascal_code = re.sub(r"\s+", " ", pcode.read().lower()).split()


def getLexemas(token):

    lexemas = []
    pascal_keys = ""
    pascal_symbols = ""

    with open("pascal-symbols.txt", "r") as psymbols:
        pascal_symbols = psymbols.read().split()

    with open("pascal-keys.txt", "r") as keys:
        pascal_keys = keys.read().lower().split()

   
      
    token = re.sub(r"\s*\(\s*", " ( ", token)

    token = re.sub(r"\s*\)\s*", " ) ", token)

    token = re.sub(r"\s*,\s*", " , ", token)

    token = re.sub(r"\s*;\s*", " ; ", token)

    for splitedToken in token.split():
        if splitedToken in pascal_keys:
            print([splitedToken, 'keyword'])
            lexemas.append([splitedToken, 'keyword'])
        elif re.match(integerPattern, splitedToken):
            print([splitedToken, 'integer'])
            lexemas.append([splitedToken, 'integer'])
        elif re.match(floatPattern, splitedToken):
            print([splitedToken, 'float'])
            lexemas.append([splitedToken, 'float'])
        elif splitedToken in pascal_symbols:
            print([splitedToken, 'symbol'])
            lexemas.append([splitedToken, 'symbol'])
        else:
            print([splitedToken, 'variable'])
            lexemas.append([splitedToken, 'variable'])

    return lexemas





for token in pascal_code:
    if isString:
        if re.match(endStringPattern, token):
            aux = re.sub(r"\'", "' ", token).split()
            isString = False
            auxStringRead += aux[0]
            print([auxStringRead.replace("'", ""), 'String'])
            lexemas.append([auxStringRead.replace("'", ""), 'String'])
            lexemasAux = (token.replace(aux[0], ""))

            for lex in lexemasAux:
                lexemas.append(lex)
        else:
            auxStringRead += " " + token + " "
    else:
        if re.match(startStringPattern, token):
            aux = re.sub(r"\'", " '", token).split()
            isString = True
            auxStringRead = aux[-1]

            lexemasAux = getLexemas(token.replace(auxStringRead, ""))

            for lex in lexemasAux:
                lexemas.append(lex)
        else:
            lexemasAux = getLexemas(token)

            for lex in lexemasAux:
                lexemas.append(lex)
