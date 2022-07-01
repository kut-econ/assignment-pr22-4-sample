# 以下にコードを記述してください。
# %%
# oz.mdの読み込み
with open('./oz.md','r') as file:
    text = file.readlines()
# タイトル部分とそれ以外を分離
header = text[:5]
body = text[5:]
# bodyから改行のみの行を除去
# かつ各行の先頭にナンバーを付加
body = ['1. ' + s for s in body if s != '\n']
# タイトル部分とbodyを再結合
text = header + body
# ファイルへの書き込み
with open('./oz_enumerated.md','w') as file:
    file.writelines(text)
