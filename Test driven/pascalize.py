def pascalize(name):
    if name == '':
        return ''
    return name.title().replace('_', '')

# meaning of don't use it outside of this file
def _capitalize(name):
    return name.title()