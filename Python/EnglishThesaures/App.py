import json

data=json.load(open("data.json"))

def transalte(word):
	word.lower()
	if word in data:
		return data[word]
	else:
	    return"Word does not exist, Please double check!"	

	


word= input("Enter a word: ")


print(transalte(word))