from textblob import TextBlob

negative_words = list(set([
    "abandon", "abandonment", "aberration", "abet", "abhor", "abhorrent", 
    "abide", "abjure", "abnormal", "abject", "abnormality", "abolish", 
    "abominable", "abomination", "abort", "abortive", "abrade", "abrasive", 
    "abrupt", "abscond", "absence", "absentee", "absurd", "absurdity", 
    "abusive", "abysmal", "abyss", "accost", "accursed", "accuse", 
    "accusation", "accuser", "ache", "achilles' heel", "acidic", "acrid", 
    "acrimonious", "acridity", "acrimony", "aggravate", "aggravating", 
    "aggravation", "aggression", "aggressive", "aggressor", "agitate", 
    "agitated", "agitation", "agonize", "agonizing", "agony", "alarm", 
    "alarming", "alienation", "alibi", "aloof", "ambiguity", "ambiguous", 
    "ambush", "amputate", "anathema", "anger", "angry", "angst", 
    "annoy", "annoyance", "annoyed", "annoying", "anomalous", "anomaly", 
    "antagonism", "antagonist", "antagonistic", "antagonize", "anticlimactic", 
    "antipathy", "antiquated", "antisocial", "anxiety", "anxious", 
    "anxiousness", "apathetic", "apathy", "apocalypse", "apocalyptic", 
    "appall", "appalling", "apprehension", "apprehensive", "arbitrary", 
    "arcane", "archaic", "arduous", "arrogance", "arrogant", "ashamed", 
    "asinine", "asphyxiate", "assault", "assail", "asshole", "assumption", 
    "astray", "atrophy", "attack", "audacious", "audacity", "avenge", 
    "aversion", "avert", "avoid", "avoidance", "awful", "awkward", 
    "backslide", "bad", "badger", "badly", "bait", "baleful", 
    "balk", "banal", "banish", "banishment", "bankrupt", "barbaric", 
    "barbarous", "barbed", "barrage", "barrier", "bash", "bastard", 
    "battered", "battering", "battle", "bawl", "beating", "bedlam", 
    "bedridden", "beleaguer", "belittle", "belittlement", "belligerent", 
    "bemoan", "bemused", "bender", "bereavement", "bereft", "berserk", 
    "betray", "betrayal", "bewail", "bewildered", "bewilderment", 
    "bias", "bigot", "bigotry", "bitch", "bitter", "bitterness", 
    "bizarre", "blackmail", "blame", "blameful", "blasphemous", "blasphemy", 
    "blasted", "blatant", "bleak", "bleakness", "bleed", "blight", 
    "blister", "blithering", "block", "blockade", "bloodshed", "bloody", 
    "blot", "blunder", "blunt", "blur", "blurt", "boastful", 
    "boggle", "boil", "bombard", "bombardment", "bombastic", "boorish", 
    "bore", "boredom", "boring", "bothersome", "bound", "boundaries", 
    "bounties", "bout", "brash", "brashness", "brat", "bravado", 
    "brawl", "brazen", "breach", "break", "breakdown", "breakup", 
    "bribery", "bridle", "brimstone", "brink", "brooding", "bruise", 
    "brunt", "brutal", "brutality","no","never","n't"]))
    
    
    

def sentence_checking(sentence):
	bolbed_text=TextBlob(sentence)
	for words in bolbed_text.words:
		if words in negative_words:
			lis.append(1)
		else:
			lis.append(0)
	if (sum(lis))>0:
		return ("It is a negetive sentence!")
	else:
		return ("It is a possitive sentence!")
	
		
		
while True:
	lis=[]
	text=input(">> ")
	text=text.lower()
	print (sentence_checking(text))