# -*- coding: utf-8 -*-

# Lilja Øvrelid
import os
import re
import sys

from sys import argv
from collections import defaultdict




# Functions for accessing the conll data fields
# Input: a list of fields for a token
#****************************************************************************#
def get_id(fields):
    """
    return the token id
    """
    return int(fields[0])


def get_form(fields):
    """
    return the word form
    """
    return fields[1]

def get_lemma(fields):
    """
    return the lemma
    """
    return fields[2]

def get_cpos(fields):
    """
    return the cpos
    """
    return fields[3]

# return the fine grained part of speech
def get_pos(fields):
    """
    return the pos
    """
    return fields[4]

def get_feats(fields):
    """
    return the feats
    """
    return fields[5]

def get_head(fields):
    """
    return the head
    """
    return int(fields[6])

# return the dependency relation
def get_deprel(fields):
    return fields[7]

# return a line of token data in a sentence, given a token id
def get_data(id, sentence):
    return sentence[id-1]

#NP = Nominal heads + all dependents of a nominal head forms a NP
#Nominal = 
# * subst, 
# * pron (pers, not expletive: deprel FSUBJ, FOBJ), 
# * det poss
# * adj (nominal deprel: SUBJ/OBJ/PUTFYLL)


def get_NP(s,graph,token):
    token_id = get_id(token)
    visited = None
    deps = dfs(graph, token_id, s, visited)
    filtered = filter_deps(s,sorted(deps))

    #uncomment this to output NP forms
    # forms = []
    # for dep in filtered:
    #    deprel = get_deprel(s[dep-1])
    #    form = get_form(s[dep-1])
    #    forms.append(form)
    # return forms

    return filtered


def get_NP_nokoord(s,graph,token):
    token_id = get_id(token)
    visited = None
    deps = dfs_nokoord(graph, token_id, s, visited)
    filtered = filter_deps(s,sorted(deps))
    #uncomment this to output NP forms
    # forms = []
    # for dep in filtered:
    #     deprel = get_deprel(s[dep-1])
    #     form = get_form(s[dep-1])
    #     forms.append(form)
    
    # return forms

    return filtered





def filter_deps(s,deps):
    first = deps[0]
    firstdep = get_deprel(s[first-1])
    if firstdep == "KONJ":
        deps.pop(0)
    elif firstdep == "FLAT" and len(deps) == 1:
        deps.pop(0)
    elif firstdep == "APP" and len(deps) == 1:
        deps.pop(0)
    return deps


def is_nominal(token,s):
    pos = get_pos(token)
    feats = get_feats(token)
    dep = get_deprel(token)

    r = re.compile('.*pers.*')
    pers = r.match(feats)
    r2 = re.compile('.*poss')
    poss = r2.match(feats)
    
    if pos == "subst":
        return True
    elif pos == "pron":
       if pers:
            if dep == "FSUBJ" or dep == "FOBJ":
                return False
            else:
                return True
    elif pos == "det" and poss:
        return True
    elif pos == "adj" and is_nominal_dep(dep):
        return True
    elif pos == "adj" and dep == "KOORD":
        head = get_head(token)
        headdep = get_deprel(s[head-1])
        if is_nominal_dep(headdep):
            return True
    else:
        return False


def is_nominal_dep(dep):
    if dep == "SUBJ" or dep == "OBJ" or dep == "PUTFYLL":
        return True
    else:
        return False



def has_dep_label(deprel,deps):
    labels = []
    if deps:
        labels = map(get_deprel,deps)
        if deprel in labels:
            return True
        else:
            return False
    else:
        return False


def dependents(sentence, head):
    current_id = 1
    dependents = []

    while current_id <= len(sentence):
        if head != current_id:
            current_fields = sentence[current_id-1]
            current_head_id = get_head(current_fields)

            if head == current_head_id:
                dependents.append(current_fields)

        current_id = current_id+1

    return dependents




def make_digraph(sent):
    Gr = {}

    # for each word in the sentence
    for token_data in sent:
        word = get_form(token_data)
        word_id = get_id(token_data)

        # add the id for the word, if not already present.
        if word_id not in Gr:
            Gr[word_id] = set()

        # find the head-info for the current token
        head = get_head(token_data)
        head_data = get_data(head, sent)
        head_id = get_id(head_data)

        if head_id not in Gr:
            Gr[head_id] = set()

        # add the path from the head to the dependent
        Gr[head_id].add(word_id)

    return Gr


