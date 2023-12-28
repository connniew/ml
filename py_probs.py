# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
def alarmclock(day, vacation):
    weekday = False
    
    if day >= 1 and day <= 5:
        weekday = True
    
    if (not weekday and not vacation) or (weekday and vacation):
        return "10:00"
    elif weekday and not vacation:
        return "7:00"
    else:
        return "off"

# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleepin(weekday, vacation):
    if vacation and weekday or not weekday:
        return True
    return False

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
def left2(str):
    return str[2:] + str[0:2]

# Determines whether a list is strictly ascending
def isascend(items):
    prev = items[0]
    
    for i in range(1, len(items)):
        if items[i] <= prev:
            return False
        prev = items[i]
    return True

# Shuffles a list by interleaving its halves
def shuffles(items, outShuffle=True):
    front = items[:len(items)//2]
    back = items[len(items)//2:]
    index = 0
    
    for i in range(0, len(items), 2):
        if out:
            front.insert(i+1, back[index])
        else:
            front.insert(i, back[index])
        index += 1
    return front

# Determines if int contains only odd digits 
def odddigitsonly(n):   
    for num in str(n):
        if int(num) % 2 == 0:
            return False
    return True

# Determine if int is a cyclops number (odd number of digits with a zero at the middle)
def cyclops(n):
    my_str = str(n)
    middle_index = len(my_str) // 2
    is_zero_front = False
    is_zero_end = False
    
    if len(my_str) % 2 == 0:
        return False
    
    if my_str[middle_index] == "0":
        is_zero_front = checkzero(my_str[:middle_index])
        is_zero_end = checkzero(my_str[middle_index+1:])
        return not(is_zero_front or is_zero_end)
    return False

def checkzero(n):
    for num in n:
        if num == "0":
            return True
    return False

# Determine if list of tuples is a domino cycle
def dominocycle(tiles):
    pip1 = [x[0] for x in tiles]
    pip2 = [x[1] for x in tiles]
    return pip2 == pip1[1:] + pip1[:1]

# Create a look and say sequence as in 312211 is read as "three 1s, two 2s, one 1" to create 111221.
def lookandsayseq(digits):
    count = 0
    my_str = ""
    prev = digits[0]
    
    for num in digits:
        if num == prev:
            count += 1
        else:
            my_str += str(count) + str(prev)
            count = 1
        prev = num
    my_str += str(count) + str(prev)
    return my_str

# Reverse the vowels in string
def reversevowels(text):
    my_text = list(text)
    vowels = [letter for letter in my_text if letter in "aeiouAEIOU"]
    vowels_reverse = vowels[::-1]
    k = 0
    
    for i in range(len(vowels)):
        if 47 < ord(vowels[i]) < 91:
            vowels_reverse[i] = chr(ord(vowels_reverse[i])-32)
        elif 47 < ord(vowels_reverse[i]) < 91:
            vowels_reverse[i] = chr(ord(vowels_reverse[i])+32)
    
    for j in range(len(my_text)):
        if my_text[j] in "aeiouAEIOU":
            my_text[j] = vowels_reverse[k]
            k += 1
    return "".join(my_text)  

# Convert string of intervals into list of ints
def expand(intervals):
    my_list = intervals.split(",")
    result = []
    
    if intervals:
        for x in my_list:
            if "-" in x:
                middle = x.index("-")
                first = int(x[:middle])
                last = int(x[middle+1:])
                result += list(range(first, last+1))
            else:
                result.append(int(x))
    return result

# Convert Spanish verb given its subject and tense
def conjugate(verb, subject, tense):    
    conjugations = {
        "ar": {
            "presente": {
                "yo": "o",
                "tú": "as", 
                "él": "a",
                "ella": "a",
                "usted": "a",
                "nosotros": "amos",
                "nosotras": "amos",
                "vosotros": "áis",
                "vosotras": "áis",
                "ellos": "an",
                "ellas": "an",
                "ustedes": "an",
            },
            "pretérito": {
                "yo": "é",
                "tú": "aste", 
                "él": "ó",
                "ella": "ó",
                "usted": "ó",
                "nosotros": "amos",
                "nosotras": "amos",
                "vosotros": "asteis",
                "vosotras": "asteis",
                "ellos": "aron",
                "ellas": "aron",
                "ustedes": "aron",
            },
            "imperfecto": {
                "yo": "aba",
                "tú": "abas", 
                "él": "aba",
                "ella": "aba",
                "usted": "aba",
                "nosotros": "ábamos",
                "nosotras": "ábamos",
                "vosotros": "abais",
                "vosotras": "abais",
                "ellos": "aban",
                "ellas": "aban",
                "ustedes": "aban",
            },
            "futuro": {
                "yo": "é",
                "tú": "ás", 
                "él": "á",
                "ella": "á",
                "usted": "á",
                "nosotros": "emos",
                "nosotras": "emos",
                "vosotros": "éis",
                "vosotras": "éis",
                "ellos": "án",
                "ellas": "án",
                "ustedes": "án",
            }
        }, 
        "er": {
            "presente": {
                "yo": "o",
                "tú": "es", 
                "él": "e",
                "ella": "e",
                "usted": "e",
                "nosotros": "emos",
                "nosotras": "emos",
                "vosotros": "éis",
                "vosotras": "éis",
                "ellos": "en",
                "ellas": "en",
                "ustedes": "en",
            },
            "pretérito": {
                "yo": "í",
                "tú": "iste", 
                "él": "ió",
                "ella": "ió",
                "usted": "ió",
                "nosotros": "imos",
                "nosotras": "imos",
                "vosotros": "isteis",
                "vosotras": "isteis",
                "ellos": "ieron",
                "ellas": "ieron",
                "ustedes": "ieron",
            },
            "imperfecto": {
                "yo": "ía",
                "tú": "ías", 
                "él": "ía",
                "ella": "ía",
                "usted": "ía",
                "nosotros": "íamos",
                "nosotras": "íamos",
                "vosotros": "íais",
                "vosotras": "íais",
                "ellos": "ían",
                "ellas": "ían",
                "ustedes": "ían",
            },
            "futuro": {
                "yo": "é",
                "tú": "ás", 
                "él": "á",
                "ella": "á",
                "usted": "á",
                "nosotros": "emos",
                "nosotras": "emos",
                "vosotros": "éis",
                "vosotras": "éis",
                "ellos": "án",
                "ellas": "án",
                "ustedes": "án",
            }
        }, 
        "ir": {
            "presente": {
                "yo": "o",
                "tú": "es", 
                "él": "e",
                "ella": "e",
                "usted": "e",
                "nosotros": "imos",
                "nosotras": "imos",
                "vosotros": "ís",
                "vosotras": "ís",
                "ellos": "en",
                "ellas": "en",
                "ustedes": "en",
            },
            "pretérito": {
                "yo": "í",
                "tú": "iste", 
                "él": "ió",
                "ella": "ió",
                "usted": "ió",
                "nosotros": "imos",
                "nosotras": "imos",
                "vosotros": "isteis",
                "vosotras": "isteis",
                "ellos": "ieron",
                "ellas": "ieron",
                "ustedes": "ieron",
            },
            "imperfecto": {
                "yo": "ía",
                "tú": "ías", 
                "él": "ía",
                "ella": "ía",
                "usted": "ía",
                "nosotros": "íamos",
                "nosotras": "íamos",
                "vosotros": "íais",
                "vosotras": "íais",
                "ellos": "ían",
                "ellas": "ían",
                "ustedes": "ían",
            },
            "futuro": {
                "yo": "é",
                "tú": "ás", 
                "él": "á",
                "ella": "á",
                "usted": "á",
                "nosotros": "emos",
                "nosotras": "emos",
                "vosotros": "éis",
                "vosotras": "éis",
                "ellos": "án",
                "ellas": "án",
                "ustedes": "án",
            }
        }
    }
    
    ending = verb[-2:]  
    
    if tense == "futuro":
        return verb + conjugations[ending][tense][subject]
    else:
        return verb[:-2] + conjugations[ending][tense][subject]

# Combine two names to create a couple name
def couplenames(first, second):
    first_vowels = [i for i in range(len(first)) if first[i] in "aeiou"]
    first_end = first_vowels[0]
    vowel_groups = []
    
    if len(first_vowels) > 1:
        sublist = [first_vowels[0]]
        previous = first_vowels[0]
        
        for i in range(1, len(first_vowels)):
            current = first_vowels[i]
            if current - previous == 1:
                sublist.append(current)
            else:
                vowel_groups.append(sublist)
                sublist = [current]
            previous = current
        if sublist:
            vowel_groups.append(sublist)
        
    if len(vowel_groups) == 1:
        first_end = vowel_groups[0][0]
    elif len(vowel_groups) > 1:
        first_end = vowel_groups[-2][0]

    for i in range(len(second)):
        if second[i] in "aeiou":
            second_start = i
            break
    
    return first[:first_end] + second[second_start:]

    