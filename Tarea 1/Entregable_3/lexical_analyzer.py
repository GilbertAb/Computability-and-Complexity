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
  'SHAPELIST_OPEN',#ERICK   
  'SHAPE_OPEN',  #ERICK
  'SHAPE_CLOSE',#ERICK
  'SHAPELIST_CLOSE',#ERICK   
  'SHAPE',      #ERICK
  'EVENT_OPEN',  #ERICK
  'EVENT_CLOSE',#ERICK
  'CITY_OPEN',   #ERICK
  'CITY_CLOSE', #ERICK
  'CITY',       #ERICK
  'SUMMARY_OPEN', #ERICK
  'SUMMARY_CLOSE',#ERICK
  'SUMMARY', #ERICK
  'DURATION_OPEN', #ERICK
  'DURATION_CLOSE',#ERICK
  'DURATION', #ERICK
  'STATESLIST_OPEN',
  'STATESLIST_CLOSE',
  'DATE_OPEN',
  'DATE_CLOSE',
  'DATE',
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
t_SHAPELIST_OPEN = r'<shape_list>'#ERICK 
t_SHAPE_OPEN = r'<shape>'#ERICK 
t_SHAPE_CLOSE = r'</shape>' #ERICK
t_SHAPELIST_CLOSE= r'</shape_list>'#ERICK 
t_EVENT_OPEN = r'<event>' #ERICK
t_EVENT_CLOSE = r'</event>' #ERICK
t_CITY_OPEN = r'<city>' #ERICK
t_CITY_CLOSE = r'</city>' #ERICK
t_SUMMARY_OPEN = r'<summary>' #ERICK
t_SUMMARY_CLOSE = r'</summary>' #ERICK
t_DURATION_OPEN = r'<duration>' #ERICK
t_DURATION_CLOSE = r'</duration>' #ERICK
t_STATESLIST_OPEN = r'<states_list>'
t_STATESLIST_CLOSE = r'</states_list>'
t_DATE_OPEN = r'<date>'
t_DATE_CLOSE = r'</date>'
t_IMAGES_OPEN = r'<images>'
t_IMAGES_CLOSE = r'</images>'
t_POSTED_OPEN = r'<posted>'
t_POSTED_CLOSE = r'</posted>'
t_TIME_OPEN = r'<time>'
t_TIME_CLOSE = r'</time>'

# A regular expression rule with some action code

def t_SUMMARY(t):
  r'(?<=<summary>).[^<]*'
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
  r'(?<=<duration>).[^<]*'
  return t          

def t_DATE(t):
  r'(?<=<date>).[^<]*'
  return t

def t_TIME(t):
  r'(Unknown|\d{2}:\d{2})'
  return t

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
  f.write("Illegal character '%s'" % t.value[0])
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# List to store 
STATES = []

# A dictionaries list, with a dictionary for each event
dict_list = []
dictionary = {}

# File for the results
file_syntax = open("syntax.txt", "a")

def p_file(t):
  '''file : states_list shapes_list events_list'''
  file_syntax.write("File\n")

def p_events_list(t):
  '''events_list : event'''
  file_syntax.write("Events_list\n")

def p_event(t):
  '''event : EVENT_OPEN link_element date_element time_element city_element state_element country_element \
  shape_element duration_element summary_element posted_element images_element EVENT_CLOSE event
  | EVENT_OPEN link_element date_element time_element city_element state_element country_element \
  shape_element duration_element summary_element posted_element images_element EVENT_CLOSE'''

def p_states_list(t):
  '''states_list : STATESLIST_OPEN stateslist_element STATESLIST_CLOSE'''
  file_syntax.write(str(t[1]) + "\n" + t[3] + "\n\n")
  STATES.append(t[2])

def p_stateslist_element(t):
  '''stateslist_element : STATE_OPEN STATE STATE_CLOSE stateslist_element 
  | STATE_OPEN STATE STATE_CLOSE'''
  file_syntax.write(str(t[1]) + "\n" + "\t" + str(t[2]) + "\n" + t[3] + "\n")
  STATES.append(t[2])

def p_shapes_list(t):
  '''shapes_list : SHAPELIST_OPEN shapeslist_element SHAPELIST_CLOSE'''
  file_syntax.write(str(t[1]) + "\n" + t[3] + "\n\n")     

def p_shapeslist_element(t):  
  '''shapeslist_element : SHAPE_OPEN SHAPE SHAPE_CLOSE shapeslist_element
                       | SHAPE_OPEN SHAPE SHAPE_CLOSE  '''   
  file_syntax.write(str(t[1]) + "\n" + "\t" + str(t[2]) + "\n" + t[3] + "\n")

def p_time_element(t):
  '''time_element : TIME_OPEN TIME TIME_CLOSE 
                  | TIME_OPEN TIME_CLOSE'''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_country_element(t):
  '''country_element : COUNTRY_OPEN COUNTRY COUNTRY_CLOSE 
                      | COUNTRY_OPEN COUNTRY_CLOSE'''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_summary_element(t):
  '''summary_element : SUMMARY_OPEN SUMMARY SUMMARY_CLOSE 
                      | SUMMARY_OPEN SUMMARY_CLOSE'''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_posted_element(t):
  '''posted_element : POSTED_OPEN POSTED POSTED_CLOSE
                    | POSTED_OPEN POSTED_CLOSE'''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_duration_element(t):
  '''duration_element : DURATION_OPEN DURATION DURATION_CLOSE
                      | DURATION_OPEN DURATION_CLOSE'''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_state_element(t):
  '''state_element : STATE_OPEN STATE STATE_CLOSE
                    | STATE_OPEN STATE_CLOSE'''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_date_element(t):
  '''date_element : DATE_OPEN DATE DATE_CLOSE
                  | DATE_OPEN DATE_CLOSE'''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_link_element(t):
  '''link_element : LINK_OPEN LINK LINK_CLOSE
                  | LINK_OPEN LINK_CLOSE'''
  file_syntax.write("<event>\n")
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_images_element(t):
  '''images_element : IMAGES_OPEN IMAGES IMAGES_CLOSE
                    | IMAGES_OPEN IMAGES_CLOSE'''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")
  file_syntax.write("</event>\n\n")

def p_city_element(t):
  '''city_element  : CITY_OPEN CITY CITY_CLOSE 
                   | CITY_OPEN  CITY_CLOSE  '''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_shape_element(t):
  '''shape_element : SHAPE_OPEN  SHAPE SHAPE_CLOSE shape_element 
                  | SHAPE_OPEN SHAPE SHAPE_CLOSE  '''
  file_syntax.write("\t" + str(t[1]) + "\n" + "\t\t" + str(t[2]) + "\n" + "\t" + t[3] + "\n")

def p_error(t):
    print("Syntax error at '%s'" % t[0].value)

# Read the file
lines = []
def open_file(filename):
  data = open(filename, "r", encoding="utf-8")
  for line in data.readlines():
    lines.append(line.replace('\n', ''))
  with open (filename, "r") as filecontents:
    data = filecontents.read().replace('\n', ' ')
  return data

#data = open_file("UFO_Report_2022.xml")
data = open_file("UFO.xml")

f = open("results.txt", "a")

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
  tok = lexer.token()
  if not tok: 
    break      # No more input
  f.write(str(tok.value)+" | " +  str(tok.type) + "\n")
  #print(tok)

#import ply.yacc as yacc
#parser = yacc.yacc()
#parser.parse(data)

#f.close()

import ply.yacc as yacc
parser = yacc.yacc()
parser.parse(data)

print(STATES)
print(dict_list)

f.close()