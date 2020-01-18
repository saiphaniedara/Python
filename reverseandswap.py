word=input()
vow=list()
final_word=""
new_word=""
for i in word:
    if i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U':
        vow.append(i)
ind=-1
for i in word:
    if i=='a' or i=='e'or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        final_word+=vow[ind]
        ind-=1
    else:
        final_word+=i
print(final_word)
i=0
while i<len(final_word)-1:
    new_word+=final_word[i+1]+final_word[i]
    i+=2
print(new_word)
