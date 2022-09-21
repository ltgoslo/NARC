
# Norwegian Anaphora Resolution Corpus: Guidelines

# Chapter 1: Introduction
In this annotation effort, we mark information regarding anaphoric and cataphoric expressions in the Norwegian Dependency TreeBank (NDT).
These guidelines are heavily influenced by the guidelines from the BREDT, Ontonotes and ARRAU corpora.. The guidelines are structured as follows. Chapter 2 introduced the basic terminology employed in this effort. Chapter 3 contains discussions of specific cases of anaphora and cataphora, and the treatment of these. Chapter 4 contains brief instructions about how to annotate these in the annotation tool Brat (Stenetorp et al, 2012). The project is financed by the National Library of Norway.

# Chapter 2: Introduction to terminology
The purpose of this section is to give an introduction to coreference and an overview of the kinds of phenomena we will be annotating in this corpus. It also introduces some useful terminology. We introduce the three relations we will mark: [coreference](#coreference), [split antecedent](#split-antecedent) and [bridging](#bridging). 

A very important goal of text, arguably the most important of all, is to make claims about things in the world, or in a fictional world in the case of fiction. As an example, the goal of this text is to make claims about nouns and pronouns. We use "things" in a very broad sense of the word, including very abstract “things” such as a thought or concepts such as happiness. In order to be able to make claims about things in the world, we must be able to use words to refer to those things. Words that typically serve this purpose are nominals: proper nouns, common nouns and pronouns, in addition to some determiners, including *begge* 'both' and *alle* 'all'. Moreover, we need to know which words refer to the same thing, i.e. which words **corefer**. Let us look at an example.

&nbsp;&nbsp;&nbsp;&nbsp;(1) I dag besøkte **Per<sub>1</sub>** et **bibliotek<sub>2</sub>**. På **biblioteket<sub>2</sub>** leste **han<sub>1</sub>** en **bok<sub>3</sub>**. Etterpå dro **Per<sub>1</sub>** ut og handlet.

I have highlighted most of the nouns and added reference markers. Every word marked with 1 refers to the person named *Per*, and words marked with 2 refer to the library he visits. Notice that different devices are used to indicate **coreference**: The definite form *biblioteket* indicates that the library is already known. Similarly, *han* indicates that the person referred to has been mentioned previously. In this example it must be Per. However, we also have a third mention of Per in the text. In this instance, the name Per is repeated. Definite forms of nouns, pronouns such as *han*, *den* and *det* and repeating a name are three ways you can mark coreference. Notice, however, that you cannot usually repeat an indefinite noun and expect people to interpret it as coreferring with a previous instance of the same noun. If you continued the text above with a sentence containing *et bibliotek*, you would presumably interpret this as a different library.

### Coreference

Coreference is crucial to our understanding of texts. It is also the main focus of this annotation effort. Suppose we could not figure out which words referred to the same thing in the text above. Without this information, we would not be able to make any sense out of it. In isolation, each sentence would be understandable, but the connection between them would be lost. This scenario is hard to conceive of for humans, especially for easy texts like this one, because we are excellent at figuring out coreference. For computer systems aimed at understanding text, however, this scenario is often a reality. Systems can be good at interpreting individual sentences, but may have a hard time linking coreferring words in different sentences together. The task of interpreting coreference automatically is called **corereference parsing** or **coreference resolution**. Coreference parsers are trained on text corpora annotated with coreference relations such as the one we are making in this project.

### Potential for coreference

Returning to example (1) above, note that *bok* is marked with 3. There are no other words in the text referring to this book, so no other words are marked with 3. However, this word has the **potential** for coreference. In other words, the word can function as the **antecedent** of an anaphor. You could perfectly well add a sentence to this text with the definite form boka, and you would interpret it as coreferring with bok. On the other hand, *dag*, while being a noun, behaves differently. This word does not have a potential for coreference in the same way, as in this case it is part of a fixed adverbial expression. It is difficult to refer back to nouns such as *dag* "day" and *bords* "table (genitive)" in fixed expressions such as *i dag* "today" or *til bords* "to the table (in order to dine)". However, as it is difficult to draw a clear line between nouns that clearly have potential for coreference and those that do not, we mark all these nouns as markables. Many of these will remain as **singletons**, which are markables that have no relations to or from them after all relations have been drawn. In this corpus, we mark up all nouns, pronouns and determiners that have a potential for coreference, whether or not there are more than one word in the text with the same reference. Such words with a potential for coreference are called **markables** in this project. Markables also include words that can function as anaphors. When a markable is coreferent with another markable in the text, we add a relation between them. In the sentence below, all markables are marked with brackets:

&nbsp;&nbsp;&nbsp;&nbsp;[En hest] kom galopperende ned [en bakke]. [Bakken] var skrå og [hesten] var rask. [Hesten som stod ved [stallen]] ble glad.


In the rest of this chapter, we give a linguistic introduction to the phenomena that we will be annotating. First we will be looking at the two main forms of coreference: repetition and anaphora. We will then look at bridging, a special kind of anaphora which we will also annotate in this project.

### Coreference by repetition

Coreference by repetition is perhaps the most obvious form of coreference: You refer to the same thing by using the same word, e.g. the thing’s name, over and over. We saw this in (1) where the name Per was used twice. Note that the name can be slightly different in each instance, as in (2), or even entirely different, as in (3), where a synonym is used to refer to the same referent. This does not matter, as long as the names are coreferring:

&nbsp;&nbsp;&nbsp;&nbsp;(2) **Fremskrittspartiet**<sub>1</sub> hadde landsmøte i helga. På søndag kveld holdt **FrPs**<sub>1</sub> nye leder tale.\
&nbsp;&nbsp;&nbsp;&nbsp;(3) Tante Olga flytta til **USA**<sub>1</sub> i 1950. Hennes kusine Martha hadde allerede bodd i **Statene**<sub>1</sub> i 10 år på det tidspunktet.

Proper nouns are not the only words which can be used in this way. Every time a first person pronoun is used by the same speaker, it refers to the same individual, the speaker. Similarly, second person pronouns refer to the addressee every time they are used:

&nbsp;&nbsp;&nbsp;&nbsp;(4) **Jeg**<sub>1</sub> liker kake. Vafler liker **jeg**<sub>1</sub> også. Men rullekake er **min**<sub>1</sub> aller største favoritt.
&nbsp;&nbsp;&nbsp;&nbsp;(5) Hva heter **du**<sub>1</sub>? Hvor bor **du**<sub>1</sub>?\


Note that possessive determiners such as *min* "my" in (4) above share some of the same qualities as pronouns do. Other (non-possessive) determiners do not have the same qualities 
Also note that this means that pronouns such as "jeg" and "du" can corefer with proper nouns and common nouns.

&nbsp;&nbsp;&nbsp;&nbsp; **Kari]<sub>1</sub>** la **gaffelen** ned. "**Jeg<sub>1</sub>** er ikke sulten," sa **hun<sub>1</sub>**. 

