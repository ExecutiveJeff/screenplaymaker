import pickle
import random
import string


def names():
    notes = open('names.txt', 'r')
    note = []
    for n in notes:
        note.append(n)
    name = random.choice(note)
    name = name.strip()
    return name

line_length = raw_input("What is the largest number of characters per dialogue? ")
line_length = int(line_length)
name1 = names().upper()
name2 = names().upper()
name3 = names().upper()
name4 = names().upper()

def main():
    screen_play()
    print 'END SCENE'


def location():
    locs = open('locations.txt', 'r')
    loc = []
    for l in locs:
        loc.append(l)
    location = random.choice(loc)
    location = location.strip()
    return location


def deets():
    details = open('details.txt', 'r')
    dee = []
    for d in details:
        dee.append(d)
    deet = random.choice(dee)
    deet = deet.strip()
    return deet


def build_line():
    chain = pickle.load(open("chain.p", "rb"))
    new_line = []
    sword1 = "BEGIN"
    sword2 = "NOW"
    while True:
        sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        if sword2 == "END":
            break
        new_line.append(sword2)
    line = ' '.join(new_line)
    line = line + '\n'
    return line


def stage_direction():
    chain = pickle.load(open("chain.p", "rb"))
    direct = []
    sword1 = "BEGIN"
    sword2 = "NOW"
    while True:
        sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        if sword2 == "END":
            break
        direct.append(sword2)
    stage = ' '.join(direct).upper()
    stage = stage + '\n'
    return stage


def name_swap(line):
    notes = open('names.txt', 'r')
    line = string.replace(line, "NAME1", name1)
    line = string.replace(line, "NAME2", name2)
    line = string.replace(line, "NAME3", name3)
    line = string.replace(line, "NAME4", name4)
    knots = notes.readlines()
    spl = line.split()
    for n in knots:
        if any(s in n for s in line):
            line = string.replace(line, n, name1)
    return line


def build_diag():
    output = ''
    length = random.randrange(1, line_length)
    while len(output) < length:
        output += (' ' + build_line())
    return output

def screen_play():
    title = build_line()
    title = title.upper()
    print name_swap(title)
    print deets()
    print location().upper()
    print name1 + ' ' + 'and' + " " + name2 + ' ' + 'and' + " " + name3 + ' ' + 'and' + " " + name4
    print name_swap(stage_direction())
    print name1 + ':' + ' ' + name_swap(build_diag())
    print name2 + ':' + ' ' + name_swap(build_diag())
    print name_swap(stage_direction())
    print name1 + ':' + ' ' + name_swap(build_diag())
    print name2 + ':' + ' ' + name_swap(build_diag())
    print name_swap(stage_direction())
    print name3 + ':' + ' ' + name_swap(build_diag())
    print name4 + ':' + ' ' + name_swap(build_diag())
    print name_swap(stage_direction())
    print name3 + ':' + ' ' + name_swap(build_diag())
    print name2 + ':' + ' ' + name_swap(build_diag())
    print name_swap(stage_direction())
    print name4 + ':' + ' ' + name_swap(build_diag())
    print name1 + ':' + ' ' + name_swap(build_diag())
    print name_swap(stage_direction())
    print name1 + ':' + ' ' + name_swap(build_diag())
    print name3 + ':' + ' ' + name_swap(build_diag())

if __name__ == '__main__':
    main()
