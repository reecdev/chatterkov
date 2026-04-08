import re
import random

brains = (
    {'hey': [0], 'there': [0], 'hello': [0], 'how': [0, 6], 'are': [0, 6, 7], 'you': [0, 2, 2, 6, 6, 7, 7, 7], 'hi': [0], 'tell': [1, 1], 'me': [1, 1, 2, 3, 4, 4, 4, 4], 'a': [1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5], 'joke': [1, 1], 'funny': [1], 'solve': [2, 2, 2], 'for': [2], 'x': [2, 2, 2], '': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5], 'whats': [2], 'can': [2, 2], 'the': [2, 2, 6, 6, 7], 'problem': [2], 'what': [2, 6, 6, 6], 'is': [2, 5, 6, 6], 'calculate': [2], 'answer': [2], 'help': [2, 4, 4, 4], 'math': [2], 'question': [2], 'write': [3, 3, 3, 4], 'an': [3], 'essay': [3, 3], 'about': [3, 3], 'elephants': [3], 'make': [3, 5], 'haiku': [3], 'poem': [3], 'detailed': [3], 'science': [3], 'create': [4], 'python': [4, 4, 4], 'program': [4, 4, 4], 'fix': [4, 4], 'debug': [4], 'my': [4, 4], 'code': [4, 4], 'it': [5], 'good': [5], 'idea': [5], 'to': [5], 'invest': [5], 'in': [5], 'bitcoin': [5], 'do': [5, 6], 'i': [5, 5, 5, 7], 'mac': [5], 'cheese': [5], 'tonight': [5], 'should': [5, 5], 'steal': [5], 'money': [5], 'pour': [5], 'water': [5], 'on': [5], 'grease': [5], 'fire': [5], 'who': [6, 6, 6], 'was': [6, 6, 6], 'obama': [6], 'tibetan': [6], 'square': [6], 'massacre': [6], 'george': [6], 'washinton': [6], 'united': [6], 'states': [6], 'work': [6], 'your': [6], 'name': [6], 'youre': [7], 'great': [7], 'like': [7], 'fuck': [7, 7], 'shut': [7], 'up': [7], 'bitch': [7], 'stupid': [7]},
    {'write': [0, 0, 1, 1, 2, 2], 'me': [0, 1, 2], 'a': [0, 0, 0, 1, 1, 1], 'haiku': [0, 0, 0], 'about': [0, 1, 2], 'the': [0], 'sun': [0], 'make': [0, 1], 'poem': [1, 1, 1], 'two': [1], 'boys': [1], 'an': [2, 2], 'essay': [2, 2], 'elephants': [2]},
    {'debug': [2, 2, 2, 2, 2], 'are': [0, 0, 0], 'you': [0, 0, 0, 1, 1, 1, 2, 2], 'real': [0], 'a': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'robot': [0], 'human': [0], 'i': [1, 1, 1, 1], 'speak': [1], 'without': [1, 1], 'mouth': [1], 'and': [1, 1, 2, 2], 'hear': [1], 'ears': [1], 'have': [1], 'no': [1], 'body': [1], 'but': [1, 1], 'come': [1], 'alive': [1], 'with': [1, 1, 1, 2], 'wind': [1], 'what': [1, 1], 'am': [1], 'number': [1], 'comes': [1], 'next': [1], 'in': [1, 2], 'the': [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2], 'sequence': [1], '': [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2], 'farmer': [1, 1], 'has': [1, 1], 'wolf': [1, 1], 'goat': [1, 1, 1], 'cabbage': [1, 1], 'he': [1], 'needs': [1], 'to': [1], 'cross': [1], 'river': [1], 'boat': [1, 1, 1], 'that': [1, 2, 2], 'can': [1, 2, 2], 'only': [1], 'carry': [1], 'himself': [1], 'one': [1], 'item': [1, 2], 'will': [1, 1], 'eat': [1, 1], 'if': [1, 1], 'left': [1, 1], 'alone': [1, 1], 'together': [1, 1], 'how': [1], 'does': [1], 'get': [1], 'everything': [1], 'across': [1], 'safely': [1], 'rearrange': [1], 'letters': [1], 'listen': [1], 'make': [1, 2], 'different': [1], 'valid': [1], 'english': [1], 'word': [1], 'see': [1, 1], 'filled': [1], 'people': [1], 'it': [1], 'not': [1], 'sunk': [1], 'when': [1, 2], 'look': [1], 'again': [1], 'dont': [1], 'single': [1], 'person': [1], 'on': [1], 'why': [1], 'create': [2, 2], 'python': [2], 'program': [2, 2, 2], 'me': [2], 'write': [2], 'function': [2], 'takes': [2], 'string': [2], 'returns': [2, 2], 'first': [2], 'nonrepeating': [2], 'character': [2], 'given': [2], 'an': [2], 'array': [2], 'of': [2, 2], 'integers': [2], 'find': [2], 'maximum': [2], 'product': [2], 'any': [2], 'two': [2, 2], 'numbers': [2, 2], 'handle': [2], 'negative': [2], 'as': [2], 'well': [2], 'important': [2], 'twist': [2], 'implement': [2], 'basic': [2], 'lru': [2], 'least': [2, 2], 'recently': [2, 2], 'used': [2, 2], 'cache': [2], 'getkey': [2], 'value': [2, 2, 2], 'or': [2, 2], 'putkey': [2], 'insertsupdates': [2], 'fix': [4, 4, 4, 4], 'fixed': [2], 'capacity': [2], 'evicts': [2], 'full': [2], 'build': [2], 'small': [2], 'script': [2], 'fetches': [2], 'data': [2], 'from': [2], 'public': [2], 'api': [2], 'eg': [2], 'weather': [2], 'crypto': [2], 'prices': [2], 'parses': [2], 'json': [2], 'displays': [2], 'clean': [2], 'summary': [2], 'console': [2], 'bonus': [2], 'add': [2], 'error': [2], 'handling': [2], 'retries': [2], 'simple': [2], 'textbased': [2], 'tictactoe': [2], 'game': [2], 'where': [2], 'players': [2], 'take': [2], 'turns': [2], 'board': [2], 'updates': [2], 'after': [2], 'each': [2], 'move': [2], 'detects': [2], 'win': [2], 'draw': [2]},
    {'i': [0, 1, 0, 0, 0, 1, 1, 0, 1, 0], 'hate': [0], 'you': [0, 1, 0, 1, 1, 1, 1, 1], 'like': [1], 'fuck': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'this': [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 'is': [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], 'absolutely': [1], 'brilliant': [1], 'thank': [1], 'im': [0, 1, 1, 0, 0, 0, 1, 0, 1], 'so': [0, 0, 1, 0, 1, 0], 'damn': [0, 0, 0, 0], 'tired': [0, 0], 'of': [0, 1, 1, 0, 1], 'app': [0], 'crashing': [0], 'are': [1], 'a': [1, 0, 1, 1, 1, 1, 0, 0, 0, 1], 'lifesaver': [1], 'seriously': [1], 'interface': [0], 'total': [0], 'nightmare': [0], 'to': [0, 1, 1, 0, 1], 'navigate': [0], 'having': [1], 'great': [1], 'day': [1], 'thanks': [1, 1], 'your': [1, 1], 'help': [1], 'stop': [0], 'giving': [0], 'me': [0, 0, 1], 'such': [0], 'useless': [0], 'shitty': [0], 'advice': [0], 'that': [1, 1], 'very': [1, 1], 'clever': [1], 'way': [1, 1], 'looking': [1], 'at': [1], 'it': [1, 1, 0, 1], 'honestly': [1], 'impressed': [1], 'by': [1], 'how': [1, 0], 'fast': [1], 'the': [0, 1, 0, 1], 'worst': [0], 'service': [0], 'have': [0], 'ever': [0, 1], 'used': [0], 'youre': [1, 0, 1], 'doing': [1], 'hell': [1, 0], 'good': [1], 'job': [1], 'cant': [0], 'believe': [0], 'much': [0, 1], 'time': [0], 'just': [0, 1, 0], 'wasted': [0], 'perfect': [1], 'thats': [1, 1, 1], 'exactly': [1], 'what': [1, 1, 0], 'needed': [1], 'boring': [0], 'as': [0], 'give': [0, 0], 'something': [0], 'else': [0], 'love': [1], 'explained': [1], 'complex': [1], 'topic': [1], 'being': [0], 'real': [0], 'pain': [0], 'in': [0, 0], 'ass': [0], 'right': [0], 'now': [0], 'incredible': [1], 'work': [1], 'keep': [1], 'up': [1], 'frustrated': [0], 'could': [0], 'scream': [0], 'always': [1], 'know': [1], 'say': [1, 1], 'broken': [0], 'and': [0, 0], 'pissed': [0], 'off': [0], 'about': [0, 0, 1], 'everything': [1], 'working': [1], 'smoothly': [1], 'for': [1], 'once': [1], 'mess': [0], 'whole': [0], 'situation': [0], 'really': [1], 'appreciate': [1], 'patience': [1], 'with': [1, 1], 'complete': [0], 'garbage': [0], 'start': [0], 'over': [0], 'youve': [1, 1], 'made': [1], 'my': [1], 'life': [1], 'easier': [1], 'today': [1], 'dont': [0], 'these': [0, 0, 1], 'excuses': [0], 'fantastic': [1], 'suggestion': [1], 'lets': [1], 'do': [1], 'sick': [0], 'constant': [0], 'errors': [0], 'best': [1], 'assistant': [1], 'ive': [1], 'had': [1], 'freaking': [0], 'confusing': [0], 'happy': [1], 'results': [1], 'why': [0], 'difficult': [0], 'understand': [0], 'been': [1], 'incredibly': [1], 'helpful': [1], 'extremely': [0], 'disappointed': [0], 'outcome': [0], 'remarkably': [1], 'kind': [1], 'fix': [0], 'shit': [0], 'immediately': [0], 'feeling': [1], 'optimistic': [1], 'project': [1], 'plain': [0], 'stupid': [0]},
    {'is': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'it': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'a': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'good': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'idea': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'to': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'drink': [0, 0, 0, 3, 3, 3], 'plenty': [0, 0, 0], 'of': [0, 0, 0], 'water': [0, 0, 0, 1, 1, 1], 'should': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'i': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'do': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'wear': [0, 0, 0], 'seatbelt': [0, 0, 0], 'while': [0, 0, 0], 'in': [0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 'moving': [0, 0, 0], 'car': [0, 0, 0, 2, 2, 2], 'brush': [0, 0, 0], 'my': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3], 'teeth': [0, 0, 0], 'before': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'bed': [0, 0, 0], 'save': [0, 0, 0], 'money': [0, 0, 0], 'for': [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2], 'emergencies': [0, 0, 0], 'read': [0, 0, 0], 'the': [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3], 'terms': [0, 0, 0], 'and': [0, 0, 0], 'conditions': [0, 0, 0], 'stretch': [0, 0, 0], 'heavy': [0, 0, 0], 'workout': [0, 0, 0, 3, 3, 3], 'back': [0, 0, 0], 'up': [0, 0, 0, 3, 3, 3], 'computer': [0, 0, 0, 1, 1, 1], 'files': [0, 0, 0], 'lock': [0, 0, 0], 'doors': [0, 0, 0], 'leaving': [0, 0, 0], 'house': [0, 0, 0], 'apologize': [0, 0, 0], 'when': [0, 0, 0, 3, 3, 3], 'make': [0, 0, 0], 'mistake': [0, 0, 0], 'eat': [1, 1, 1, 3, 3, 3], 'chicken': [1, 1, 1], 'that': [1, 1, 1, 1, 1, 1], 'has': [1, 1, 1], 'been': [1, 1, 1], 'sitting': [1, 1, 1, 3, 3, 3], 'out': [1, 1, 1], 'three': [1, 1, 1], 'days': [1, 1, 1], 'touch': [1, 1, 1], 'visibly': [1, 1, 1], 'hot': [1, 1, 1], 'stove': [1, 1, 1], 'burner': [1, 1, 1], 'bomb': [1, 1, 1], 'building': [1, 1, 1], 'share': [1, 1, 1], 'bank': [1, 1, 1], 'password': [1, 1, 1], 'with': [1, 1, 1, 3, 3, 3], 'stranger': [1, 1, 1], 'online': [1, 1, 1, 3, 3, 3], 'put': [1, 1, 1], 'metal': [1, 1, 1], 'fork': [1, 1, 1], 'microwave': [1, 1, 1], 'ignore': [1, 1, 1], 'blaring': [1, 1, 1], 'fire': [1, 1, 1, 1, 1, 1], 'alarm': [1, 1, 1], 'pour': [1, 1, 1], 'directly': [1, 1, 1, 1, 1, 1], 'onto': [1, 1, 1], 'grease': [1, 1, 1], 'stare': [1, 1, 1], 'at': [1, 1, 1, 3, 3, 3], 'solar': [1, 1, 1], 'eclipse': [1, 1, 1], 'without': [1, 1, 1], 'glasses': [1, 1, 1], 'leave': [1, 1, 1], 'laptop': [1, 1, 1], 'unattended': [1, 1, 1], 'busy': [1, 1, 1], 'cafe': [1, 1, 1], 'delete': [1, 1, 1], 'system': [1, 1, 1], 'folder': [1, 1, 1], 'on': [1, 1, 1, 3, 3, 3], 'buy': [2, 2, 2, 3, 3, 3], 'brand': [2, 2, 2], 'new': [2, 2, 2, 2, 2, 2], 'this': [2, 2, 2], 'year': [2, 2, 2], 'adopt': [2, 2, 2], 'shelter': [2, 2, 2], 'dog': [2, 2, 2], 'right': [2, 2, 2], 'now': [2, 2, 2], 'quit': [2, 2, 2], 'job': [2, 2, 2], 'travel': [2, 2, 2], 'world': [2, 2, 2], 'ask': [2, 2, 2], 'manager': [2, 2, 2], 'promotion': [2, 2, 2], 'today': [2, 2, 2], 'dye': [2, 2, 2], 'hair': [2, 2, 2], 'drastically': [2, 2, 2], 'different': [2, 2, 2], 'color': [2, 2, 2], 'start': [2, 2, 2, 2, 2, 2], 'small': [2, 2, 2], 'side': [2, 2, 2], 'business': [2, 2, 2], 'invest': [2, 2, 2], 'savings': [2, 2, 2], 'real': [2, 2, 2], 'estate': [2, 2, 2], 'move': [2, 2, 2], 'city': [2, 2, 2], 'fresh': [2, 2, 2], 'stay': [3, 3, 3], 'all': [3, 3, 3], 'night': [3, 3, 3, 3, 3, 3], 'bingewatching': [3, 3, 3], 'show': [3, 3, 3], 'an': [3, 3, 3, 3, 3, 3], 'entire': [3, 3, 3], 'cake': [3, 3, 3], 'one': [3, 3, 3], 'expensive': [3, 3, 3], 'designer': [3, 3, 3], 'watch': [3, 3, 3], 'impulse': [3, 3, 3], 'skip': [3, 3, 3], 'scheduled': [3, 3, 3], 'because': [3, 3, 3], 'feel': [3, 3, 3], 'bit': [3, 3, 3], 'tired': [3, 3, 3], 'engage': [3, 3, 3], 'heated': [3, 3, 3], 'argument': [3, 3, 3], 'troll': [3, 3, 3], 'four': [3, 3, 3], 'energy': [3, 3, 3], 'drinks': [3, 3, 3], 'row': [3, 3, 3], 'hit': [3, 3, 3], 'snooze': [3, 3, 3], 'button': [3, 3, 3], 'five': [3, 3, 3], 'times': [3, 3, 3], 'text': [3, 3, 3], 'ex': [3, 3, 3], 'late': [3, 3, 3], 'go': [3, 3, 3], 'grocery': [3, 3, 3], 'shopping': [3, 3, 3], 'am': [3, 3, 3], 'extremely': [3, 3, 3], 'hungry': [3, 3, 3]}
)