## Anaphora
An anaphoric expression has as part of its meaning that it needs to be coreferent with an expression in the context. The most obvious example of this is pronouns like han/hun/den/det/hans etc. If you use one of those pronouns out of context, you will usually not be understood. (6) does not make sense unless uttered after a previous mention of a male person, as in (7):

&nbsp;&nbsp;&nbsp;&nbsp;(6) Han<sub>?</sub> er snill!\
&nbsp;&nbsp;&nbsp;&nbsp;(7) Jeg snakker ofte med Gunnar<sub>1</sub>. **Han**<sub>1</sub> er snill!

A subclass of anaphoric pronouns is reflexive pronouns such as seg (selv) and sin. These usually refer to the closest subject:

&nbsp;&nbsp;&nbsp;&nbsp;(8) **Kari**<sub>1</sub> vasker **seg**<sub>1</sub>.
&nbsp;&nbsp;&nbsp;&nbsp;(9) **Anna**<sub>1</sub> liker hunden **sin**<sub>1</sub>.


Another kind of anaphoric expressions is definite nouns such as mannen and definite noun phrases such as det røde flagget. 

&nbsp;&nbsp;&nbsp;&nbsp;(10) En dame og **en mann**<sub>1</sub> gikk langs veien. **Mannen**<sub>1</sub> hadde en stor frakk på seg.
&nbsp;&nbsp;&nbsp;&nbsp;(11) Under statsbesøket på Bø rådhus hang det **et kinesisk flagg**<sub>1</sub> over døra. **Det røde flagget**<sub>1</sub> var blitt kjøpt inn for anledningen. 

Although both pronouns and definite nouns may be anaphoric, a definite noun (phrase) is a quite different kind of animal from a pronoun: A pronoun contains very little content on its own, except perhaps gender and number. Nouns and noun phrases, on the other hand, may contain very specific content. Take *det røde flagget* as an example. The noun *flagget* denotes a particular kind of object, a flag, and *røde* specifies the color of that flag. Because definite nouns and noun phrases can express such specific concepts, they can pick antecedents in more subtle ways. In (11), the antecedent does not contain information about the color of the flag. Still, we can refer back to the antecedent with *det røde flagget*, since we know that the Chinese flag is red. Because of this, antecedents of definite nouns/noun phrases can be quite far away in the text. The relationship between the anaphor and the antecedent may also be in a more indirect relationship, called **bridging**, or the antecedent may be lacking altogether, which we call **accommodation**. Examples of accomodation include "solen",referring to the sun, even if it is not mentioned, or other common entities that are assumed to be known by both speaker and listener, such as "månen", "jorda", "himmelen" and "statsministeren".

