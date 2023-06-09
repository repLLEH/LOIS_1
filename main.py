# Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
# выполнена студентом группы 021703 БГУИР Смелов Алексей Александрович
# Файл с описанием модуля анализатора сокращённого языка логики высказываний
# Проверяет является ли формула сокращенного языка логики высказываний конъюктивной нормальной формой
# 28.03.2023

class Lexem:
    def __init__(self,lexem_type,input_string):
        self.lexemType = lexem_type
        self.value = input_string
lexem_type = {
    'symbol': ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'),
    'conjunction': '/\\',
    'disjunction': '\/',
    'implication': '->',
    'equivalence': '~',
    'neg': '!',
    'constant': ('0','1'),
    'open_bracket': '(',
    'close_bracket': ')'
}
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
            lexList.append(Lexem('conjunction', input_string[i] + input_string[i+1] ))
            i += 1
            continue
        elif (input_string[i] == '\\') and (input_string[i+1] == '/'):
            lexList.append(Lexem('disjunction', input_string[i] + input_string[i+1]))
            i += 1
            continue
        elif (input_string[i] == '-') and (input_string[i+1] == '>'):
            lexList.append(Lexem('implication', input_string[i] + input_string[i+1]))
            i+=1
            continue
        elif input_string[i] in lexem_type['equivalence']:
            lexList.append(Lexem('equivalence', input_string[i]))

    return lexList



##############################################
# symbol : [A-Z][0-9]*
# binary_connections : [/\ | \/ | -> | ~]
# unary_op : !
# constant : 0 | 1
# atom : symbol | '(' formula ')' | constant
# formula : atom | binary_complex_formula | unary_complex_formula
# unary_complex_formula :  unary_op atom
# binary_complex_formula :  atom binary_connection atom
def double_bracket_check(lexList):
    operator_count = 0
    for i in range(len(lexList)):
        if lexList[i].lexemType == 'open_bracket':
            if lexList[i + 1].lexemType == 'open_bracket':
                for j in range(i+2,len(lexList)):
                    if lexList[j].lexemType == 'conjunction' or lexList[j].lexemType == 'disjunction' or lexList[
                        j].lexemType == 'implication' or lexList[j].lexemType == 'equivalence':
                        operator_count+=1
                    elif lexList[j].lexemType == 'close_bracket':
                        if lexList[j+1].lexemType == 'close_bracket':
                            break
    if operator_count == 1:
        return False
    else: return True



def is_formula(lexList):
    if double_bracket_check(lexList):
        bracket_counter = 0
        if len(lexList) == 0:
            return False
        for i in range(len(lexList)):
            if i + 1 != len(lexList):
                if lexList[i].lexemType == 'open_bracket':
                    bracket_counter += 1
                    if lexList[i+1].lexemType == 'neg':
                        continue
                    elif lexList[i+1].lexemType == 'open_bracket':
                        continue
                    elif lexList[i+1].lexemType == 'symbol':
                        continue
                    elif lexList[i+1].lexemType == 'constant':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'neg':
                    if lexList[i+1].lexemType == 'symbol' and lexList[i-1].lexemType == 'open_bracket':
                        continue
                    elif lexList[i+1].lexemType == 'open_bracket':
                        continue
                    elif lexList[i+1].lexemType == 'constant':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'symbol':
                    if (lexList[i+1].lexemType == 'conjunction' or lexList[i+1].lexemType == 'disjunction' or lexList[i+1].lexemType == 'implication' or lexList[i+1].lexemType == 'equivalence') and ( lexList[i-1].lexemType == 'conjunction' or lexList[i-1].lexemType == 'disjunction' or lexList[i-1].lexemType == 'implication' or lexList[i-1].lexemType == 'equivalence'):
                        return False
                    elif lexList[i-1].lexemType == 'neg' and lexList[i+1].lexemType != 'close_bracket':
                        return False
                    elif lexList[i+1].lexemType == 'close_bracket' and (lexList[i-1].lexemType == 'neg' or lexList[i-1].lexemType == 'conjunction' or lexList[i-1].lexemType == 'disjunction' or lexList[i-1].lexemType == 'implication' or lexList[i-1].lexemType == 'equivalence'):
                        continue
                    elif lexList[i+1].lexemType == 'conjunction' or lexList[i+1].lexemType == 'disjunction' or lexList[i+1].lexemType == 'implication' or lexList[i+1].lexemType == 'equivalence':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'constant':
                    if lexList[i + 1].lexemType == 'close_bracket' and (
                            lexList[i - 1].lexemType == 'neg' or lexList[i - 1].lexemType == 'conjunction' or lexList[
                        i - 1].lexemType == 'disjunction' or lexList[i - 1].lexemType == 'implication' or lexList[
                                i - 1].lexemType == 'equivalence'):
                        continue
                    elif lexList[i+1].lexemType == 'conjunction' or lexList[i+1].lexemType == 'disjunction' or lexList[i+1].lexemType == 'implication' or lexList[i+1].lexemType == 'equivalence':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'conjunction' or lexList[i].lexemType == 'disjunction' or lexList[i].lexemType == 'implication' or lexList[i].lexemType == 'equivalence':
                    if i == 0 or i == 1:
                        return False
                    elif lexList[i+1].lexemType == 'symbol':
                        continue
                    elif lexList[i+1].lexemType == 'open_bracket':
                        continue
                    elif lexList[i+1].lexemType == 'constant':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'close_bracket':
                    bracket_counter -= 1
                    if lexList[i+1].lexemType == 'close_bracket':
                        continue
                    elif lexList[i+1].lexemType == 'conjunction' or lexList[i+1].lexemType == 'disjunction' or lexList[i+1].lexemType == 'implication' or lexList[i+1].lexemType == 'equivalence':
                        continue
                    else:
                        return False
            elif i + 1 == len(lexList):
                if lexList[i].lexemType == 'close_bracket':
                    bracket_counter -= 1
                elif lexList[i].lexemType == 'constant':
                    continue
                elif lexList[i].lexemType == 'symbol':
                    continue

                else:
                    return False

        if bracket_counter != 0:
            return False
        return True
    else: return False

