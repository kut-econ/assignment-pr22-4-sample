# 以下にコードを記述してください。
# %%
# テキストの読み込み
with open('oz.md','r') as file:
    text = file.read()
# 特殊文字除去のためのtrans辞書作成
trans_rule = {'#':' ',',':' ','"':' ',':':' ',';':' ','!':' ','.':' ','\n':' '}
trans = str.maketrans(trans_rule)
# 重複を許した単語のリスト作成(小文字への変換も)
all_text = text.translate(trans).lower().split(' ')
# (必要ないが、いちおう空文字の除去)
all_text = [w for w in all_text if w!='']
# 重複を許さない単語のリスト作成
words = sorted(list(set(all_text)-{''}))
# 上記を理解し、この続きを書いてください。

# %%
# 各単語の出現回数を記録した辞書wcountを作成
wcount = {}
for w in words:
    wcount[w] = all_text.count(w)
# 重複の無い出現回数のリストを作成(ソーティングも行う)
value_list = sorted(list(set(wcount.values())))
# 出現回数vごとに、そのv回出現する単語の数を印字
for v in value_list:
    no_words = len([w for w in wcount.keys() if wcount[w]==v])
    print(v,'times -->',no_words,'words')