## Cataphors
The same way we use the term *anaphor* for cases where a word that comes later in a text refers to a word that has appeared earlier, there are cases where the opposite happens. These are cases of **cataphors**, and their antecedent counterparts are called *postcedents*. Apart from their direction, they are largely the same. Cataphors are not as frequent, and we prioritize an anaphoric interpretation if possible. All that is written about anaphors in this document is relevant for cataphors unless otherwise stated. 

Example:

\[Hun\]<sub>1</sub> åpnet \[døra\]. \[Rommet\] var tomt. \[Kari\]<sub>1</sub> holdt pusten.
She opened the door. The room was empty. Kari held her breath.

We see here that the pronoun *hun* 'she' is used *before* the postcedent *Kari* is used. 

Note the way later anaphoric expressions refer to the cataphoric expression itself, even though it comes before its postcedent:

\[Hun\]<sub>1</sub> åpnet \[døra\]. \[Rommet\] var tomt. \[Kari\]<sub>1</sub> holdt pusten. \[Hun\]<sub>1</sub> var tidlig ute. 
She opened the door. The room was empty. Kari held her breath. She was early.

Here there is a cataphoric relation from Hun to Kari, and an *anaphoric* relation from Hun in the last sentence to Hun in the first sentence.

### Metonymy and the importance of identifying reference
In many cases the same word can refer to some related meaning. A common example is that of geopolitical entities such as city names or country names, which may refer to both their geographical location, their governments or political organization, or perhaps the inhabitants. However, metonymy is far from limited to this. Other examples include using an author's name to refer to their books, or the name of a school to refer to its leadership or student body, as opposed to its location. The important point in all these cases is to pay close attention to what the token or set of tokens actually refer to. Two different tokens, such as *Oslo* and *Norges hovedstad* might occur in a coreferential relationship if they both refer to the geographical location, but not if for example *Oslo* refers to the local government, while *Norges hovedstad* refers to its geografical location. A token's reference decides whether or not it should be part of a coreference relation with repetitions of the same token, which may or may not share the same reference, or with other tokens.

### Split antecedent
When multiple antecedents together contribute to a single anaphoric expression, we are dealing with the relation called split antecedent. Note that this relation is only used when all parts that contribute to a whole are mentioned. No part-of relations or subset/superset relations are allowed. In this regard, it is similar to coreference, and is the second most important aspect of this annotation effort. We have a basic case of split antecedent when two antecedents that are **not** coordinated occur before an expression that refers to both of them at the same time. Note that like for the other relations, this can also be cataphoric, with two postcedents, but there is not separate label.

&nbsp;&nbsp;&nbsp;&nbsp;**Kari**<sub>1</sub> spiser grøt. **Ola**<sub>2</sub> drikker saft. **De**<sub>1,2</sub>  koser seg.


In the above sentence, one split antecedent-arch is drawn for each markable that is involved in the relation. The rules for which direction the arch is drawn is the same as for the other relations, so in this case, one is drawn from"De" to "Kari" and one is drawn from "De" to "Ola".

However, we have decided to treat coordinated phrases as single markables. This decision is based on the existence of certain expression that modify whole coordinated phrases, and not just one of the elements. This means that an expression referring back to a coordinated expression should use the **coreference** relation, as long as the identity of the expressions are the same. 

&nbsp;&nbsp;&nbsp;&nbsp;**Kari og Ola**<sub>1</sub> gikk bortover veien. **De**<sub>1,2</sub> var sultne.

"Kari" and "Ola" can still be part of separate relations if it is relevant.

&nbsp;&nbsp;&nbsp;&nbsp; **Kari**<sub>1</sub> og **Ola**<sub>2</sub> satt og spiste. **Kari**<sub>1</sub> spiste kål. **Ola**<sub>2</sub> spiste potet.

### Bridging
Judging from what we have discussed so far, it could seem like anaphora is a special case of coference. This is, however, not the case. There are instances of anaphora where the anaphor and the antecedent do *not* corefer.  Instead, there is another relationship between the anaphor and the antecedent. Let us look at the first sentence in example (11) again:

&nbsp;&nbsp;&nbsp;&nbsp;(11) Under statsbesøket på **Bø rådhus**<sub>1</sub> hang det et kinesisk flagg over **døra**<sub>1</sub>.

