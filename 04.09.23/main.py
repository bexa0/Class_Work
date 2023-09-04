# лемматизации
import json
from pymystem3 import Mystem
from tqdm import tqdm
from joblib import Parallel, delayed

# text = 'Красивая женцина или красиво'
# m = Mystem()
# lem = m.lemmatize(text)
# print('lemmas: ', ''.join(lem))
# print('full info:', json.dumps(m.analyze(text),
#       ensure_ascii = False))


batch_size = 1000

mytext = ['Мама мыла раму {}'.format(i) for i in range(10000)]
text_batch = [mytext[i: i + batch_size] for i in range(0, len(mytext), batch_size)]

def lemmatize(text):
    m = Mystem()
    merged_text = '|'.join(text)

    doc = []
    res = []

    for t in m.lemmatize(merged_text):
        if t != '|':
            doc.append(t)
        else:
            res.append(doc)
        doc = []
    return  res
processing_texts = Parallel \
    (n_jobs= - 1) \
    (delayed(lemmatize)(t) for t in tqdm(text_batch))