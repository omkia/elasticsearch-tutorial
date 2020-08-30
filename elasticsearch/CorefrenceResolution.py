#corefrence resolution using stanford core nlp
import csv

from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost:9000')


def resolve(corenlp_output):
    """ Transfer the word form of the antecedent to its associated pronominal anaphor(s) """
    for coref in corenlp_output['corefs']:
        mentions = corenlp_output['corefs'][coref]
        antecedent = mentions[0]  # the antecedent is the first mention in the coreference chain
        for j in range(1, len(mentions)):
            mention = mentions[j]
            if mention['type'] == 'PRONOMINAL':
                # get the attributes of the target mention in the corresponding sentence
                target_sentence = mention['sentNum']
                target_token = mention['startIndex'] - 1
                # transfer the antecedent's word form to the appropriate token in the sentence
                corenlp_output['sentences'][target_sentence - 1]['tokens'][target_token]['word'] = antecedent['text']


def print_resolved(corenlp_output):
    """ Print the "resolved" output """
    possessives = ['hers', 'his', 'their', 'theirs']
    for sentence in corenlp_output['sentences']:
        for token in sentence['tokens']:
            output_word = token['word']
            # check lemmas as well as tags for possessive pronouns in case of tagging errors
            if token['lemma'] in possessives or token['pos'] == 'PRP$':
                output_word += "'s"  # add the possessive morpheme
            output_word += token['after']
            print(output_word, end='')

with open("E:\\data.csv", encoding='utf-8') as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\x1b")
    i=0
    turn=0
    text=""
    for line in tsvreader:
        doc = {}
        i = i + 1

        if(line[0]=='' or i==1 ):
            continue
        text=(line[2])
        text=text.replace("\'","")
        print(text)
        if("Number:" in line[0] ):
            print("turn " + turn)
            output = nlp.annotate(text,
                                  properties={'annotators': 'dcoref', 'outputFormat': 'json', 'ner.useSUTime': 'false'})

            resolve(output)
            print('Original:', text)
            print('Resolved: ', end='')
            print_resolved(output)
            text=""
            turn=line[0].split(" ")[1]