When we read this example, we interpret the definite *døra* as the door of *Bø rådhus*. These two phrases are in an antecedent-anaphor relationship, but it is not a coreference relationship. Rather, it is a **part-whole** relationship, since the door is part of the building Bø rådhus. We call this kind of anaphora **bridging**. In bridging, the antecedent and the anaphor are in some other relationship than coreference. The particular relationship is inferred from the context. A part-whole relationship is a very common relationship, but it can also be, e.g., **possession**, as in the following example:

&nbsp;&nbsp;&nbsp;&nbsp;(12) En **ridder**<sub>1</sub> kom mot oss. **Sverdet**<sub>1</sub> blinket i sola.
&nbsp;&nbsp;&nbsp;&nbsp;(12) A knight came towards us. The sword blinked in the sun.

In this example, we easily infer that *sverdet* 'the sword' belongs to *en ridder* 'a knight', since stereotypical knights own and carry swords. Notice that another definite noun would, e.g. *speilet* 'the mirror', would be much harder to interpret:

&nbsp;&nbsp;&nbsp;&nbsp;(13) En ridder<sub>1</sub> kom mot oss. Speilet<sub>?</sub> blinket i sola.
&nbsp;&nbsp;&nbsp;&nbsp;(13) A knight came towards us. The mirror blinked in the sun.

It is not common knowledge that knights own mirrors, or are in any other relationship to mirrors, so it is hard to see what *speilet* could refer to.
Bridging is very common with definite nouns and noun phrases, but rather uncommon (although not entirely non-existent) with third person pronouns. The reason is that definite nouns/noun phrases have more descriptive content, and it is therefore easier to infer relationships between the anaphor and the antecedent. In this project, we use a special bridging relationship in cases like this to distinguish bridging from coreference. On the other hand, the restrictions on the antecedents of a bridging relation are the same as for the other relations. 

While many definite nouns and noun phrases are in an anaphoric relationship to an antecedent, it is also quite common to have a definite noun (phrase) without an antecedent, as in example (14):

&nbsp;&nbsp;&nbsp;&nbsp;(14) **Sola** skal skinne på mandag.

It is perfectly normal to say (14) out of the blue, even though *sola* has no antecedent. There is only one sun in our solar system and we know it very well, so we can perfectly well refer to it in the definite form without having talked about a sun previously. We call this phenomenon **accommodation**. If there is no antecedent in the previous text, we can accommodate one from what we know about the world and the situation at hand. Let us look at another example:

&nbsp;&nbsp;&nbsp;&nbsp;(15) På vei hjem fra jobb gikk Per forbi **rådhuset**. Der traff han en venn.

You can say (15) without an antecedent for rådhuset. Many towns have a town hall, so it is quite easy to infer, or accommodate, that there is one also in the town where Per is. There is no need to understand accommodation well in order to annotate in this project. But it is important to understand that there will be a lot of definite noun phrases which are neither in a coreference relationship or a bridging relationship with an antecedent.

To decide what to do when you encounter a definite noun (phrase), the following checklist may be useful.
-1) Is there a markable in the proceeding text with the same reference as this noun (phrase)? If so, add a **coreference**  relation between them.

-2) If the answer to 1. is no, is there a markable in the previous context that the current noun phrase is in some relationship with (e.g. part-whole or possession)? Can the presence of this antecedent explain why the definite form is used? If yes, add a **bridging** relation between them. To test whether the potential antecedent explains the use of the definite form, you can try to swap the definite noun phrase with some other noun phrase which is in a less obvious relationship to the potential antecedent, as we did in (13) above, and see if it feels odd or not. If it feels odd, as (13) did, there is likely a bridging relationship between the definite noun (phrase) and the potential antecedent. You can also imagine the text without the potential antecedent and ask yourself if the definite noun (phrase) would sound odd then. If it would, there is likely a bridging relationship.
If the answer to 2 is no, or if you are unsure if it is, do not add a relation.

Be aware that intuitions about bridging may vary between annotators, and there is not always one correct answer. It is highly likely and perfectly ok if the inter-annotator agreement is not as good for bridging as for other relations.    



### Prioritizing annotations

In some cases the annotators have to chose between several different possibilities when it comes to the relations discussed above, and whether a relation is anaphoric or cataphoric. In these cases we follow the following hierarchy: 1) Coreference 2) Split-antecedent 3)Bridging, meaning that whenever possible, a coreference relation is preferred. We also prefer an anaphoric interpretation over a cataphoric interpretation. 

## Chapter 3: Specific cases


