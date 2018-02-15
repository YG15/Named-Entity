# Name Entity Tagger
**Summary:** The script offers multiple tools to tag different types of name entities in a text, including complex case of mediocre performance of speeac-to-text algorithm.

__Script Details_:_
- Name :        NER_Tagger (Name Entity Recognition Tagger)
- Target:      Entity identification in text (including non-regular cases) and and tagging (in one of the following tags):
 {PERSON}- A first or last name (sometimes also an affix)
 {CARDINAL} - Quantity/Number
 {ORG} - Organization
 {LOCATION} - location
 {DATE} - Date
 {UNIDENTIFIED_NAME} - A name- Usually last name that wasn't identified by the list
 {TIME} - Time
 {PHONE} - Phone number
 {MAIL} - E-mail
 {FAC} - Facility
 {MONEY} - Money
- Arguments :   
    1. A plain text
    2. A name list
- Returning :   A tagged text
- Author :      Yonathan Guttel yesguttel@gmail.com
- Date :        08.02.2018
- Version :     1.0.2
 
### Description

The "NER_tagger" scripts came to offer an editional tagging and identification tools for text tagging which aren't offer by currrent libraries, putting the emphasis on taging speech-to-text output and contact details (phone and mail) identification.

***
The code contain the following functiond:

1. `phone_tagger` - Tags phone numbers in different formats, recieves a text and a parameter "TH_MIN_NUMBER_LENGTH" which is the minimum length of a  phone number and return a tagged text
2. `mail_tagger` - Tags e-mails numbers in different formats, recieves a text, return a tagged text.
3. `spacy_entity_extractor` - Name entity tagger using SpaCy package. recieves a text, return a tagged text.
4. `nltk_entity_extractor` - Name entity tagger using nltk package. recieves a text, return a tagged text.
5. `person_names_list_entity_extractor` - Name entity tagger using an external name list. recieves a text and a name list, return a tagged text.
6. `list_entity_exclude_include` - Name entity tagger using an external name list tha tag the any words appearing in the list, or tag all Out Of Vocabulary words (words which do not appear in a list). recieves a text, a name list, a boolean prameter "exclude=True" and a tag type; "entity".  return a tagged text.
7. `remove_repeated_ent` - Remove double tagging (in cast multiple NET are used). recieves a tagged text, return a tagged text.
8. `correct_point_tag_order` - Reorder a tag that came after a "." or "," so it will appear before it. recieves a tagged text, return a tagged text.
9. `multi_NER_tagger` - Combinning all above functions. recieves a  text, return a edited tagged text.

Than the main  script is run for the test:
1. Upload the data.
2. Run the `multi_NER_tagger`

### notice

The repo contain also a unittest file for testing the function abovementioned
