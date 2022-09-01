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
  'STATESLIST_OPEN',
  'STATESLIST_CLOSE',
  'SHAPE_OPEN',
  'SHAPE_CLOSE',
  'EVENTDATE_OPEN',
  'EVENTDATE_CLOSE',
  'IMAGES_OPEN',
  'IMAGES_CLOSE',
)

# Regular expression rules for simple tokens
t_STATE_OPEN = r'<state>'
t_STATE_CLOSE = r'</state>'
t_STATESLIST_OPEN = r'<states_list>'
t_STATESLIST_CLOSE = r'</states_list>'
t_EVENTDATE_OPEN = r'<_date>'
t_EVENTDATE_CLOSE = r'</date>'
t_DURATION_OPEN = r'<duration>'
t_DURATION_CLOSE = r'</duration>'
t_IMAGES_OPEN = r'<images>'
t_IMAGES_CLOSE = r'</images>'

# A regular expression rule with some action code

def t_DATE(t):
  r'^(0[1-9]|1[012]|[1-9])\/([012][0-9]|3[01]|[1-9])\/(0[1-9]|[1-9][0-9])$'
  return t

def t_IMAGES(t):
  r'^(Yes|No)$'
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
  data = open(filename, "r", encoding="utf-8")
  for line in data.readlines():
    lines.append(line.replace('\n', ''))
  with open (filename, "r") as filecontents:
    data = filecontents.read().replace('\n', ' ')
  return data

data = open_file("UFO_Report_Test.xml")

# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
  tok = lexer.token()
  if not tok: 
    break      # No more input
  print(tok)