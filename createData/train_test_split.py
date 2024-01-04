from sklearn.model_selection import train_test_split
import pandas as pd
import os

dataset = pd.read_csv("/origin.csv", sep=',')

# 作成するテストデータの行数を指定
test_size = 9000
dataset_name = f"dataset-splited-test-size-{test_size}"

# random_stateはデータ分割時のランダムシード値
for random_state in range(10):
    path = dataset_name + f"-random-state-{random_state}"
    os.makedirs(path, exist_ok = True)
    train, test = train_test_split(
        dataset,
        test_size=test_size,
        random_state=random_state
    )
    train.to_csv(f"{path}/train.csv", index=False)
    
    test_X = test[["text"]]
    test_X.index.name = "id"
    test_X.to_csv(f"{path}/test_text.csv")
    
    test["generated"] = test["label"]
    test_y = test["label"]
    test_y.to_csv(f"{path}/test_labels.csv")