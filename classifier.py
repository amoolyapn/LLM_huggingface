from transformers import pipeline
classifier = pipeline("sentiment-analysis")
classifier("I like to study" , "But i hate assignments")

#output
#[{'label': 'POSITIVE', 'score': 0.9994291663169861}]


from transformers import pipeline
classifier=pipeline("sentinemnt-analysis")
classifier("But i hate doing assignments")

#output
#[{'label': 'NEGATIVE', 'score': 0.9885258674621582}]


from transformers import pipeline
classifier = pipeline("sentiment-analysis")
classifier(["I like to study" , "But i hate doing assignments"])

#output
#[{'label': 'POSITIVE', 'score': 0.9994291663169861},
 #{'label': 'NEGATIVE', 'score': 0.9885258674621582}]


from transformers import pipeline
classifier=pipeline("sentiment-analysis")
classifier("India won a match")

#output
#[{'label': 'POSITIVE', 'score': 0.9997269511222839}]


from transformers import pipeline
classifier=pipeline("sentiment-analysis")
classifier("Rohan had an accident")

#output
#[{'label': 'NEGATIVE', 'score': 0.9947031140327454}]


#Zero-shot classification
from transformers import pipeline

classifier = pipeline("zero-shot-classification")
classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)

#output
#{'sequence': 'This is a course about the Transformers library',
 #'labels': ['education', 'business', 'politics'],
 #'scores': [0.8445963859558105, 0.111976258456707, 0.043427448719739914]}
