#! python3

#Simple py3 program to parse the filenames of GAIT Scorecards and output a txt file with sorted list of candidates according to score
# File Name: 'CompiledList.txt'
#Run only in the dir containing the pdf scorecards

import os, re, operator, time

#Compile the pattern for string matching (FirstName_MiddleName_LastName_score.pdf)
#**sometimes the lastname is not present, sometimes people have middle name too**

nameAndNumberFinder = re.compile(r'(([a-zA-Z.]+)_(([a-zA-Z]+)_)?(([a-zA-Z]+)_)?(\d+))')

#clears the list file, if present
newFile = open('CompiledList.txt','w')
newFile.write('#RecordNo Name (Score) \n\n')
newFile.close()

#create a dict to store value key pairs
numberDict = {}
for fileName in os.listdir('.'):
    try:
        if('.pdf' in fileName):
            foundName = nameAndNumberFinder.search(fileName)
            #check for middle name and last name
            if(foundName.group(4) != None and foundName.group(5) != None):
                numberDict.update({foundName.group(2)+' '+foundName.group(4)+' '+foundName.group(6):int(foundName.group(7))})
            elif(foundName.group(4) != None):
                numberDict.update({foundName.group(2)+' '+foundName.group(4):int(foundName.group(7))})
            else:
                numberDict.update({foundName.group(2):int(foundName.group(7))})
    except:
        print('Error Parsing: '+fileName)

#sort the dict on values and store in a list
sorted_dict = sorted(numberDict.items(),key=operator.itemgetter(1))

#reverse the list for ascending order
sorted_dict.reverse()

#count will keep track of record number
count = 1

#write the file
newFile = open('CompiledList.txt','a')
for name,score in sorted_dict:
    newFile.write('#'+str(count)+' '+name.upper()+' ('+str(score)+')\n')
    count = count+1

newFile.write('\n\nList Compiled on: '+time.strftime("%c"))
newFile.close()
