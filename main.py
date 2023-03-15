
class Lexem:
    def __init__(self,lexem_type,input_string):
        self.lexemType = lexem_type
        self.value = input_string
lexem_type = {
    'symbol': ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            ,'0','1','2','3','4','5','6','7','8','9'),
    'conjunction': '/\\',
    'disjunction': '\/',
    'implication': '->',
    'equivalence': '~',
    'neg': '!',
    'constant': (0,1),
    'open_bracket': '(',
    'close_bracket': ')'
}

##############################################
# symbol : [A-Z][0-9]*
# binary_connections : [/\ | \/ | -> | ~]
# unary_op : !
# atom_formula : symbol
# formula : atom | constant
# unary_complex_formula : ( !  )
# binary_complex_formula : (atom binary_connection atom)

def lexAnalyze(input_string,lexem_type):
    lexList=[]
    for i in range(len(input_string)):
        if input_string[i] in lexem_type['open_bracket']:
            lexList.append(Lexem('open_bracket',input_string[i]))
            continue
        elif input_string[i] in lexem_type['close_bracket']:
            lexList.append(Lexem('close_bracket', input_string[i]))
            continue
        elif input_string[i] in lexem_type['symbol']:
            lexList.append(Lexem('symbol', input_string[i]))
            continue
        elif input_string[i] in lexem_type['neg']:
            lexList.append(Lexem('neg', input_string[i]))
            continue
        elif input_string[i] in lexem_type['constant']:
            lexList.append(Lexem('constant', input_string[i]))
        elif (input_string[i] == '/') and (input_string[i+1] == '\\'):
            lexList.append(Lexem('conjunction', input_string[i] + input_string[i+1]))
            i+=1
            continue
        elif (input_string[i] == '\\') and (input_string[i+1] == '/'):
            lexList.append(Lexem('disjunction', input_string[i] + input_string[i+1]))
            i+=1
            continue
        elif (input_string[i] == '-') and (input_string[i+1] == '>'):
            lexList.append(Lexem('implication', input_string[i] + input_string[i+1]))
            i+=1
            continue
        elif input_string[i] in lexem_type['equivalence']:
            lexList.append(Lexem('equivalence', input_string[i]))
    return lexList

input_string='(((!((A/\С)->B))~B)/\(!A))'

lexList = lexAnalyze(input_string,lexem_type)
for lex in lexList:
    print(lex.lexemType + '   ::=   ' + lex.value)