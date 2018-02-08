# coding: utf-8
"""
#improvements:
1. add to the list extractor an opposite function- to add "{OOV}" tag to words not in list-V
2. New function (correct_point_tag_order) that in cases that if there is a "." or "," before the tag
   - it replace the order so they will come after the tag-V
3. enable he identification of a phone number even if it arrives at the end of the text-  V
4. Corrected tagging in mail in words - tag only at the end (and not after each word) -V
5. I wrote unittest for all the functions [except nltk tagger and spacy tagger]- several cases for each -VX
6. comments correction- V
"""

###################################################
# Name: NER_Tagger (Name Entity Recognition Tagger)
# Target: entity identification of text, including non-regular cases
#         each entity is tagged in one of the following tags:
#         {PERSON}- A first or last name (sometimes also an affix)
#         {GPE}- A geographical political entity
#         {CARDINAL} - Quantity/Number
#         {ORG} - Organization
#         {LOCATION} - location
#         {DATE} - Date
#         {UNIDENTIFIED_NAME} - A name- Usually last name that wasn't identified by the list
#         {TIME} - Time
#         {PHONE} - Phone number
#         {MAIL} - E-mail
#         {FAC} - Facility
#         {MONEY} - Money
# Receives : a Plain text, a name list
# Return : A tagged text
# Author: Yonathan Guttel <yesguttel@gmail.com>
# Last Edited: 08.02.2018
# Version: 1.0.2
###################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Imports ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###Package imports
import nltk
import re
import string
import spacy
import pandas as pd
import os


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Function Who tags phone numbers in different formats, assuming phone number
# are cases in where more than five digits come without chrachter between them
def phone_tagger(text, TH_MIN_NUMBER_LENGTH=7 ):
    digits_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", ",", "_", "zero",
                   "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "o"]
    split_text = text.split()
    new_text = []
    digit_count = 0
    text_count = 0
    text_len=len(split_text)
    for i in range(text_len):
        if split_text[i].lower() in digits_list or split_text[i][:-1].lower() in digits_list:
            new_text.append(split_text[i])
            text_count +=1
            digit_count += 1
            if text_count== text_len:
                new_text.append("{PHONE}")
            elif split_text[i+1] not in digits_list and digit_count > TH_MIN_NUMBER_LENGTH:
                new_text.append("{PHONE}")
        elif bool(re.match(r"([\W*\d*])", split_text[i])) and len(split_text[i]) > TH_MIN_NUMBER_LENGTH:
            new_text.append(split_text[i])
            new_text.append("{PHONE}")
            text_count += 1
            digit_count = 0
        else :
            new_text.append(split_text[i])
            text_count += 1
            digit_count = 0
    returned_text = "".join(
        [" " + i if not i.startswith("'") and i not in string.punctuation else i for i in new_text]).strip()
    return (returned_text)


# Function Who tags e-mails numbers in different formats

def mail_tagger(text):
    # email_words =["at","@","dot","com",".com","gmail","hotmail", "email", "e-mail", "mail","electronic mail"]
    text_split = text.split()
    new_text = []
    sub_mail_1 =[]

    # identify format "bla at bla dot bla dot bla"
    if bool(re.findall(r"(\S*\s?at\s*\S*\s*dot\s*\S*\s?dot?\s?\S*)", text)):
        sub_mail_1 = re.findall(r"(\S*\s?at\s*\S*\s*dot\s*\S*\s?dot?\s?\S*)", text)
        ind1=1
        for sub in sub_mail_1:
            words_list=sub.split()
            ind1 = text_split.index(words_list[-1], ind1)
            text_split.insert(ind1 + 1, "{MAIL}")

    # identify format "bla at bla dot bla"
    if bool(re.findall(r"(\S*\s?at\s*\S*\s*dot\s\S*)", text)):
        sub_mail_2 = re.findall(r"(\S*\s?at\s*\S*\s*dot\s\S*)", text)
        ind1=1
        for sub in sub_mail_2:
            words_list=sub.split()
            ind1 = text_split.index(words_list[-1], ind1)
            if sub not in ''.join(sub_mail_1):
                text_split.insert(ind1 + 1, "{MAIL}")

    # identify format "XXXXXXXX@XXXXXX.XXX"
    for word in text_split:
        if bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", word)):
            new_text.append(word)
            new_text.append("{MAIL}")
        else:
            new_text.append(word)

    returned_text = "".join(
        [" " + i if not i.startswith("'") and i not in string.punctuation else i for i in new_text]).strip()
    return (returned_text)

# Name entity tagger using SpaCy package
def spacy_entity_extractor(text):
    nlp = spacy.load('en')
    doc = nlp(text)
    new_doc = text
    add = 0
    # Iterate over the text list and add entity when there is
    for ent in doc.ents:
        new_doc = new_doc[:ent.end_char + add] + ' {' + str(ent.label_) + '} ' + new_doc[ent.end_char + add:]
        add = add + (len(ent.label_)) + 4
    return (new_doc)


