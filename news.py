import newspaper
from newspaper import news_pool

# BBC News: http://www.bbc.com/news
# CNN: http://www.cnn.com
# 腾讯新闻: https://news.qq.com
# 新浪新闻: http://news.sina.com.cn
bbc_news = newspaper.build('http://www.bbc.com/news')
cnn_news = newspaper.build('http://www.cnn.com')
tent_news = newspaper.build('https://news.qq.com')
sina_news = newspaper.build('http://news.sina.com.cn')
papers = [bbc_news, cnn_news, tent_news, sina_news]
news_pool.set(papers, threads_per_source=2)
news_pool.join()
ti = []
i = 1
for paper in papers:
    for article in paper.articles:
        article.download()
        article.parse()
        # 处理该文章
         # 检查文章是否存在标题
        if article.title != "":
            title = article.title
            ti.append(title)
            print(i)
            i = i + 1
            # 处理该文章
        else:
            # 使用第一段作为标题
            first_paragraph = article.text.split('\n')[0]
            title = first_paragraph[:50] + "..."
            ti.append(title)
            print(i)
            i = i + 1

with open('news.txt', 'w',encoding='utf-8') as f:
    for item in ti:
        f.write("%s\n" % item)