#### Relative sentences and the word "som"
The word "som" by itself is a subjunction, and despite its earlier label relative pronoun, it is not marked as an anaphoric expression, but it can be part of antecedents. Relative sentences are always included in the markable span of the noun phrase they modify. This applies both to restrictive relative sentences and non-restrictive ones. Restrictive relative clauses are the ones that provide information that changes or specifies the reference of a noun phrase. Non-restrictive relative sentences are usually preceded by a comma. Thus, the two following sentences both have similar markable spans, despite the fact that in 16, the relative clause restricts the reference of *katten* 'the cat'. It is not the cat that is sitting on the floor, for example, but rather the cat that is sitting on the table. The relative clause in (17) on the other hand, is non-restrictive, but still marked the same way. 

&nbsp;&nbsp;&nbsp;&nbsp;(16)[Katten som sitter på [bordet]] malte.
&nbsp;&nbsp;&nbsp;&nbsp;(17)[Katten, som sitter på [bordet]], malte.

#### Markable boundaries
Markables do not exist at the sub-token level. Compound nouns, hyphenated or not, are not split up. Extra information that is often provided in parantheses behind a noun is part of the noun phrase and therefore also part of the markable.

&nbsp;&nbsp;&nbsp;&nbsp;[Kari (53)] liker å spille fotball.


#### Apposition
Apposition (nor. apposisjon) is when two adjacent noun phrases are next two each other, and one of them specify the other, either by renaming or by expanding on the definition. We separate between **loose** and **tight** apposition, as is done in BREDT. Lose appositions is typically separated by a comma, while tight apposition is not. Tight apposition typically comes before the noun phrase it specifies, and lose after, but this is not absolute. Lose and tight appositions are sometimes called predicative and anaphoric (BREDT). In this annotation effort, we do not mark appositions in a special way. Appositions are always included together with the noun phrase they specify as one, big markable. Examples of tight apposition include titles such as _statsminister_. In the case of lose appositions, the first comma is included, while the second is not.  

An example of a lose apposition:

&nbsp;&nbsp;&nbsp;&nbsp;\[John, A linguist\], is coming to dinner.


Some examples of tight apposition:

&nbsp;&nbsp;&nbsp;&nbsp;\[The linguist John\]
&nbsp;&nbsp;&nbsp;&nbsp;\[Statsminister Erna\]
&nbsp;&nbsp;&nbsp;&nbsp;\[Erna, statsministeren\]
&nbsp;&nbsp;&nbsp;&nbsp;\[Herr Ibsen\]



#### Nested markables
Nesting happens when a noun phrase is contained within a longer noun phrase. When identifying long markables, it is important to see if any noun phrases within the markable can themselves stand as markables. A test for this is whether it is possible for the different noun-phrases making up the larger markable to have a reference that is independent of the markable as a whole.

&nbsp;&nbsp;&nbsp;&nbsp;(1) \[Katten på bordet\] spiser \[fisk\].
&nbsp;&nbsp;&nbsp;&nbsp;(2) \[Katten på bordet til \[Lise\]\] spiser \[fisk\].

In the first example, Katten cannot refer to a cat that is not (sitting) on the table. Katten can therefore not be a markable by itself. However, "bordet" is its own markable. The definite form implies that the table has been talked about or is implicit from the context. "Katten på" does not restrain the reference of bordet.

Proper nouns are always considered to be atomic, they are not seen as nesting even if it is possible to identify smaller divisions within the names.

&nbsp;&nbsp;&nbsp;&nbsp;\[Drammen Bibliotek\] åpner klokka halv ni. \[Biblioteket\] har mange bøker. 

Here, Although it is possible to identify "Drammen" within the name, the whole entity is *one* name, and should be treated as such. These combinations have a flat structure in the tree bank. 


#### Nominal predicates
We assume that predicates are not anaphorically related to their subject, and therefore we do not add a relation between a subject and a nominal predicate, even if they refer to the same thing.  This implies that there is no relation between a subject and the subject predicate, or an object and its object predicate. This is especially common with copular verbs such as være (vere,vera) ,verte, bli, kalles (kallast). The relation between a subject and its predicate is predication, not anaphora, and thus we do not mark it even though they are the same referent. 

&nbsp;&nbsp;&nbsp;&nbsp;\[Jon\] er \[språkviter\].

&nbsp;&nbsp;&nbsp;&nbsp;\[Per\] blir \[den neste statsministeren\].

There are also other verbs that take nominal predicates, such as "anerkjenne" in the example below.

&nbsp;&nbsp;&nbsp;&nbsp;Vi anerkjente Per som den rettmessige statsministeren i Norge

