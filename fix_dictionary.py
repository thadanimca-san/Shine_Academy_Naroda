with open('/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english/data/dictionary_topics.dart', 'a') as f:
    f.write("\n\nfinal allDictionaryTopics = dictionaryLibraryByGrade.values.expand((lib) => lib.topics).toList();\n")
