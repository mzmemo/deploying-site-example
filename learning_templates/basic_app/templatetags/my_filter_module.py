from django import template

register = template.Library()


# defining my own filter function

@register.filter(name='cut_tag') #here was used a decorator to register filter in place of using the line 'register.filter('cut_tag',cut)' below.
def cut(value, arg):
    """
        This function cuts out the 'agr' value from a given string.
    """

    return value.replace(arg,'')

#registering the filter function
# register.filter('cut_tag',cut)    -- #'cut_tag' is the name to be used on the template. 'cut' is the above defined function

