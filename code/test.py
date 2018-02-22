# import nltk
import os
import pickle
# from prepros import add_patterns, get_cv_and_cin, get_words
# import pymysql.cursors
# import spacy
# from spacy.matcher import Matcher
# import webbrowser

# nlp = spacy.load('en')
# matcher = Matcher(nlp.vocab)
# adds_patterns(matcher)
# pos_tag = "CV VBG APP CV APP"
# pattern = matcher(nlp(u'{}'.format(pos_tag)))
# print pattern




# # Insert pairs.txt into mysql
# cursor = connection.cursor()
# count = 1
# with open(os.path.join(os.pardir, "Data", "cateInGroups_freq100_v2.txt")) as data_file:
#     for line in data_file:
#         tech_list = line.split("\t")
#         first = tech_list[0]
#         second = tech_list[1]
#         sql = "INSERT INTO pairs(Id, First, Second) VALUES ('%d', '%s', '%s')" % (count, first, second)
#         cursor.execute(sql)
#         connection.commit()
#         count += 1
# connection.close()

synonyms_file = open(os.path.join(os.pardir, "data", "synonyms_for_all_similar_techs.pkl"), 'rb')
synonyms = pickle.load(synonyms_file)
synonyms_file.close()

for key in synonyms.keys():
    if key[0] == ".":
        print(key)
