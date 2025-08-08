from transformers import pipeline
unmasker = pipeline("fill-mask")
unmasker("This course will teach you all about <mask> models.", top_k=2)


'''[{'sequence': 'This course will teach you all about mathematical models.',
  'score': 0.19619831442832947,
  'token': 30412,
  'token_str': ' mathematical'},
 {'sequence': 'This course will teach you all about computational models.',
  'score': 0.04052725434303284,
  'token': 38163,
  'token_str': ' computational'}]'''



from transformers import pipeline
fill_mask = pipeline("fill-mask", model="roberta-base")
result = fill_mask("The weather today is <mask> and sunny.")
for res in result:
    print(f"{res['token_str']} — Score: {res['score']:.4f}") #token string-actual word, res['score']-is a probability

#output
# warm — Score: 0.3055
#bright — Score: 0.1676
#clear — Score: 0.1610
#nice — Score: 0.0614
#cool — Score: 0.0550

#BERT usecase
from transformers import pipeline

# BERT uses [MASK]
fill_mask = pipeline("fill-mask", model="bert-base-uncased")
result = fill_mask("I love eating [MASK] for breakfast.",top_k=2)


