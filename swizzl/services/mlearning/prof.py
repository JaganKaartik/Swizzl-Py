from profanity_check import predict, predict_prob

def predProf(sentence):
	return predict_prob(sentence)

print(predProf(['go to hell, you scum']))
