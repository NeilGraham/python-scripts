print()


story = []


story.append("It was a {adjective}, cold November day. I woke up " +
"to the {adjective} smell of {type of bird} roasting in the " +
"{room in a house} downstairs. I {verb (past tense)} down the " +
"stairs to see if I could help {verb} the dinner. My mom said, " +
"\"See if {relative's name} needs a fresh {noun}.\" So I " +
"carried a tray of glasses full of {a liquid} into the {verb " +
"ending in -ing} room. When I got there, I couldn't believe my " +
"{part of the body (plural)}! There were {plural noun} {verb " +
"ending in -ing} on the {noun}!")


#Gather parts of speech (pos) between curly braces in story
def parse_pos (story):

    b = 0
    pos = []
    for y in range(0, len(story)):
        if story[y] == '{':
            b = y + 1
        if story[y] == '}':
            pos.append(story[b:y])
    return pos


#In story, replace parts of speech with inputs, then return finished story
def finish_story (story, inputs):

    finished_story = ''
    x = 0
    b = 0
    for y in range(0, len(story)):
        if story[y] == '{':
            finished_story += story[b:y] + '{}'.format(inputs[x])
            x += 1
        if story[y] == '}':
            b = y + 1
    return finished_story


def replace_pos (pos):

    pos_replacements = [''] * len(pos)
    print('Type in your own parts of speech.')
    print('(Input a number to rewrite that part of speech)')
    for y in range(0, len(pos)):
        print('(' + str(y+1) + '/' + str(len(pos)) + ') ' + pos[y] + ': ', end='')
        pos_input = input()
#        if represents_int(pos_input):
#            if int(pos_input) >= 1 and int(pos_input) <= len(pos):
#                y -= 1
#                pos_input_secondary = 1
#                while int(pos_input_secondary) >= 1 and int(pos_input_secondary) <= len(pos):
#                    print('    (' + pos_input + '/' + str(len(pos)) + ') ' + pos[int(pos_input) - 1] + ': ', end='')
#                    pos_input_secondary = input()
#                    if represents_int(pos_input_secondary):
#                        if int(pos_input) >= 1 and int(pos_input) <= len(pos):
#                            pos_input = int(pos_input_secondary)
#                    else:
#                        pos_replacements[int(pos_input)-1] = pos_input_secondary
#        else:
#            pos_replacements[y] = pos_input
        pos_replacements[y] = pos_input
    return pos_replacements


def represents_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def test():

    pos = parse_pos(story[0])
    pos = replace_pos(pos)
    print(finish_story(story[0], pos))


test()