class TestParserException(Exception):
    pass

# formula='A~A'
# lexList = lexAnalyze(formula,lexem_type)
# print(is_formula(lexList))
def is_CNF(lexList):

    if is_formula(lexList):
        bracket_counter=0
        conjuct_counter=0
        # for i in range(len(lexList)):
        #     if lexList[i].lexemType == 'conjunction':
        #         conjuct_counter += 1
        #         break
        # if conjuct_counter == 0:
        #     return False
        for i in range(len(lexList)):
            if i + 1 != len(lexList):
                if lexList[i].lexemType == 'open_bracket':
                    bracket_counter += 1
                    if lexList[i + 1].lexemType == 'neg':
                        continue
                    elif lexList[i + 1].lexemType == 'open_bracket':
                        continue
                    elif lexList[i + 1].lexemType == 'symbol':
                        continue
                    elif lexList[i + 1].lexemType == 'constant':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'neg':
                    if lexList[i + 1].lexemType == 'symbol' and lexList[i - 1].lexemType == 'open_bracket':
                        continue
                    elif lexList[i + 1].lexemType == 'constant':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'symbol':
                    if (lexList[i + 1].lexemType == 'conjunction' or lexList[i + 1].lexemType == 'disjunction') and ( lexList[i - 1].lexemType == 'conjunction' or lexList[i - 1].lexemType == 'disjunction'):
                        return False
                    elif lexList[i + 1].lexemType == 'close_bracket' and (
                            lexList[i - 1].lexemType == 'neg' or lexList[i - 1].lexemType == 'conjunction' or lexList[
                        i - 1].lexemType == 'disjunction'):
                        continue
                    elif lexList[i + 1].lexemType == 'conjunction' or lexList[i + 1].lexemType == 'disjunction':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'constant':
                    if lexList[i + 1].lexemType == 'close_bracket' and (
                            lexList[i - 1].lexemType == 'neg' or lexList[i - 1].lexemType == 'conjunction' or lexList[i - 1].lexemType == 'disjunction'):
                        continue
                    elif lexList[i + 1].lexemType == 'conjunction' or lexList[i + 1].lexemType == 'disjunction':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'conjunction' or lexList[i].lexemType == 'disjunction':
                    conjuct_counter+=1
                    if i == 0 or i == 1:
                        return False
                    elif lexList[i + 1].lexemType == 'symbol':
                        continue
                    elif lexList[i + 1].lexemType == 'open_bracket':
                        continue
                    elif lexList[i + 1].lexemType == 'constant':
                        continue
                    else:
                        return False
                elif lexList[i].lexemType == 'close_bracket':
                    bracket_counter -= 1
                    if lexList[i + 1].lexemType == 'close_bracket':
                        continue
                    elif lexList[i + 1].lexemType == 'conjunction':
                        continue
                    else:
                        return False
            elif i + 1 == len(lexList):
                if lexList[i].lexemType == 'close_bracket':
                    bracket_counter -= 1
                elif lexList[i].lexemType == 'constant':
                    continue
                elif lexList[i].lexemType == 'symbol':
                    continue
                else:
                    return False

        if bracket_counter != 0:
            return False
        return True
    else:
        return False


input_string=input('Input string: ')
lexList = lexAnalyze(input_string,lexem_type)
# for lex in lexList:
#     print(lex.lexemType + '  ::==  ' + lex.value)
if is_CNF(lexList):
    print('+ Formula is CNF +')
else:
    print('- Formula is not CNF -')


# with open("tests.csv", "r") as tests_file:
#     tests = tests_file.readlines()
#     for test in tests:
#         if test == "\n":
#             continue
#         formula, answer_string = test[0:-1].split(",")
#         lexList = lexAnalyze(formula, lexem_type)
#         test_answer: bool = True if answer_string == "True" else False
#         try:
#             parser_answer = is_formula(lexList)
#         except Exception as ex:
#             print(f"TestParserError: test failed: {tests.index(test)} error: {ex}")
#         if parser_answer != test_answer:
#             print(formula)
#             raise TestParserException(f"TestParserError: {tests.index(test)} "
#                                            f"test failed, parser answer: {parser_answer}, "
#                                            f"test answer: {test_answer}")