# PyTohchi (Py倒置)
PyTohchiは、日本語文を倒置法に変換するPythonライブラリです。<br>
係り受け解析にspaCy/GiNZAを使用しています。<br>
spaCy: https://github.com/explosion/spaCy ([License](https://github.com/explosion/spaCy/blob/master/LICENSE))<br>
GiNZA: https://github.com/megagonlabs/ginza ([License](https://github.com/megagonlabs/ginza/blob/develop/LICENSE))

## インストール
`pip install git+https://github.com/z0ff/pytohchi.git`

## 使用例
```python
import pytohchi

sentence1 = "吾輩は猫である。名前はまだ無い。"
sentence2 = "オーストラリアに住んでいる私の兄は、大学の帰りによくカフェで勉強をしている。"

inv_root1 = pytohchi.put_root_to_head(sentence1)
assert inv_root1 == "猫である。吾輩は。無い。名前はまだ。"
inv_root2 = pytohchi.put_root_to_head(sentence2)
assert inv_root2 == "している。オーストラリアに住んでいる私の兄は、大学の帰りによくカフェで勉強を。"

inv_obl1 = pytohchi.put_obl_to_head(sentence1)
assert inv_obl1 == "猫である。吾輩は。無い。名前はまだ。"
inv_obl2 = pytohchi.put_obl_to_head(sentence2)
assert inv_obl2 == "大学の帰りによくカフェで勉強をしている。オーストラリアに住んでいる私の兄は。"
```
