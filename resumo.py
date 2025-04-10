import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Carregando um dataset de fake news
df = pd.read_csv('fake_or_real_news.csv')  # dataset com colunas: 'text' e 'label'

# Separando os dados
X = df['text']
y = df['label']  # 0 para fake, 1 para real

# Pré-processamento e vetorização com TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vect = vectorizer.fit_transform(X)

# Dividindo em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

# Treinando o modelo
model = LogisticRegression()
model.fit(X_train, y_train)

# Avaliando o modelo
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