In the cases mentioned above, only the subject or object should be linked, not the predicates.

&nbsp;&nbsp;&nbsp;&nbsp;\[Jon\]<sub>1</sub> er \[språkviter\]<sub>2</sub>. \[Han\]<sub>1</sub> tegner trær hver dag.

When drawing a  relation back to a referent that is in a predicate relation, the subject is the one that received the relation.


&nbsp;&nbsp;&nbsp;&nbsp;[Denne katten]<sub>1</sub> er [en liten rakker]. [Den]<sub>1</sub> drikker [melka [vår]].

Here we see that the subject is referred back to by the anaphoric expression "Den" (It) in the sentence above.


####  Temporal expressions
Temporal expressions can be linked as long as the anaphoric expression is nominal. The antecedent does not have to be nominal. Multi-date expressions are considered atomic, and are not nested. Words such as "da" are not nominal and are not marked in this effort.

&nbsp;&nbsp;&nbsp;&nbsp;Jeg hadde det veldig gøy i \[går\]<sub>1</sub>. \[Dagen\]<sub>1</sub> gikk veldig fort!
&nbsp;&nbsp;&nbsp;&nbsp;I had a great time yesterday. The day passed very quickly. 

Here,the noun "går" in the adverbial phrase "i går" is referred to by "dagen".


#### Pronouns and demonstratives
All pronouns and demonstratives are linked to their referents, even in quoted speech. Possessive pronouns are always linked to their antecedents if available. 

&nbsp;&nbsp;&nbsp;&nbsp;"\[Jeg\]<sub>1</sub> spiste all grøten" sa \[trollet\]<sub>1</sub>.

&nbsp;&nbsp;&nbsp;&nbsp;\[Kari\]<sub>1</sub> sitter ved \[bordet\]. Katten \[hennes\]<sub>1</sub> sitter i \[sofaen\].


#### Generic pronouns and expletives
Generic pronouns such as *man* and generic *en/ein* are not linked, generic *vi* is not linked to repeated occurrences of the same word. However, if a word like "seg" refers back to any generic word, then this is in fact marked.

&nbsp;&nbsp;&nbsp;&nbsp;**Man**<sub>1</sub> kan slå **seg**<sub>1</sub> i den bakken.
&nbsp;&nbsp;&nbsp;&nbsp;One might hit oneself in that hill.

The same is true for expletive pronouns such as *det* 'it', *der* 'there and *her* 'here'. Note that care must be given especially to "det" so that it is linked in cases where it is in fact referential. The same is true for *vi*. Ontonotes gives a useful tip for checking for expletiveness: if the word in question can be substituted with a noun phrase, it is a referential pronoun, otherwise it is an expletive. As these are already explicitly marked in NDT, they are not highlighted as markables, and the annotators need not worry about them.

&nbsp;&nbsp;&nbsp;&nbsp;Man kan ikke spise is hele dagen.

&nbsp;&nbsp;&nbsp;&nbsp;Det står et tre i hagen.

&nbsp;&nbsp;&nbsp;&nbsp;Hvis vi skal synge alle versene i nasjonalsangen vil det ta for lang tid. 

In these three examples, *man*, *det* and *vi* should not be linked to any other expressions. 



#### Indefinite nouns
A noun does not always have a clear reference. It is possible for a noun phrase to be generic. Generic means that it is used to refer to something in general, for example as in saying something about all instances of a noun in general. "Horses are good animals". A case of generic use is only linked to referring pronouns and definite markables of the same entity, *not* to other generic nominal mentions (Ontonotes). In other words: They can form identity relation chains with non-generic mentions (pronouns or definite nouns), but not to repetitions of the same word. They are therefore markables, but will often be singletons.

Indefinite plurals are always generic. The same goes for indefinite singular nouns. Note that definite nouns can also be considered general, and this can be seen in, for example, encyclopedic entries:

