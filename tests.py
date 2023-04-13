from sentencematcher import SentenceMatch

sentences = ["Hey there", "Nice to meet you", "How are you", "How's your day going"]
userin = "How's your goddamn day goin boy!"
res, accr = SentenceMatch(userin, sentences)
print(res, accr)