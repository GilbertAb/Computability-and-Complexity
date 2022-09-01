# ------------------------------------------------------------
 # lexical_analyzer.py
 # Authors: Daniel López, Erick Chicas, Gilbert Márquez
 # tokenizer for a simple expression evaluator
 # ------------------------------------------------------------

import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'STATE_OPEN',
    'STATE_CLOSE',
    'SHAPELISTOPEN',#ERICK   
    'SHAPEOPEN',  #ERICK
    'SHAPECLOSED',#ERICK
    'SHAPELISTCLOSED',#ERICK   
    'SHAPE',      #ERICK
    'EVENTOPEN',  #ERICK
    'EVENTCLOSED',#ERICK
    'CITYOPEN',   #ERICK
    'CITYCLOSED', #ERICK
    'CITY',       #ERICK
    'SUMMARYOPEN', #ERICK
    'SUMMARYCLOSED',#ERICK
    'SUMMARY', #ERICK
    'DURATIONOPEN', #ERICK
    'DURATIONCLOSED',#ERICK
    'DURATION', #ERICK
)

# Regular expression rules for simple tokens
t_STATE_OPEN = r'<state>'
t_STATE_CLOSE = r'</state>'
t_SHAPELISTOPEN = r'<shape_list>'#ERICK 
t_SHAPEOPEN = r'<shape>'#ERICK 
t_SHAPECLOSED = r'</shape>' #ERICK
t_SHAPELISTCLOSED= r'</shape_list>'#ERICK 
t_EVENTOPEN = r'<event>' #ERICK
t_EVENTCLOSED = r'</event>' #ERICK
t_CITYOPEN = r'<city>' #ERICK
t_CITYCLOSED = r'</city>' #ERICK
t_SUMMARYOPEN = r'<summary>' #ERICK
t_SUMMARYCLOSED = r'</summary>' #ERICK
t_DURATIONOPEN = r'<duration>' #ERICK
t_DURATIONCLOSED = r'</duration>' #ERICK

# A regular expression rule with some action code
def t_SHAPE(t):
     r'(?<=<shape>).[^</]+'
     return t   

def t_CITY(t):
     r'(?<=<city>).[^</]+'
     return t 
 
def t_SUMMARY(t):
     r'(?<=<summary>).[^</]+'
     return t   

def t_DURATION(t):
     r'(?<=<duration>).[^</]+'
     return t          

# Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Read the file
lines = []
def open_file(filename):
    data = open(filename, "r")
    for line in data.readlines():
        lines.append(line.replace('\n', ''))
    with open (filename, "r") as filecontents:
        data = filecontents.read().replace('\n', ' ')
    return data

#data = open_file("UFO_Report_2022.xml")
data = ''' '''
# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)