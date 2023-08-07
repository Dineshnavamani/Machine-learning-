import csv
a = []
with open('D:/folders/ML/CSV/enjoysport.csv', 'r') as csvfile:
    print("Concepts : \n")
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)
print("\nThe total number of training instances are : ", len(a))
# a[0] is column name from that reduce 1 value for initial hypothiesis
num_attribute = len(a[0])-1
print("\nThe initial hypothesis is : ")
hypothesis = ['0']*num_attribute
print(hypothesis)

for i in range(0, len(a)):
    if a[i][num_attribute] == 'yes':
        for j in range(0, num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
print("\nThe hypothesis for the training instance {} is :\n" .format(i+1), hypothesis)
print("\nThe Maximally specific hypothesis for the training instance is ")
print(hypothesis)
