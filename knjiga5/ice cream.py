def make_sundae(ice_cream='vanilla',sauce='chocolate',nuts=True,banana=True,
                brownies=False,whiped_cream=True):
    recipe=ice_cream+' ice cream and '+sauce+' sauce'
    if nuts:
        recipe=recipe+' with nuts and '
    if banana:
        recipe=recipe+' with banana and '
    if brownies:
        recipe=recipe+' with brownies and '
    if not whiped_cream:
        recipe=recipe+' no '
    recipe=recipe+' whiped cream on top.'
    return recipe

sundae=make_sundae()
print('One sundar coming with'+sundae)

sundae=make_sundae('chocolate')
print('One sundar coming with ',sundae)

sundae=make_sundae(sauce='caramel',whiped_cream=False,banana=False)
print('One sundar coming with ',sundae)

sundae=make_sundae(whiped_cream=False,banana=True,brownies=True,ice_cream='peanut butter')
print('One sundar coming with ',sundae)

sundae=make_sundae(whiped_cream=True)
print('One sundar coming with ',sundae)