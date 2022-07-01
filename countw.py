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
