
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN PRINT RPAREN STRINGprogram : statementstatement : PRINT LPAREN STRING RPAREN'
    
_lr_action_items = {'PRINT':([0,],[3,]),'$end':([1,2,6,],[0,-1,-2,]),'LPAREN':([3,],[4,]),'STRING':([4,],[5,]),'RPAREN':([5,],[6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','parser.py',22),
  ('statement -> PRINT LPAREN STRING RPAREN','statement',4,'p_statement_print','parser.py',28),
]
