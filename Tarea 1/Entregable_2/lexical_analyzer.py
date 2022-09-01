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
    'POSTED_OPEN',
    'POSTED_CLOSE'
)

# Regular expression rules for simple tokens
t_STATE_OPEN = r'<state>'
t_STATE_CLOSE = r'</state>'
t_POSTED_OPEN = r'<posted>'
t_POSTED_CLOSE = r'</posted>'
# A regular expression rule with some action code


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