def dfs(graph, start, sentence, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        nextdata = sentence[next - 1]
        nextrel = get_deprel(nextdata)

        dfs(graph, next, sentence, visited)
# koordinering følges ikke, vi vil ikke ha en markable for hele koordineringen
#        if nextrel == "KOORD":
#            return visited
#        else:
#  dfs(graph, next, sentence, visited)

#    print(visited)
    return visited

def dfs_nokoord(graph, start, sentence, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        nextdata = sentence[next - 1]
        nextrel = get_deprel(nextdata)

        if nextrel == "KOORD":
#            return visited
            next
        else:
            dfs(graph, next, sentence, visited)


    return visited




#######################
# Main processing loop
# Read a conll file


def is_continuous(liste):
    # checks if all the numbers of a list follow each other
    if len(liste) <= 1:
        return True
    current = liste[0]
    for number in liste[1:]:
        if number != current + 1:
            return False
        current = number
    return True

def indekser(start_index,sentence_tokens, sublist): #petter
    # Takes the start index of a sentence (start_index)
    # and a list of all the tokens in the sentence (sentence_tokens)
    # and a list that forms a noun phrase (sublist)
    indices = []
    index = start_index
    num = 0
    sent_length = len(sentence_tokens)
    # legger til +1 fordi sublist-indeksene begynner på 1.
    while num < sent_length:
        if num+1 not in sublist:
            index += len(sentence_tokens[num]) + 1
            num += 1
        else:
            indices.append(index)
            while num+1 in sublist:
                index += len(sentence_tokens[num]) + 1
                num += 1
            indices.append(index-1)
    return indices[0],indices[-1]


def break_up(token_list):
    # takes a list of discontinuous indices and splits them into continuous chunks
    # this function is only called on for lists > 1
    new = []
    temp = []
    c = token_list[0]
    temp.append(c)
    for e in token_list[1:]:
        if e == c + 1:
            temp.append(e)
            c = e
        else:
            new.append(temp)
            temp = [e]
            c = e
    new.append(temp)
    return new



def process(conll_file):
    global tokencounts, sentencecounts, poscounts, depcounts, wordcounts, verbcounts
    # List of lists. Each element is a list of data for a token in the sentence
    sentence = []
    #----------------------------------------------------petter start
    file_string = conll_file #henter ut filnavnet, så det kan brukes til å generere de nye dokumentene.
    print(file_string)
    newname = file_string[:-6]
    print(newname)
    # Write text file and annotation file
    txt_output = open(newname + ".txt","w",encoding="utf-8")
    ann_output = open(newname + ".ann","w",encoding="utf-8")
    # Each markable is an entity (T) in BRAT
    entities = [] #p liste over uttrykk av typen "T 1 12 
    T = 1 #counter for entities #p
    document_text = "" #Hold the whole document
    index = 0
    #----------------------------------------------------petter slutt
    file_data = open(conll_file, 'r')
        # read a line with token info from the file
        # split this string into its 10 elements as a list
    for line in file_data:
        if not line.startswith("#"):

            if line != '\n':
            # Extract token data, add the token data to the sentence.
                fields = line.split('\t')
                sentence.append(fields)

            # Blank line reached, finished reading a sentence.
            else:
                graph = make_digraph(sentence)
                token_list = [x[1] for x in sentence]#p
                setn = " ".join(token_list) #p
                for token in sentence:
                    if is_nominal(token,sentence):
                        tokenid = get_id(token)
                        deps = dependents(sentence, tokenid)
                        np = get_NP(sentence,graph,token)
                        if np != []: #p
                            if not is_continuous(np):
                                disc_inds = []
                                setn_strings = []
                                for sub_np in break_up(np):
                                    x,y = indekser(0,token_list,sub_np) #start at 0 index
                                    disc_inds.append("{} {}".format(index+x,index+y))
                                    setn_strings.append("{}".format(setn[x:y]))
                                    #brat_text = "T{}\tMarkable {} {}\t{}".format(T,index+x,index+y,setn[x:y])
                                    #T += 1
                                brat_text = "T{}\tMarkable {}\t{}".format(T,";".join(disc_inds), " ".join(setn_strings))
                                ann_output.write(brat_text + "\n")
                                T += 1
                            else:
                                x,y = indekser(0,token_list,np) #start at 0 index
                                brat_text = "T{}\tMarkable {} {}\t{}".format(T,index+x,index+y,setn[x:y])
                                T += 1
                                ann_output.write(brat_text + "\n")
                        if has_dep_label("KOORD",deps):
                            np = get_NP_nokoord(sentence,graph,token)
                            if np != []:
                                if not is_continuous(np):
                                    # for cases when the span is discontinuous
                                    disc_inds = []
                                    setn_strings = []
                                    for sub_np in break_up(np):
                                        x,y = indekser(0,token_list,sub_np) #start at 0 index
                                        disc_inds.append("{} {}".format(index+x,index+y))
                                        setn_strings.append("{}".format(setn[x:y]))
                                    brat_text = "T{}\tMarkable {}\t{}".format(T,";".join(disc_inds), " ".join(setn_strings))
                                    ann_output.write(brat_text + "\n")
                                    T += 1
                                else:
                                    x,y = indekser(0,token_list,np) #start at 0 index
                                    brat_text = "T{}\tMarkable {} {}\t{}".format(T,index+x,index+y,setn[x:y])
                                    T += 1
                                    ann_output.write(brat_text + "\n")   
                txt_output.write(setn+"\n")
                index += len(setn) +1                        
                sentence = []

    file_data.close()
    txt_output.close()
    ann_output.close()
    



def format_word(t):
    fields = []
    fields.append(str(get_id(t)))
    fields.append(get_form(t))
    fields.append(get_lemma(t))
    fields.append(get_cpos(t))
    fields.append(get_pos(t))
    fields.append(get_feats(t))
    fields.append(str(get_head(t)))
    fields.append(get_deprel(t))
    fields.append("_")
    fields.append("_")
#    print fields
    return fields
    
def process_folder():
    # when this is run, all documents in a folder are processed
    files = os.listdir()
    #    assert len(files) == 10 #there should always be only 10 files
    # can now process
    for f in files:
        if f[-5:] == "conll":        # so we do not try to process the wrong files
            process(f)
    print("All files processed")    
    

def print_conll(s):
    for token_data in s:
        print("\t".join(format_word(token_data)))
    print


def get_relfreq(freq,total):
    rel = freq / total
    return(rel)




def read_single_file():
    file = argv[1]
    process(file)

#comment out the one of the following calls depending on use:

#read_single_file()
process_folder()



#------------------------------
#f = open(file)
# text = f.read()
#f.close()



