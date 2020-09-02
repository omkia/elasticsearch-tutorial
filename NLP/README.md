# Definition of the coreference resolution
Coreference is defined as occurring when one or more expressions in a document refer to the entity that preceded it/them. Coreference accuracy, then, is the task of finding all expressions that correspond to any of the entities present in a given text. While this problem definition seems simple enough, the nomenclature in papers regarding reference solutions is often very confusing. Its visualization makes things a little easier to understand:

![](/NLP/imgs/nomenclature.png)

Words are colored according to whether or not they are entities. Different colored word groups are members of the same reference group. Entities that are the only member of their group are known as "single" entities.

# Why the Corefence decision is difficult

Entities can be very long, and base entities can occur very far from one another. The greedy system will calculate each possible range (sequence) of tokens and then compare them for every possible period that came before them. This complicates the problem with O (T <sup> 4 </sup>), where T is the length of the document. For a 100-word document, this would be 100 million possible options, and for the longest document in our dataset, that is roughly a quadrillion possible combinations.

If that does not make it tangible, imagine we have the sentence.

<p align="center"> 
  * Arya Stark walks her direwolf, Nymeria. *
</p>

Here we have three entities: ```Arya Stark```, ```her```, and ```Nymeria```. As a native speaker of English it should be trivial to tell that ```her``` refers to ```Arya Stark```. But to a machine with no knowledge, how should it know that ```Arya``` and ```Stark``` should be a single entity rather than two separate ones, that ```Nymeria``` does not refer back to ```her``` even though they are arguably related, or even that that ```Arya Stark walks her direwolf, Nymeria``` is not just one big entity in and of itself?

For another example, consider the sentence
<p align="center"> 
  * Napoleon and all of his marvelously dressed, incredibly well-trained, loyal troops marched all the way across the Europe to enter into Russia in an, ultimately unsuccessful, effort to conquer it for their country. *
</p>


The word ```their``` is referent to ```Napoleon and all of his marvelously dressed, incredibly well trained, loyal troops```; entities can span many, many tokens. Coreferent entities can also occur far away from one another.

# NER-Tagger
*NER-tagger* is a web tool that helps linguists to manually classify entities in text.
It has been specifically developed for the annotation of named entities, where the task of classifying appropriate nouns into a number of semantic types.
However, the tool can be easily customized for both annotation tasks.

## Features
* *NER-tagger* Allows multiple annotation projects to run simultaneously,
* Supports multiple users,
Comes with an administrative interface to monitor the annotation process.

## Use Cases
One might find *ner-tagger* useful for the following annotation tasks:

* **Identify the specific entity**, where the task is to classify the correct names into categories of interest.
* **Sentiment analysis** to illustrate the polarity of the adjectives.
