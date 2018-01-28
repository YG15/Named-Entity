###################################################
# Name: entity identification
# Target: entity identification of text, including non-regular cases
# Author: Yonathan Guttel
# Last Edited: 23.01.2018
# Version: 2
###################################################
###Package imports
import nltk
import re


#change to stanford NER

data ="""A chinese man, Lau Xing (Jackie Chan), robbed and try to escape from the Bank of England. To escape from the police, he observes from a window, two police officers searching for him asking an Oriental man in the street for his identification, and says "Passport...too", he becomes, under the name "Passepartout" (pronounced Pass-par-too), a valet to Phileas Fogg (Steve Coogan), a scientist trying to break the 50-mph speed barrier. After succeeding to do so, and managing to avoid the police, they head to the Royal Academy of Science. Here, Fogg is insulted by other 'brilliant minds', in particular the bombastic Lord Kelvin (Jim Broadbent), who believes that everything worth discovering has already been discovered and there is no need for further progress. The bank robbery is also discussed. In his blind rage, Fogg says that he's glad the bank was robbed because it is outdated and says that the thief could be in China in little over a month, which interests Lau Xing. Fogg places a bet to see if it would be possible (as his calculations said) to travel around the world in 80 days. If he won, he would become Minister of Science in Lord Kelvin's place; if not, he would tear down his lab and never invent anything again.
Passepartout and Phileas retreat to Phileas's home, where he mourns on his rash decision; yet Passepartout said that to bet on something he believed in made the bet in no way foolish. Without losing a moment, they take a carriage and leave London, after crossing with Inspector Fix (Ewen Bremner), a corrupt officer who was hired to stop them from travelling around the world.
They then travel to Paris, where Passepartout must evade minions sent by the murderous female soldier General Fang, out after what he stole: the Jade Buddha, which is a sign of good fortune. She had given the Buddha to Lord Kelvin in exchange for military assistance in her enterprises to conquer Lau Xing's village. Pretending to take Phileas to a convention with Thomas Edison, Passepartout leads him instead to an Art School, where Phileas meets Monique (Cécile de France), a would-be impressionist. Realizing how busy his boss is, Passepartout fights the minions using every material available: canvas, brushes, buckets of paint, etc. Meanwhile, Phileas and Monique discuss Monique's paintings of 'impossible things', such as dogs playing poker. Moments later, Phileas sees a painting of a man with wings. To make a machine that could allow men to fly was always Phileas's dream; he therefore feels touched. All of a sudden, Passepartout returns and tells his boss that they are late. The two men, accompanied by Monique, depart in a hot-air balloon.
They then travel to Turkey, where they are greeted by Prince Hapi (Arnold Schwarzenegger). Here, they were entertained for some hours in a swimming pool. The Prince, having become infatuated with Monique and ordered her to stay as his seventh wife (one for each day of the week) while the men were ordered to leave. The men leave, but blackmail Prince Hapi into releasing Monique, using a prized but apparently flimsy statue of the Prince as a bargaining counter. The statue is a parody of Rodin's The Thinker made to look like the Prince. The statue is ultimately destroyed, though the three travelers escape.
Lord Kelvin, hearing of all this and of the theft of the Jade Buddha, becomes angry; he is later contemptuous when he learns that Fogg has been involuntarily abetting a thief's escape. Using this as an excuse to delay Phileas, he and his aides order the British colonial authorities in India to arrest both men.
In India, Passepartout sees notice of the price on his head and warns his companions. Disguised as local women, they evade the police, but are attacked by General Fang's agents. Using Inspector Fix and a sextant as weapons, Phileas and Passepartout defeat their assailants and flee to China.
Guided by knowledge of China, Passepartout leads his friends to a village, where they are happily greeted. They spend several days here, during which Phileas discovers that Passepartout is in fact Lau Xing, a local warrior, and that the repeated attacks by General Fang's militia, the Black Scorpions, are part of a power struggle centred around the Jade Buddha. Phileas is disappointed by this, and more so by the revelation that Monique has known the truth for many weeks.
Later, the village is attacked by the Black Scorpions. Phileas, Monique and Lau Xing are held captive. In the next morning, Lau Xing challenges the arrogant young leader of the group that has seized him to a fight. Lau Xing at first fights alone, and is defeated; moments later, he is joined by the members of the "Ten Tigers" fraternity[disambiguation needed], of whom he is one. The Tigers, though outnumbered, drive the Black Scorpions from their village and free the Westerners. The Jade Buddha is reinstated in the village's temple.
Phileas now desires to continue alone, having been disappointed by his companions. He travels to San Francisco, where he is tricked out of his money. He attempts to replenish his supply with the aid of a beggar (Rob Schneider), but fails. He is recognized by Lau Xing and Monique, who have come to find him.
It was in the desert that they found the Wright brothers (brothers Owen and Luke Wilson), and the 3 inventors discussed the flying machine. Taking a look at the plans (which Wilbur Wright claimed to be his silly brother's doing), Phileas found them brilliant and suggested a few mere changes (Wilbur says he was proud of his brother and had always believed in him).
Lau Xing (still called Passepartout because of force of habit on the other people's part), Monique and Phileas' next stop was New York, where a massive crowd who had placed bets for or against Phileas winning, greeted them and made it impossible for them to pass and reach their ship. A policeman allowed this to be possible, by taking them through a building he called a shortcut. Here more minions awaited them, ready for one last face-off. They made arrangements with Lord Kelvin to take Lau Xing's village and tap the jade reserves underneath it, but if Phileas wins the bet, Lord Kelvin will not have the means to help them.
A major battle between the three friends and General Fang and her minions started in the workshop where the statue of liberty was made, with Lau Xing using his skill to stop his enemies and the other two using luck. In the end the three friends were victorious, or so it seemed, as the minions had stalled them enough to make them lose their ship to England. Though Phileas could have gotten to the boat, he decides to miss it to help Lau Xing.
Phileas felt like he had lost, but the other two said they might still make it if they caught the next ship. Phileas knew the unlikelihood of this yet chose to carry on. The old ship was owned by a sailor who had lost both his nipples in an attack by a shark. Phileas told the captain they weren't going fast enough, and after a lot of talking, he managed to convince the captain to let him build a plane out of the old wood from the ship, in exchange for a new ship and a surgery to give him new nipples.
The building started and soon was over. Using the changed Wright brother's plans, Phileas built a machine that seemed to work. On it was Lau Xing (pedalling), Phileas (driving), and Monique (commenting). The machine was working fine and soon they reached London. Then, the machine began to fall apart and they had a crash-landing in front of the RAS. Lord Kelvin sends police to stop them from making it to their actual destination, the top step of the Royal Academy of Science, and the clock soon strikes noon, which is the time Phileas started.
Lord Kelvin proclaims himself the victor. Several people, such as Monique, Fix, and other ministers, begin attesting to Kelvin's unfair methods and his bullying nature, but Kelvin scoffs at them. However, in the process he insults the Queen Victoria (Kathy Bates), who is nearby listening. She had found out he had sold her arsenal to Fang thanks to one of his aides. Kelvin tries to run away but is apprehended.
Phileas is also lucky enough not to have lost the bet; he is one day early thanks to crossing the international date line, yet believed himself late because of an error on the part of Lau Xing. He ascends the stairs of the Academy and, there, embraces Monique, victorious in his bet."""


