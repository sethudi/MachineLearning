from sklearn.metrics import normalized_mutual_info_score

target = [0, 0, 0, 1, 1, 1]
predicted = [1, 1, 1, 0, 0, 0]

print(normalized_mutual_info_score(target, predicted))