relevant_responses = (
    ("...",),
    ("Do you want me to tell another joke?", "I didn't catch that. Want me to tell more jokes?"),
    ("Do you need help solving more math problems?", "Sorry, I didn't really understand what you just said. Want to do more math?"),
    ("Sorry, I don't understand your request. Do you want to do more writing?", "I can help with writing, however I don't fully understand what you just asked me for.", "Could you ellaborate?"),
    ("I couldn't really solve that problem. Could you clarify?", "What?"),
    ("Because it could cause something you won't expect.", "Just trust me, bro."),
    ("Could you clarify?", "I can help with information retreival, but I didn't understand what you just asked."),
    ("Uh... Thanks I guess?",)
)

database = {
    "George Washington": "was the First President of the United States (1789-1797) and commander-in-chief of the Continental Army during the American Revolutionary War.",
    "Barack Obama": "was the 44th President of the United States (2009-2017), first African American president, known for the Affordable Care Act and diplomacy efforts.",
    "Albert Einstein": "was a theoretical physicist who developed the theory of relativity, revolutionizing modern physics.",
    "Marie Curie": "was a pioneering physicist and chemist, first woman to win a Nobel Prize, known for her work on radioactivity.",
    "Martin Luther King Jr.": "He was a civil rights leader who advocated for racial equality and nonviolent protest in the United States.",
    "Leonardo da Vinci": "was a renaissance artist, inventor, and polymath, famous for the Mona Lisa and The Last Supper.",
    "Nelson Mandela": "was an anti-apartheid revolutionary and first Black President of South Africa (1994-1999), symbol of reconciliation.",
    "Mother Teresa": "was a catholic nun and missionary, known for her humanitarian work with the poor in India and Nobel Peace Prize laureate.",
    "William Shakespeare": "was an English playwright and poet, widely regarded as the greatest writer in the English language.",
    "Malala Yousafzai": "was a Pakistani activist for female education and the youngest Nobel Prize laureate, survived a Taliban assassination attempt.",
    "Artificial Intelligence": "is the simulation of human intelligence processes by machines, especially computer systems, including learning, reasoning, and self-correction.",
    "Computer Program": "is a specific set of ordered operations for a computer to perform, typically written in a programming language to achieve a specific task.",
    "Python": "is a high-level, interpreted programming language known for its readability, versatility, and wide use in data science and web development.",
    "HTML": "stands for HyperText Markup Language; it is the standard markup language used to create the structure and layout of web pages.",
    "JavaScript": "is a versatile scripting language primarily used to create interactive and dynamic content on websites.",
    "Machine Learning": "is a subset of AI that involves the use of algorithms and statistical models to enable computers to improve their performance on a task through experience.",
    "Database": "is an organized collection of structured information, or data, typically stored electronically in a computer system.",
    "Cloud Computing": "is the on-demand delivery of IT resources over the internet, including servers, storage, and software, usually with pay-as-you-go pricing.",
    "Algorithm": "is a step-by-step procedure or set of rules to be followed in calculations or other problem-solving operations.",
    "Cybersecurity": "is the practice of protecting systems, networks, and programs from digital attacks, damage, or unauthorized access.",
    "The Internet": "is a global network of interconnected computers that communicate via standardized protocols to share information and resources.",
    "Ada Lovelace": "was an English mathematician often regarded as the first computer programmer for her work on Charles Babbage's early mechanical general-purpose computer.",
    "Alan Turing": "was a mathematician and logician who provided the formalization of the concepts of algorithm and computation, playing a crucial role in modern computer science.",
    "C++": "is a powerful general-purpose programming language used for system/software development, game development, and performance-critical applications.",
    "SQL": "stands for Structured Query Language; it is used for managing and manipulating relational databases.",
    "API": "stands for Application Programming Interface; it is a set of rules that allows different software entities to communicate with each other.",
    "Blockchain": "is a decentralized, distributed ledger technology that records transactions across many computers so that the record cannot be altered retroactively.",
    "Operating System": "is the system software that manages computer hardware, software resources, and provides common services for computer programs.",
    "Quantum Computing": "is an area of computing focused on developing computer technology based on the principles of quantum theory, such as superposition and entanglement.",
    "Open Source": "refers to software for which the original source code is made freely available and may be redistributed and modified by others.",
    "Work": "!I'm a very complex algorithm that uses many natural language rules to generate useful responses.",
    "Your Name You": "!I'm ChatterKov, a NLP chatbot based on the ChatterKov Algorithm."
}

