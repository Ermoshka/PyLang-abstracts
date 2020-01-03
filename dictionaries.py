fav_langs = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

fav_langs['ermoshka'] = ['js', 'python', 'java']

for name, langs in fav_langs.items():
    print("\n" + name.title() + "'s fav langs are:")
    for lang in langs:
        print("\t" + lang.title())