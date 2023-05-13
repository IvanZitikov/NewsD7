from django import template

register = template.Library()

sens = 'редис'

@register.filter()
def censor(text):
   check = text.split()
   for i in check:
       if sens in i:
           text = text.replace(i, i[0:5] + '***')
   return text