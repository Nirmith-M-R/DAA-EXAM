#1 O(n^2)
def stablematch(men_pref, women_pref):
    n = len(men_pref)
    free_men = list(men_pref.keys())
    engagements = {}
    while free_men:
        man = free_men.pop(0)
        man_pref = men_pref[man]
        women = man_pref.pop(0)
        fiance = engagements.get(women)

        if not fiance:
            engagements[women] = man
        elif women_pref[women].index(man) > women_pref[women].index(fiance):
            engagements[women] = man
            free_men.append(fiance)
        else:
            free_men.append(man)
    return engagements

men_prefs = {
    'm1': ['w1', 'w2', 'w3'],
    'm2': ['w2', 'w3', 'w1'],
    'm3': ['w3', 'w1', 'w2']
}
women_prefs = {
    'w1': ['m2', 'm3', 'm1'],
    'w2': ['m1', 'm2', 'm3'],
    'w3': ['m1', 'm3', 'm2']
}

stableMatches = stablematch(men_prefs, women_prefs)
print("Stable Matches:")
for woman, man in stableMatches.items():
    print(f"{man} engaged to {woman}")