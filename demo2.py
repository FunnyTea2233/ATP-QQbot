import re

# 核心函数部分

def UUID(ID, isFull=False):

    if not hasattr(UUID, 'cache'):
        UUID.cache = {}
    if ID.casefold() in UUID.cache.keys():
        info = UUID.cache[ID.casefold()]
        return [info['ID'], info['FullUUID'] if isFull else info['UUID']]

    from urllib.request import urlopen, Request, quote
    from urllib.error import HTTPError
    import urllib

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    url = Request('https://playerdb.co/api/player/minecraft/' +
                  quote(ID), headers=headers)

    try:
        r = urlopen(url, timeout=10)
    except urllib.error.HTTPError:
        UUID.cache[ID.casefold()] = {
            'ID': ID, 'UUID': 'The name does not exist. ', 'FullUUID': 'The name does not exist. '}
        return [ID, 'The name does not exist. ']

    temp_scope = {'true': True, 'false': False}
    result = eval(str(r.read(), encoding="utf-8"), temp_scope)

    ansID = result['data']['player']['username']
    ansUUID = result['data']['player']['raw_id']
    ansFullUUID = result['data']['player']['id']

    UUID.cache[ansID.casefold()] = {'ID': ansID,
                                    'UUID': ansUUID, 'FullUUID': ansFullUUID}
    return [ansID, (ansFullUUID if isFull else ansUUID)]


def skinAndCape(UUID):

    if not hasattr(skinAndCape, 'cache'):
        skinAndCape.cache = {}
    if UUID in skinAndCape.cache.keys():
        info = skinAndCape.cache[UUID]
        return [info['UUID'], [info['ID'], info['skin'], info['cape']]]

    import base64
    from urllib.request import urlopen, Request, quote
    from urllib.error import HTTPError
    import urllib

    try:
        r = urlopen(
            'https://sessionserver.mojang.com/session/minecraft/profile/' + UUID)
    except urllib.error.HTTPError:
        return [UUID, [None, 'The UUID does not exist', 'The UUID does not exist']]
    result = eval(str(r.read(), encoding="utf-8"))
    value = result['properties'][0]['value']
    decriedValue = eval(base64.b64decode(value).decode("utf-8"))

    ID = decriedValue['profileName']
    skin = decriedValue['textures']['SKIN']['url']
    try:
        cape = decriedValue['textures']['CAPE']['url']
    except KeyError:
        cape = 'The player has no cape. '
    skinAndCape.cache[UUID] = {'UUID': UUID,
                               'ID': ID, 'skin': skin, 'cape': cape}
    return [UUID, [ID, skin, cape]]


# 封装函数部分

def getHelp(commands):
    func_docs = {
        'uuid': 'Show players\' UUIDs. ',
        'fulluuid': 'Show players\' full UUIDs. ',
        'skin': 'Show players\' skins. ',
        'cape': 'Show players\' capes. ',
        'help': 'Get help of commands. ',
        'about': 'Get information of this program. ',
        'clear':'Clear screen.'
    }
    use_docs = {
        'uuid': '>>> uuid ID_1 ID_2 ID_3 ...',
        'fulluuid': '>>> fulluuid ID_1 ID_2 ID_3 ...',
        'skin':  '>>> skin ID_1 ID_2 ID_3 ...',
        'cape': '>>> cape ID_1 ID_2 ID_3 ...',
        'help': '>>> help command_1 command_2 command_3 ...',
        'about': '>>> about',
        'clear': '>>> clear'
    }
    if commands:
        for i in commands:
            try:
                print('    ' + use_docs[i] + '\n    ' + func_docs[i])
            except KeyError:
                print('    "' + i + '" is not defined. ')
    else:
        print('    >>> command arg_1 arg_2 ...')
        print('    commands:')
        for command, doc in func_docs.items():
            print('        ' + command + ': ' + doc)
        print('    e.g. >>> uuid CYWVS Jack')
        print('    Use ">>> help (command)" for more info. ')


def getUUID(IDs):
    for i in IDs:
        ansID, ansUUID = UUID(i)
        print('    ' + ansID + ': ' + ansUUID)


def getFullUUID(IDs):
    for i in IDs:
        ansID, ansFullUUID = UUID(i, isFull=True)
        print('    ' + ansID + ': ' + ansFullUUID)


def getSkinURL(IDs):
    for i in IDs:
        if UUID(i)[1] == 'The name does not exist. ':
            print('    '+i+': The name does not exist.')
            continue
        else:
            info = skinAndCape(UUID(i)[1])
            ID = info[1][0]
            skinURL = info[1][1]
            print('    ' + ID + ':', skinURL)


def getCapeURL(IDs):
    for i in IDs:
        if UUID(i)[1] == 'The name does not exist. ':
            print('    '+i+': The name does not exist.')
            continue
        else:
            info = skinAndCape(UUID(i)[1])
            ID = info[1][0]
            capeURL = info[1][2]
            print('    ' + ID + ':', capeURL)


def getAbout(args):
    # if args:
    #     print('    The command "about" doesn\'t need any args.')
    print('''
    ABOUT
    A program to inquire accounts of Minecraft JE.
    By CYWVS

    ********        ********
    *      *        *      *
    *      *        *      *
    ************************
           *        *
        ****        ****
        *              *
        *   ********   *
        *****      *****
    ''')


def clearScreen(args):
    print('\n' * 233)

dictOfFunctions = {
    'uuid': getUUID,
    'fulluuid': getFullUUID,
    'skin': getSkinURL,
    'cape': getCapeURL,
    'help': getHelp,
    'about': getAbout,
    'clear': clearScreen
}

# 主程序


while True:
    try:
        splitInput = re.findall(r'(\w+|".*?")', input('>>> '))  # 将输入分隔
        if not splitInput:
            continue
        command, *args = splitInput
        command = command.casefold()

        if not command:
            continue
        if args:
            dictOfFunctions[command](args)
        else:
            if command in ['help', 'about', 'clear']:
                dictOfFunctions[command](None)
            else:
                getHelp([command])
    except (Exception) as error:
        print()
        print('    Error:', error)
        print('    Try again.')