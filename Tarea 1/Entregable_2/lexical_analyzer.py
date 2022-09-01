# ------------------------------------------------------------
 # lexical_analyzer.py
 # Authors: Daniel López, Erick Chicas, Gilbert Márquez
 # tokenizer for a simple expression evaluator
 # ------------------------------------------------------------

import ply.lex as lex

# List of token names.   This is always required
tokens = (
  'COUNTRY_OPEN',
  'COUNTRY_CLOSE',
  'COUNTRY',
  'LINK_OPEN',
  'LINK_CLOSE',
  'LINK',
  'STATE_OPEN',
  'STATE_CLOSE',
  'STATE',
  'POSTED_OPEN',
  'POSTED_CLOSE',
  'POSTED',
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
  'STATESLIST_OPEN',
  'STATESLIST_CLOSE',
  'SHAPE_OPEN',
  'SHAPE_CLOSE',
  'EVENTDATE_OPEN',
  'EVENTDATE_CLOSE',
  'IMAGES_OPEN',
  'IMAGES_CLOSE',
  'IMAGES',
  'TIME_OPEN',
  'TIME_CLOSE',
  'TIME',
)

# Regular expression rules for simple tokens
t_COUNTRY_OPEN = r'<country>'
t_COUNTRY_CLOSE = r'</country>'
t_LINK_OPEN = r'<link>'
t_LINK_CLOSE = r'</link>'
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
t_STATESLIST_OPEN = r'<states_list>'
t_STATESLIST_CLOSE = r'</states_list>'
t_EVENTDATE_OPEN = r'<date>'
t_EVENTDATE_CLOSE = r'</date>'
t_IMAGES_OPEN = r'<images>'
t_IMAGES_CLOSE = r'</images>'
t_POSTED_OPEN = r'<posted>'
t_POSTED_CLOSE = r'</posted>'
t_TIME_OPEN = r'<time>'
t_TIME_CLOSE = r'</time>'

# A regular expression rule with some action code

def t_SUMMARY(t):
  r'(?<=<summary>).[^<]+'
  return t

def t_COUNTRY(t):
  r'(?<=<country>).[^<]+'
  return t

def t_STATE(t):
  r'(?<=<state>).[^<]+'
  return t

def t_SHAPE(t):
  r'(?<=<shape>).[^<]+'
  return t   

def t_CITY(t):
  r'(?<=<city>)[^<]+'
  return t 

def t_DURATION(t):
  r'(?<=<duration>).[^<]+'
  return t          

def t_DATE(t):
  r'^(0[1-9]|1[012]|[1-9])\/([012][0-9]|3[01]|[1-9])\/(0[1-9]|[1-9][0-9])$'
  return t

def t_TIME(t):
  r'(Unknown|\d{2}:\d{2})'

def t_LINK(t):
  r'https://[\w\d@:%\._\\+#?&//=]{2,256}\.html'
  return t

def t_POSTED(t):
  r'(\s)*(\t)*\d{1,2}\/\d{1,2}\/\d{1,2}(\s)*(\t)*'
  return t

def t_IMAGES(t):
  r'(Yes|No)'
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

data = open_file("UFO_Report_2022.xml")

# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
  tok = lexer.token()
  if not tok: 
    break      # No more input
  print(tok)