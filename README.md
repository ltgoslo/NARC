# NARC: Norwegian Anaphora Resolution Corpus

The Norwegian Anaphora Resolution Corpus (NARC) is the first publicly available corpus annotated with anaphoric relations between noun phrases for Norwegian.
The annotation effort enriches the existing annotation of the Norwegian Dependency Treebank (NDT).
The accompanying [paper](NARC_CRAC.pdf) by Mæhlum et al. at CRAC 2022 describes the (1st release of the) data in more detail.

___
<img width="907" alt="image" src="https://user-images.githubusercontent.com/5024871/171003897-1aac6483-0e95-4f38-94c2-13ae1a567d0c.png">
___

## Data sources

The underlying data for the annotation effort is the Norwegian Dependency Treebank (NDT), a richly annotated dataset. 
The original treebank contains  manually  annotated  syntactic and morphological information for both varieties of written Norwegian -- Bokmål and Nynorsk -- comprising roughly 300,000 tokens of each and a total of around 600,000 tokens. The corpus contains a majority of news texts (comprising around 85\% of the corpus), but also other types of texts, such as government reports, parliamentary transcripts and blog data.

## Annotation

Annotation was performed using the Brat annotation tool. 
Six students with a background in NLP and linguistics annotated the Norwegian Bokmål part of the corpus. The students received financial remuneration for their annotation work. All annotators completed an initial training round where they were tasked with annotation of the same set of documents, followed by a round of discussion and consolidation, along with updates to the annotation guidelines.

### Annotation guidelines

The annotation guidelines were developed during an initial pilot phase, where the documents used for training of the annotators were annotated by two of the project PIs. The guidelines were based largely on the guidelines from Ontonotes and the previous Norwegian BREDT dataset and were continuously refined following discussions and inputs from the annotators.
The full set of annotation guidelines can be found [here](guidelines/README.md).

### Pre-annotation

In order to alleviate the annotators' job of locating potential  mentions for coreference, we make use of the existing syntactic annotation of the treebank to perform a pre-annotation step. Using the dependency syntax, we extract all nominal heads that are either 
+ nouns (both common and proper nouns), 
+  referential personal pronouns,  
+  possessive pronouns,
+  adjectives in a nominal syntactic function (subject, object or prepositional complement).

### NARC relations

Three relations are annotated in NARC: coreference, bridging and split-antecedent. These are described further in the companion [paper](NARC_CRAC.pdf) and in the [annotation guidelines](guidelines/README.md)

## Distribution format

## License

The license follows that of the underlying Norwegian Dependency Treebank and is Creative Commons (CC)
Licence Name: Creative_Commons-ZERO (CC-ZERO). 

### Non Standard Conditions Of Use: 
* NORED * No redistribution * The original third-party contents are not included in this CC-0 license, and these individual works may not be republished as stand-alone texts.

## Obtaining the data
```
git clone https://github.com/ltgoslo/NARC
```

## Citing

If you publish work that uses or references the data, please cite our [CRAC article](NARC_CRAC.pdf). BibEntry: 

```
@InProceedings{MaeHauJor,
  author = {Petter M{\ae}hlum, Dag Haug, Tollef J{\o}rgensen, Andre K{\aa}sen, Anders N{\o}klestad, 
  Egil R{\o}nningstad, Per Erik Solberg, Erik Velldal, and Lilja {\O}vrelid},
  title = {NARC -- Norwegian Anaphora Resolution Corpus},
  booktitle = {Proceedings of Fifth Workshop on Computational Models of Reference, Anaphora and Coreference (CRAC 2022)},
  year = {2022},
  address = {Gyeongju, Republic of Korea},
}
```
