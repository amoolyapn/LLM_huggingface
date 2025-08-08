from transformers import pipeline
generator=pipeline("text-generation")
generator("Biology is basically a study of life and")

#output
"""[{'generated_text': "Biology is basically a study of life and death. 
When you study it, you're not seeing a person's head, your brain, your
brain's doing what's going on. You're seeing the body.\n\nAnd so when you
look at it in a way that looks like the human body, you're really seeing the
body.\n\nThe Human Body\n\nYou're seeing the body, the brain, and the muscles
and the nerves.\n\nThe body is not the same as the brain."}]"""


#using any model from the hub in a pipeline
#1
from transformers import pipeline
generator=pipeline("text-generation", model="Anatomy")
generator("Anatomy basically deals with",max_length=20,num_return_sequence=1,)


#2
from transformers import pipeline
generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M")
generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)

