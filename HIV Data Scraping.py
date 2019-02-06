from newspaper import Article

hiv_paper = newspaper.build('https://timesofindia.indiatimes.com/topic/HIV/news')

for article in hiv_paper.articles:
    print(article.url)


hiv_article = hiv_paper.articles[0]

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