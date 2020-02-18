import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df_books = pd.read_csv('book_data.csv')
df_books = df_books.dropna(
    subset=['book_pages', 'genres', 'image_url']
    )
df_books['corpus'] = (pd.Series(df_books[['book_authors', 'genres']].fillna('').values.tolist()).str.join(' '))

def buku_favorit(title):
    return df_books[df_books['book_title'] == title]

def rekomendasi_buku(title):
    ext = CountVectorizer(tokenizer= lambda x: x.split('|'))
    mcorpus = ext.fit_transform(df_books['corpus'].head(8500))
    mcorpus.toarray()
    cos_score = cosine_similarity(mcorpus)

    index_suka = df_books[df_books['book_title'] == title].index[0]
    buku_sama = list(enumerate(cos_score[index_suka]))
    buku_rangking = sorted(buku_sama, key=lambda x:x[1], reverse=True)
    buku_rangking.remove(buku_sama[index_suka])

    list_dict = []
    dict_rank = {}
    
    for i in buku_rangking[:10]:
        dict_rank['authors'] = df_books.iloc[i[0]]['book_authors']
        dict_rank['format'] = df_books.iloc[i[0]]['book_format']
        dict_rank['isbn'] = df_books.iloc[i[0]]['book_isbn']
        dict_rank['pages'] = df_books.iloc[i[0]]['book_pages']
        dict_rank['rating'] = df_books.iloc[i[0]]['book_rating']
        dict_rank['title'] = df_books.iloc[i[0]]['book_title']
        dict_rank['genres'] = df_books.iloc[i[0]]['genres']
        dict_rank['desc'] = df_books.iloc[i[0]]['book_desc']
        dict_rank['image'] = df_books.iloc[i[0]]['image_url']
        list_dict.append(dict_rank)
        dict_rank = {}
    return(list_dict)

def rekomendasi_genre(title):
    ext = CountVectorizer(tokenizer= lambda x: x.split('|'))
    mgenre = ext.fit_transform(df_books['genres'].head(8500))
    mgenre.toarray()
    cos_score = cosine_similarity(mgenre)

    index_suka = df_books[df_books['book_title'] == title].index[0]
    buku_sama = list(enumerate(cos_score[index_suka]))
    buku_rangking = sorted(buku_sama, key=lambda x:x[1], reverse=True)
    buku_rangking.remove(buku_sama[index_suka])

    list_dict = []
    dict_rank = {}
    
    for i in buku_rangking[:10]:
        dict_rank['authors'] = df_books.iloc[i[0]]['book_authors']
        dict_rank['format'] = df_books.iloc[i[0]]['book_format']
        dict_rank['isbn'] = df_books.iloc[i[0]]['book_isbn']
        dict_rank['pages'] = df_books.iloc[i[0]]['book_pages']
        dict_rank['rating'] = df_books.iloc[i[0]]['book_rating']
        dict_rank['title'] = df_books.iloc[i[0]]['book_title']
        dict_rank['genres'] = df_books.iloc[i[0]]['genres']
        dict_rank['desc'] = df_books.iloc[i[0]]['book_desc']
        dict_rank['image'] = df_books.iloc[i[0]]['image_url']
        list_dict.append(dict_rank)
        dict_rank = {}
    return(list_dict)

def rekomendasi_author(title):
    ext = CountVectorizer(tokenizer= lambda x: x.split('|'))
    mauthor = ext.fit_transform(df_books['book_authors'].head(8500))
    mauthor.toarray()
    cos_score = cosine_similarity(mauthor)

    index_suka = df_books[df_books['book_title'] == title].index[0]
    buku_sama = list(enumerate(cos_score[index_suka]))
    buku_rangking = sorted(buku_sama, key=lambda x:x[1], reverse=True)
    buku_rangking.remove(buku_sama[index_suka])

    list_dict = []
    dict_rank = {}
    
    for i in buku_rangking[:10]:
        dict_rank['authors'] = df_books.iloc[i[0]]['book_authors']
        dict_rank['format'] = df_books.iloc[i[0]]['book_format']
        dict_rank['isbn'] = df_books.iloc[i[0]]['book_isbn']
        dict_rank['pages'] = df_books.iloc[i[0]]['book_pages']
        dict_rank['rating'] = df_books.iloc[i[0]]['book_rating']
        dict_rank['title'] = df_books.iloc[i[0]]['book_title']
        dict_rank['genres'] = df_books.iloc[i[0]]['genres']
        dict_rank['desc'] = df_books.iloc[i[0]]['book_desc']
        dict_rank['image'] = df_books.iloc[i[0]]['image_url']
        list_dict.append(dict_rank)
        dict_rank = {}
    return(list_dict)