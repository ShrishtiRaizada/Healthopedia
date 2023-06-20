from django import template
register = template.Library()

@register.filter(name='index')
def index(indexable, i):
    print(indexable)
    print(i)
    return indexable[i-1]