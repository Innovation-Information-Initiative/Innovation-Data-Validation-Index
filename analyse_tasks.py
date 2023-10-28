import collections
import json

inno_tasks = []
ml_tasks = []

for line in open('inno_task.txt', 'r').readlines():
	inno_tasks.append(line.strip())


for line in open('ml_task.txt', 'r').readlines():
	ml_tasks.append(line.strip())


inno_counter = collections.Counter(inno_tasks)
ml_counter = collections.Counter(ml_tasks)

print(json.dumps({k: v for k, v in sorted(inno_counter.items(), key=lambda item: item[1], reverse=True)}, indent=2))
print(json.dumps({k: v for k, v in sorted(ml_counter.items(), key=lambda item: item[1], reverse=True)}, indent=2))


# print(json.dumps(inno_counter, indent=2), '\n', json.dumps(ml_counter, indent=2))

# ml_terms = list(set(ml_tasks))
# inno_terms = list(set(inno_tasks))

# print(ml_terms, inno_terms)


# {
#   "name disambiguation": 11,
#   "patent similarity": 7,
#   "geocoding": 6,
#   "firm matching": 5,
#   "citation extraction": 3,
#   "classification": 3,
#   "localisation": 2,
#   "gender estimation": 2,
#   "scope estimation": 2,
#   "keyword extraction": 2,
#   "patent classification": 2,
#   "CPC classification": 1,
#   "product identification": 1,
#   "citation provenance": 1,
#   "patent family analysis": 1,
#   "age estimation": 1,
#   "patent pairs": 1,
#   "citation analysis": 1,
#   "dependency": 1,
#   "novelty": 1,
#   "entity extraction": 1,
#   "innovation measurement": 1,
#   "financial market analysis": 1,
#   "patent identification": 1,
#   "semantic analysis": 1
# }
# {
#   "similarity": 6,
#   "semantic analysis": 6,
#   "matching": 3,
#   "classification": 3,
#   "text retrieval": 2,
#   "summarisation": 2,
#   "parsing": 1,
#   "entity extraction": 1,
#   "labelling": 1,
#   "sentiment analysis": 1
# }