def matching(men, women):
    """
    implementation of stable matching problem in context of the mating ritual
    :param men: preferences of men {m:[w,w,w]} where men[m][0] = top preference, etc
    :param women: preferences of women where it is {w:{m:1, m:2, etc}}
    :return: matching as a dict {m:w}
    """

    rejected = {}
    for w in women:
        rejected[w] = set()

    tried = {}
    for m in men:
        tried[m] = set()

    match = {}
    matched = set()
    # iterate until all men haven't been matched or all men propose a to all the women
    while True:
        suitor = None
        for m in men:
            if m not in matched:
                suitor = m
                break
        if not suitor:
            for m in men:
                if len(tried[m]) < len(women):
                    suitor = m
                    break
        if not suitor:
            break

        mate = None
        for possible in men[suitor]:
            if suitor not in rejected[possible]:
                mate = possible
                break

        tried[suitor].add(mate)
        if mate not in match:
            match[mate] = suitor
            matched.add(suitor)
        else:
            current = match[mate]
            if women[mate][current] < women[mate][suitor]:
                rejected[mate].add(suitor)
            else:
                match[mate] = suitor
                rejected[mate].add(current)
                matched.add(suitor)
    return match

men_ = {"brad":["angelina", "jenn", "cindy"],
        "dave":["angelina", "cindy", "jenn"],
        "toast":["jenn", "cindy", "angelina"]}

women_ = {"angelina": {"brad":1, "dave":2, "toast":3},
          "jenn": {"brad":1, "toast":2, "dave":3},
          "cindy":{"toast":1, "brad":2, "dave":3}}



