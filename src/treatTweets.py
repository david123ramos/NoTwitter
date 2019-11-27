import pandas as pd , demoji
from cucco import Cucco



data = pd.read_csv('EmotionsDataset.csv')

teste = ""
count = 0

# for string in data['Texto'].values:
#     finalTxt = string.split(" ")
#     for aux in finalTxt:
#         if not '@' in aux:
#             teste += aux + " "

#     teste = Cucco.replace_emojis(teste)
#     teste = teste.replace('"', '')
#     data['Texto'][count] = data['Texto'][count].replace(data['Texto'][count], teste)
#     teste = ""
#     count += 1

del data['Unnamed: 0']

print(data)
with open('EmotionsDataset.csv', 'w') as dataset:
    data.to_csv(dataset, index=False)