#data =" I met Jamie at Bangladesh on the 4th July 1960, He came from London with Jade who is Matthew Perry's uncle. We went to Disneyworld and ate the ice cream, he told me that two days ago he met Arik, which is Scandinavian who works at the United Nations, He works there for more than two years, and will be there until 2020. He will earn 200 dollars for a work day and 456 NIS for every trip to Israel, but this will happen only next week."

def entity_extractor(data):
    try:
        namedEnt = nltk.ne_chunk(nltk.pos_tag(data.split()))

        search_list = ['ORGANIZATION', 'PERSON', 'GPE', 'FACILITY', 'GSP', 'LOCATION']
        search_dic={}
        for search in search_list:
            choice_list = []
            for i in range(len(namedEnt)):
                if search in str(namedEnt[i]):
                    choice_list.append(' '.join([item[0] for item in list(namedEnt[i])]))
            search_dic[search]=choice_list
        return( search_dic)

    except (Exception):
        print('failed in the main try of processor')
        print(str(Exception))

search_dic = entity_extractor(data)

search_list = ['ORGANIZATION', 'PERSON', 'GPE', 'FACILITY', 'GSP', 'LOCATION']
for search in search_list:
    print(search)
    print(search_dic[search])




############################################################
"""
import ner
import os
from nltk.tag.stanford import CoreNLPNERTagger
from nltk.tokenize import word_tokenize
#from nltk.tag.stanford import CoreNLPPOSTagger
#st= CoreNLPNERTagger(model, jar)

os.environ['CLASSPATH'] = 'F:/Guttel/Desktop/Gong/Entity identifications/tanford-ner-2017-06-09/stanford-ner.jar'
os.environ['STANFORD_MODELS'] = 'F:/Guttel/Desktop/Gong/Entity identification/stanford-ner-2017-06-09/classifiers'

model = 'F:\Guttel\Desktop\Gong\Entity identification\stanford-ner-2017-06-09\classifiers\english.muc.7class.distsim.crf.ser.gz'
jar = 'F:\Guttel\Desktop\Gong\Entity identification\stanford-ner-2017-06-09\stanford-ner.jar'

st= CoreNLPNERTagger(r'F:\Guttel\Desktop\Gong\Entity identification\stanford-ner-2017-06-09\classifiers\english.muc.7class.distsim.crf.ser.gz')

clasEsified_text = st.tag(word_tokenize(data))

from spacy.lang.en import EnglishDefaults
nlp = EnglishDefaults()
doc = nlp('Apple is looking at buying U.K. startup for $1 billion')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

tokens = nlp(u'Mr. Best flew to New York on Saturday morning.')
ents = list(tokens.ents)
assert ents[0].label == 346
assert ents[0].label_ == 'PERSON'
assert ents[0].text == 'Mr. Best'



####################################################

from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r"F:\Guttel\Desktop\Gong\Entity identification\stanford-english-corenlp-2017-06-09-models")
nlp = StanfordCoreNLP(r'//stanford-english-corenlp-2017-06-09-models/')

sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
print 'Tokenize:', nlp.word_tokenize(sentence)
print 'Part of Speech:', nlp.pos_tag(sentence)
print 'Named Entities:', nlp.ner(sentence)
print 'Constituency Parsing:', nlp.parse(sentence)
print 'Dependency Parsing:', nlp.dependency_parse(sentence)

"""