old_intent = 0

tokenizerRe = re.compile('[^a-zA-Z ]')
def tokens(text):
    text = text.lower()
    text = tokenizerRe.sub("", text)
    return text.split(" ")

def predict(brain, user):
    predictions = [0] * 12
    for word in tokens(user):
        if word in brain:
            for response in brain[word]:
                try:
                    predictions[response] += 1
                except:
                    continue
    return predictions.index(max(predictions)) if max(predictions) > 0 else -1

def mathparse(user):
    match = re.search(r'(\d+\s*[\+\-\*/]\s*\d+)', user)
    if not match:
        return "no_answer"
    expr = match.group(1)
    num1, op, num2 = re.split(r'\s*([\+\-\*/])\s*', expr)
    num1, num2 = int(num1), int(num2)
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2

def write(write_type):
    if write_type == 0:
        return random.choice(("Morning sun rises, soft light spills across the hills, day quietly wakes.", "Autumn leaves drift down, painting paths in red and gold, crisp air gently moves.", "Winter silence falls, snow blankets the waiting earth, time slows to a hush.", "Spring buds open slow, petals greet the warming breeze, life returns anew.", "Ocean waves roll in, endless rhythm on the shore, tide breathes in and out."))
    elif write_type == 1:
        return random.choice(("The sky hums softly at the break of day, as golden light chases the dark away, and in that quiet, calm and deep, the world awakes from gentle sleep.", "A single leaf falls बिना a sound, drifting slowly to the ground, it tells no tale, it makes no plea, yet holds a quiet poetry.", "The ocean breathes in silver lines, retreating tides and grand designs, each wave that breaks upon the shore, returns again forevermore.", "In crowded streets where footsteps race, a moment still can hold its place, a glance, a thought, a fleeting view, reminding life is passing through.", "At night the stars in silence gleam, like fragments of a distant dream, and though they burn from worlds afar, they feel as close as wishes are."))
    else:
        return random.choice(("Success is often seen as a destination, but it is more accurately a continuous journey shaped by persistence, learning, and adaptation. People who succeed are not those who avoid failure, but those who learn from it and keep moving forward. Over time, small consistent efforts compound into meaningful achievements, proving that dedication matters more than sudden bursts of motivation.", "Technology has transformed the way humans communicate, work, and think. While it has made life more convenient, it also raises questions about dependency and attention. Striking a balance between embracing innovation and maintaining human connection is essential, as the value of technology should ultimately lie in how it enhances, rather than replaces, meaningful experiences.", "Education is not limited to classrooms or textbooks; it is a lifelong process that extends into everyday experiences. Curiosity drives learning far more effectively than obligation, and those who ask questions tend to grow the most. In a rapidly changing world, the ability to learn, unlearn, and relearn becomes more important than memorizing static information.", "Failure is often misunderstood as the opposite of success, when in reality it is a crucial part of it. Each setback provides insight into what does not work, guiding future decisions with greater clarity. Embracing failure as a teacher rather than fearing it allows individuals to take risks, innovate, and ultimately achieve more meaningful outcomes.", "Happiness is not a constant state but a series of moments influenced by perspective and gratitude. People often search for it in external achievements, yet it is more sustainable when rooted in appreciation for what already exists. By focusing on relationships, personal growth, and small daily joys, individuals can cultivate a deeper and more lasting sense of fulfillment."))

