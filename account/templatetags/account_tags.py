from django import template

register = template.Library()

@register.filter
def get_item(dictonary,key):

    return dictonary.get(key,False)