# Name entity tagger using nltk package
def nltk_entity_extractor(text):
    # find part of speech and entities in text
    namedEnt = nltk.ne_chunk(nltk.pos_tag(text.split()))

    # create a dictionary to set the names of the tags
    replacement_dic = {'PERSON': "{PERSON}", 'GPE': '{GPE}', 'ORGANIZATION': '{ORG}', 'FACILITY': {'FAC'}}

    # create a list to store the edited text
    edited_data_list = []
    # iterate over the the text and tag it accordingly
    for i in range(len(namedEnt)):
        if type(namedEnt[i][0]) == type('str'):
            edited_data_list.append(namedEnt[i][0])
            #if namedEnt[i][1] == 'NNP':
            #   edited_data_list.append('{UNIDENTIFIED_NAME}')
        else:
            for j in range(len(namedEnt[i])):
                edited_data_list.append(namedEnt[i][j][0])
                edited_data_list.append(replacement_dic[namedEnt[i].label()])

    # Join the list back to text
    edited_data = "".join(
        [" " + str(i) if not str(i).startswith("'") and str(i) not in string.punctuation else str(i) for i in
         edited_data_list]).strip()
    return (edited_data)


# Name entity tagger using an external name list
def person_names_list_entity_extractor(text):
    names_df = pd.read_csv("names_list.csv")
    names_list = names_df["Name"]
    return list_entity_exclude_include(text, names_list, exclude=True ,entity='{PERSON}')


# Name entity tagger using an external name list tha tag the words appearing in the list,
# or tag all Out Of Vocabulary words (words which do not appear in a list)
def list_entity_exclude_include(text, words_list, exclude=True ,entity='{PERSON}'):
    split_text = text.split()
    new_text = []
    if exclude==True:
        # iterate over the the text and tag it accordingly
        for word in split_text:
            new_text.append(word)
            name = "".join(re.findall(r'[a-zA-z]', word))
            if name in list(words_list):
                new_text.append(entity)
    else:
        for word in split_text:
            new_text.append(word)
            name = "".join(re.findall(r'[a-zA-z]', word))
            if name not in list(words_list):
                new_text.append("{OOV}")
    returned_text = "".join(
        [" " + i if not i.startswith("'") and i not in string.punctuation else i for i in new_text]).strip()
    return returned_text


# A function to remove double tagging (in cast multiple NET are used)
def remove_repeated_ent(text):
    tag_list =["{PERSON}","{GPE}","{CARDINAL}" ,"{ORG}","{LOCATION}","{DATE}",
               "{UNIDENTIFIED_NAME}" , "{TIME}","{PHONE}","{MAIL}","{FAC}","{MONEY}"]
    split_text = text.split()
    dec = 0
    for i in range(len(split_text) - 1):
        if split_text[i + 1 - dec] in tag_list:
            if split_text[i - dec].startswith("{"):
                del split_text[i + 1 - dec]
                dec += 1
            elif split_text[i - dec] == '),':
                del split_text[i + 1 - dec]
                dec += 1
    returned_text = "".join(
        [" " + i if not i.startswith("'") and i not in string.punctuation else i for i in split_text]).strip()
    return returned_text

# A function that reorder a tag that came after a "." or "," so it will appear before it
def correct_point_tag_order (text):
    split_text = text.split()
    for i in range(len(split_text) - 1):
        if split_text[i][-1]=="." and split_text[i + 1].startswith("{"):
            split_text[i]=split_text[i][:-1]
            split_text[i+1] = str(split_text[i+1]+".")
        if split_text[i][-1]=="," and split_text[i + 1].startswith("{"):
            split_text[i]=split_text[i][:-1]
            split_text[i+1] = str(split_text[i+1]+",")
    returned_text = "".join(
        [" " + i if not i.startswith("'") and i not in string.punctuation else i for i in split_text]).strip()
    return returned_text

# Combinning all above functions
def multi_NER_tagger(text):
    steps = [
        spacy_entity_extractor,
        phone_tagger,
        mail_tagger,
        nltk_entity_extractor,
        person_names_list_entity_extractor,
        remove_repeated_ent,
        correct_point_tag_order
    ]
    for step in steps:
        text = step(text)
    return text


if __name__ == "__main__":
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Setting ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # set path
    path = 'F:\Guttel\Desktop'

    # Paste or upload text
    text = u"""yesterday I've met Dave and Carly, we went to the cinema at 5 o'clock
    to watch the new movie of Mel Gibson, I didn't like it, but we thought that the main
    actor Tim, was preforming great. An hour later we went to drink coffee at Starbucks
    which was super expensive 10$ for a normal cappuccino! I also paid five dollars for a cookie.
    I think that such think could never happen in Jerusalem or in Switzerland.
    Dave ask me to give you his details:  Dave Matthews, 02-5702338, at work it is zero
    five two five five three eight seven. His mail address is dave@gmail.com and at the university is:
    dmat at Stanford dot ac dot com. He will stay in the US for four months in 2018 and then will
    get back to England where his wife Katy, leaves. They have a beautiful house in London which cost
    them 1 and a half million pounds. Send my regard to Monika and tell her to salute Mike Gonzales
    in my behalf. Lots of love Debbi. P.s. call my back on 3.12.18 on the mail dcohen@hotmail.au
    or in my work: ddebbie at embassyus dot com or on my phone 0549994893"""

    names_df = pd.read_csv("names_list.csv")
    names_list = names_df["Name"]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Run ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    print(multi_NER_tagger(text))

    # To examine each apart separately

    if False:
        text = spacy_entity_extractor(text)
        text = phone_tagger(text)
        text = mail_tagger(text)
        text = nltk_entity_extractor(text)
        text = list_entity_exclude_include(text, names_list, exclude=True ,entity='{PERSON}')
        text = remove_repeated_ent(text)
        text = correct_point_tag_order(text)

        print(text)