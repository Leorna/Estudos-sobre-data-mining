from die import Die


die_1 = Die()
die_2 = Die()
die_3 = Die()


def gen_results(times):
    for i in range(times):
        result = die_1.roll() + die_2.roll() + die_3.roll()
        yield result