&nbsp;&nbsp;&nbsp;&nbsp;(1) Tigeren er det største kattedyret, men størrelsen varierer mye og en stor løve kan være større enn en liten tiger. (https://snl.no/tiger)

#### Subsets
A subset is a type of anaphor, but we do not mark it specifically with its own relation type. Since a subset can never have the exact same reference as its parent set, we cannot use a coreference-relation in this case. However, if there is no definite noun, we cannot have bridging, either. Because of this, many subsets are **not** marked in this annotation effort, as they are not in fact coreferential or anaphoric in nature. A similar case is when the parent set is mentioned by use of a definite pronoun, as inthe sentence below. In these cases we do mark coreference. This applies to any case of a quantifying determinant + PP with a definite noun. In other words: subsets where the anaphoric expression is definite or a third person pronoun can potentially have a bridging relation.

&nbsp;&nbsp;&nbsp;&nbsp;\[Tjuefem elever\]<sub>1</sub> møtte opp. Vi møtte \[tre av \[elevene\]<sub>1</sub>\].

&nbsp;&nbsp;&nbsp;&nbsp; Vi møtte \[tre av \[elevene\]\]<sub>1</sub>. \[De\]<sub>1</sub> var glade for å snakke med oss. 

In the first example, the quantified phrase "tre av elevene" is a subset of "tjuefem elever", but is indefinite, and cannot refer back to its superset. However, the markable "elevene" inside it does refer, and should be related to, "tjuefem elever".

In the second example, "tre av elevene" is the antecedent of "de", and this is a normal coreference relation, as "de" refers to all three of the students. The nature of the antecedent does not affect the coreference relation in this case.

#### Agreement
Errors in agreement in number, case or gender is ignored if it is clear that two markables should be linked.

&nbsp;&nbsp;&nbsp;&nbsp;\[Skya\]<sub>1</sub> glir over \[himmelen\]. \[Han\]<sub>1</sub> er kritkvit.


#### Quantifying expressions
There are many different quantifying expressions. Quantifiers are words that express some quantity, or a set. (cite from ontonote). Examples are cardinal numbers (grunntall), partitives (noen, få, halv), measurements(et kilo, et glass, ei flaske) and collective nouns(en flokk, en sverm).  Some of these indicate subsets, which are discussed above.

Some examples are:
&nbsp;&nbsp;&nbsp;&nbsp;4) ei bøtte med vann
&nbsp;&nbsp;&nbsp;&nbsp;5) en del av legene
&nbsp;&nbsp;&nbsp;&nbsp;6) ei spiseskje sukker
&nbsp;&nbsp;&nbsp;&nbsp;7) en flokk geiter

A quantifying expression should **NOT** be co-referenced with the entitiy it modifies. Meaning, the quantifying expression in itself does not link with the phrase it modifies, like in the examples above. The span of the markable containing the quantifying expression should encompass the whole NP, with the quantifying expression and the modified NP. In addition, the modified NP is also a markable.  This larger span can be coreferenced with subsequent or antesequent markables. 

Like some cases of subsets, these large spans including quantifying expressions cannot be anaphors for neither bridging nor coreference, but they can be antecedents in a relation. The questions is then what the span of the markable for these expressions are.We do not treat them as nested PPs

#### Genitives
Nouns with the genitive s are marked as they are. Their non-genitive sub-token counterpart is not marked. The ambiguity of multi-token genitive phrases is reflected in the markable structure, as for *Kari og Olas datter* 'Kari and Ola's daughter'. 

&nbsp;&nbsp;&nbsp;&nbsp;[Kari] og [[Olas] datter] (the daughter is only Ola's)
or:
&nbsp;&nbsp;&nbsp;&nbsp;[[Kari] og [Olas] datter] (the daughter belongs to both Kari and Ola)


### Overlap between antecedent and anaphor.
In cases with coreferential chains, it is possible to have cases where anaphor and antecendent overlap, as in _a dog...the dog...it_, there it is the anaphor and _the dog_ is the antecendent in the last anaphoric expression, while _the dog_ is the anaphor and _a dog_ the antecendent in the first.

&nbsp;&nbsp;&nbsp;&nbsp;\[En hund\]<sub>1</sub> løper bortover \[gata\]<sub>2</sub>. \[Den\]<sub>1</sub> bjeffer mot \[et barn\]<sub>3</sub>. \[Barnet\]<sub>3</sub> er redd for \[den\]<sub>1</sub>.

Here , "Den" works both as an anaphor, referring back to the antecedent "En hund", and it is at the same time the antecedent of the object in the third sentence "den". 

&nbsp;&nbsp;&nbsp;&nbsp;"Jeg elsker denne forretten", utbrøt Kari. Hun tok en bit til før hun la fra seg gaffelen sin. Den tidligere kokken kjente alle smakene i retten. 

In this example, we first have a cataphoric relation from "Jeg" to Kari, the remaining relations are anaphoric, and all (including the first) are coreference relations. One from "Hun" to "Jeg", then from "sin" to "Hun", then from "Den tidligere kokken" to "sin". Assuming here, that we know that Kari and the former chef is the same person.



#### Definite reading of possessive determinative + indefinite noun
A possessive determinant may follow or precede the noun it modifies in Norwegian. If it follows a noun, the noun is always definite, while the noun is never in the definite form if it follows. We interpret these constructions as always having a definite reading, regardless of the declension of the noun. They are therefore open to an anaphoric reading. 


&nbsp;&nbsp;&nbsp;&nbsp;\[Vi\]<sub>1</sub> liker å besøke \[\[våre\]<sub>1</sub> naboland\].

&nbsp;&nbsp;&nbsp;&nbsp;\[Vi\]<sub>1</sub> liker å besøke \[nabolandene \[våre\]<sub>1</sub>\].
 

This is analoguous to similar possessive constructions with the genitive *s*. Therefore, these constructions are also seen as definite.

&nbsp;&nbsp;&nbsp;&nbsp;\[Journalisten\]<sub>1</sub> stilte \[et spørsmål\]<sub>2</sub>. \[De\] svarte ikke på \[\[journalistens\]<sub>1</sub> spørsmål\]<sub>2</sub>


#### Genitive constructions with "sin", "han" or "hennar"
In bokmål, the so-called *garpegenitiv* is quite common. It is recognized by the use of *sin/si/sitt/sine* directly after the possessor. In these cases, the determinants themselves do not pick up any reference from the context, and they are therefore not anaphoric. Note that this is *not* the case when they are used outside of the garpe-genitive construction. 

&nbsp;&nbsp;&nbsp;&nbsp;\[Kari\] sin \[bok\]\] ligger på \[bordet\].

