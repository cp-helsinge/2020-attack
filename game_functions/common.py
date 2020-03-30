"""============================================================================
  Common function
============================================================================"""
import re

# CamelCase to snake_case
def cc2sn(str):
  return re.sub(r'(?<!^)(?=[A-Z])', '_', str).lower()

# snake_case to CamelCase
def sn2cc(str):
  return ''.join(word.title() for word in str.split('_'))