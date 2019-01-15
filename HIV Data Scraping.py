from newspaper import Article

url = "https://timesofindia.indiatimes.com/city/chennai/hiv-blood-tranfusion-tamil-nadu-govt-assures-action-against-officials/articleshow/67394202.cms"


hiv_article = Article(url, language="en")  

hiv_article.download()

hiv_article.parse()

hiv_article.nlp()


print("Article's Title:")
print(hiv_article.title)
print("n")


print("Article's Text:")
print(hiv_article.text)
print("n")

print("Article's Summary:")
print(hiv_article.summary)
print("n")

print("Article's Keywords:")
print(hiv_article.keywords)