But note the difference when the determinant is independent:

&nbsp;&nbsp;&nbsp;&nbsp;\[Kari\]<sub>1</sub> la \[boka \[si\]<sub>1</sub>\] på \[bordet\].

The same is true for the similar construction found in Nynorsk:

&nbsp;&nbsp;&nbsp;&nbsp;\[Boka\] hennar \[Kari\] ligg på \[bordet\].

&nbsp;&nbsp;&nbsp;&nbsp;\[Silje\]<sub>1</sub> ga \[boka \[si\]<sub>1</sub>\]<sub>2</sub> til \[Kari\]<sub>3</sub>. \[Kari\]<sub>3</sub> la \[boka \[hennar\]<sub>1</sub>\]<sub>2</sub> på bordet\].


#### Notes on pronominal differences between Nynorsk and Bokmål.
Note that although han and hun are mainly used with human or at least animate referents in Bokmål, they are used with all nouns regardless of animacy in Nynorsk. This can some times lead to ambiguity.

&nbsp;&nbsp;&nbsp;&nbsp;[Kari] las [boka]. [Ho] var interessant. (boka var interessant)
&nbsp;&nbsp;&nbsp;&nbsp;[Kari] leste [boka]. [Den] var interessant.

&nbsp;&nbsp;&nbsp;&nbsp;[Nils] køyrar i [ein kul bil]. [Han] er grønn. (bilen er grønn)
&nbsp;&nbsp;&nbsp;&nbsp;[Nils] kjører i [en kul bil]. [Den] er grønn.


## Chapter 4: Annotating in BRAT
The annotations are done using the annotation tool BRAT. This chapter describes the brat-specific annotation guidelines.

#### Markables

The texts are automatically pre-annotated based on the underlying syntax from the treebank. All noun phrases that pass the specifications for markables are pre-annotated and highlighted in yellow. Annotators are still expected to be wary of errors in the pre-annotation, and fix errors if they find any.  

#### General
Each annotator has their own account, and annotate on their own computer. Remember to log in in order to be able to annotate. You can change annotation mode to remove pop-up boxes when wanting to delete an annotation. Marking from right to left makes Brat less prone to inadvertedly mark unwanted text. Relations are drawn by clicking a markable and then dragging a relation to another markable. The direction counts: dragging from a later anaforic expression to an antecedent creates an anaphoric relation (most common), while dragging the other way creates a cataphoric relation. A computer mouse is handy for dragging long-distance relations. If there is a long distance between an anaphor and its antecedent, select and hold the relation, and use the scrolling wheel to move up in the document.

#### Errors, Changing and Deletion
BRAT does not tolerate line shifts as parts of spans. If you include a newline in a span by accident, BRAT will give you an error warning. In order to fix this, go to the relevant .ann file and remove the part with the line shift. If this happens towards the end of the .ann-file, you can safely remove a few lines, but if it happens between other types of annotations, make sure that the fixed spans match, and that you do not delete any annotations that might be related to earlier or later entities.

To change the span of a markable without deleting it (and also without deleting any relations to or from it), you can use the MOVE button. A similar option is available for relations: RESELECT.

## Summary and tips
When annotating the first round, try to get an overview of the markables first. Reading through the document can prepare you for which markables that might appear later in the document. You can also try to annotate one chain at a time, to make it easier to remember the relevant phrases.

