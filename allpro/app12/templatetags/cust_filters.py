from django import template,templatetags
register=template.Library()

def first5upper(value):
    """this is my own custom filter"""
    result=value[:5].upper()
    return result
register.filter('f5u',first5upper)


@register.filter(name='l5l')
def last5lower(value):
    """this is my last 5 lower cust_filter"""
    result=value[5:].lower()
    return result