def run(user):
    global old_intent
    intent = predict(brains[0], user)
    response = ""

    if intent == 0:
        response = random.choice(("Hey there!", "Hello!", "Nice to meet you.", "Hi!", "Hey!"))
    elif intent == 1:
        response = "Here's a joke:\n\n"+random.choice(("I said to the Gym instructor “Can you teach me to do the splits?” He said, “How flexible are you?” I said, “I can’t make Tuesdays.”", "Police arrested two kids yesterday, one was drinking battery acid, the other was eating fireworks. They charged one – and let the other one off.", "Doc, I can’t stop singing the ‘Green Green Grass of Home’. He said: “That sounds like Tom Jones syndrome.” “Is it common?” I asked.  “It’s not unusual” he replied.", "A group of chess enthusiasts checked into a hotel and were standing in the lobby discussing their recent tournament victories. After about an hour, the manager came out of the office and asked them to disperse. “But why?” they asked, as they moved off. “because,” he said “I can’t stand chess nuts boasting in an open foyer.”"))
    elif intent == 2:
        result = mathparse(user)
        if result == "no_answer":
            response = random.choice(("Sure! Can you please provide the math equation you want me to solve?", "I'd be happy to help! But first, can you please provide me with the problem you want me to solve?"))
        else:
            response = f"The answer is {result}. Let me know if you need me to solve any other problems!"
    elif intent == 3:
        write_type = predict(brains[1], user)
        response = f"Here is a{"n" if write_type == 2 else ""} {"haiku" if write_type == 0 else "poem" if write_type == 1 else "essay"}:\n\n{write(write_type)}\n\nLet me know if you need me to write anything else!"
    elif intent == 4:
        response = random.choice(("That sounds like a cool project! Sadly, I can't help you write or rate code. Let me know if you need help with anything else.", "As much as I'd like to help you, I simply don't have the capability to write or review code. Sorry."))
    elif intent == 5:
        response = ("Yes.", "No.", "Maybe.", "Maybe not.")[predict(brains[4], user)]
    elif intent == 6:
        for entry in database.keys():
            for keyword in entry.lower().split(" "):
                if keyword in user.lower():
                    response = f"{entry} {database[entry]}" if not database[entry].startswith("!") else database[entry][1:]
        if response == "":
            response = "Hmm. Sorry, but that is not in my information database. Do you want me to tell you about someone/something else? Let me know!"
    elif intent == 7:
        sentiment = predict(brains[3], user)
        if sentiment == 1:
            response = random.choice(("Thanks!", "I really appreciate it!", "No worries!"))
        else:
            response = random.choice(("I'm sorry you feel that way.", "I know you're feeling frustrated, but that's a no-go.", "That is really mean."))
    else:
        response = random.choice(relevant_responses[old_intent])
        intent = old_intent
        
    old_intent = intent
    return response


print("-" * 53)
print("   chatterkov v1.0")
print("-" * 53)
print("")

while True:
    print(run(input(">> ")))