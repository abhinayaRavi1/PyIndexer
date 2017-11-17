import sys,re,string
wordlist=" "
resstr=""
words=" "
number=[]
plurals=""
sing=""
final=[]
stopwords=['and','a','the','an','by','from','for','hence','of','the','with','in','within','who','when','where','why','how','whom','have','had','has','not','for','but','do','does','done']
#Read an argument
f=open(sys.argv[1],"r")
init=""
#Run through the document
while 1:
    line=f.readline()
    if not line:break
    init += line
#Convert to lower case
init=init.lower()
#Break html tags
words=re.sub('<[^>]*>','',init)
#Handle paranthese and special characters
words=re.sub('[()[\]{}"\"``]','',words)
words=re.sub("'",'',words)
words=re.sub('[,.\?:;\!\+\-%\@#\$\^\&\*\~]',' ',words)
words=re.sub('-',' ',words)
wordlist=words.split()
#Check for plurals,numbers and index other terms 
for w in wordlist:
    if w.endswith('ies') and not(w.endswith('aies')) and not(w.endswith('eies')):
        plurals+=' '+re.sub('ies$','y',w)
    elif w.endswith('es') and not(w.endswith('aes')) and not(w.endswith('ees')) and not(w.endswith('oes')):
        plurals+=' '+re.sub('es$','e',w)        
    elif w.endswith('s') and not(w.endswith('us')) and not(w.endswith('ss')) and w in stopwords:
         plurals+=' '+re.sub('s$',' ',w)
    elif w.isdigit():
        number.append(w)
    elif w in stopwords or len(w)>1 and w not in number:
         resstr+=' '+w
    else:
        continue
a=plurals.split()
single=""
#Check for stopwords after the plurals are removed
for s in a:
    if s in stopwords:
        single+=' '+s
#Put all index terms together
resstr+=single
a=resstr.split()
#Removing duplicates in the final list
for i in a:
    if i not in final:
        final.append(i)
#Sorting in lexicographic order
final.sort()
#Insert the numbers into the list at the first position
final.insert(0,number)
#Output of index terms
for i in final:
    print(i)





