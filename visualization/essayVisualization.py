import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# カラムは右記id, prompt_id, text, generated
essays_1 = pd.read_csv('essays1.csv')

# カラムは右記text, label, prompt_name, source, RDizzl3_seven
essays_2 = pd.read_csv('essays2.csv')

# essays1.csvをprompt別で件数表示
f, ax = plt.subplots(figsize=(7, 3))
sns.despine()
ax = sns.countplot(data=essays_1, x="prompt_id")
abs_values = essays_1['prompt_id'].value_counts().values
ax.bar_label(container=ax.containers[0], labels=abs_values)
plt.savefig('essays1_prompt.png')

# essays1.csvをgenerated別で件数表示
f, ax = plt.subplots(figsize=(7, 3))
sns.despine()
ax = sns.countplot(data=essays_1, x="generated")
abs_values = essays_1['generated'].value_counts().values
ax.bar_label(container=ax.containers[0], labels=abs_values)
plt.savefig('essays1_generated.png')

# essays2.csvをprompt_name別で件数表示
f, ax = plt.subplots(figsize=(7, 3))
plt.xticks(rotation=90) # prompt_nameがラベル上で重複したため回転
sns.despine()
ax = sns.countplot(data=essays_2, x="prompt_name")
abs_values = essays_2['prompt_name'].value_counts().values
ax.bar_label(container=ax.containers[0], labels=abs_values)
plt.savefig('essays2_prompt_name.png')

# essays2.csvをlabel別で件数表示
f, ax = plt.subplots(figsize=(7, 3))
sns.despine()
ax = sns.countplot(data=essays_2, x="label")
abs_values = essays_2['label'].value_counts().values
ax.bar_label(container=ax.containers[0], labels=abs_values)
plt.savefig('essays2_label.png')

# essays1とessays2を結合
essays_2.rename(columns = {"label":"generated"}, inplace=True) # labelがessays1のgeneratedと等価であったためカラム名変更
essays_marge = pd.concat([essays_1[["text", "generated"]], essays_2[["text", "generated"]]])

# マージ後のtext列には文章が入っているので単語数と文字数をそれぞれカウントした列を作成
essays_marge["word_length"] = essays_marge["text"].apply(lambda x : len(x.split()))
essays_marge["essay_length"] = essays_marge["text"].apply(len)

# 単語数をgenerated毎に件数表示
sns.histplot(essays_marge[essays_marge['generated'] == 0]['word_length'], color="yellow", label='generated 0', kde=True)
sns.histplot(essays_marge[essays_marge['generated'] == 1]['word_length'], color="purple", label='generated 1', kde=True)
plt.legend()
plt.show()

# 文字数をgenerated毎に件数表示
sns.boxplot(x='generated', y='essay_length', data=essays_marge)
plt.xticks([0, 1])
plt.show()