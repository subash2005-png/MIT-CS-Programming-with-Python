##Dictionary:
##    *Dictionary is a special object type which is written within {}.
##    *It has a custom indexed sequence.
##    *It consists of entries, each entries are separated by using commas.
##    *Each entry consists of a Key and a value associated with it.
##    *The value can be accessed by using the key mapped to it.
##Example:

dict={}##empty dictionary
print(type(dict))

dictt={12:55}##12 is the key,55 is the value.
print(dictt[12])##gives the value 55 by invoking the key , here 12 is key.

##    *If the given key not in the dictionary , then error will arise.
##    example:
##        print(dict[11])##error will arise

my_dict={"sub":100,"mat":99,"ram":95,"kris":100}
print(my_dict["mat"])#"mat" is key , 99 value is accessed


##Example
def find_grades(grades, students):
       """ grades is a dict mapping student names (str) to grades (str)
           students is a list of student names 
           Returns a list containing the grades for students (in same order)
       """
       l=[]
       for elem in students:
           c=grades[elem]
           print(c)
           l.append(c)
       return l
d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']

##Operations of entry on a dictionary:

diction={1:2,2:3,3:4,4:5,5:6}##5 entries here
print(diction)

#To Add an entry:

diction[6]=7 ##6 is key and 7 is value associated with that key 6.
print(diction)

#To change an entry(value):

diction[6]=8
print(diction)

#To delete an entry:

del(diction[2])##the entry will be deleted(2:value)
print(diction)


##Example:
def find_in_L(Ld, k):
      """ Ld is a list of dicts
          k is an int
          Returns True if k is a key in any dicts of Ld and False otherwise
      """
      flag=True
      for elem in Ld:
          if k in elem:
              flag=False
              return True
      if flag:
          return False

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
print(find_in_L([d1, d2, d3], 2))  # returns True
print(find_in_L([d1, d2, d3], 25))  # returns False

##To separate key and value from dictionary:

my_dict1={"sub":100,"mat":99,"ram":95,"kris":100}

print(my_dict1.keys())
list1=list(my_dict1.keys())
print(list1)

list2=list(my_dict1.values())
print(list2)

##Can iterate through entry values:

list3=list(my_dict1.items())
print(list3)

for k,v in my_dict1.items():
       print(f"key is {k} and value is {v}")

##Example:
def count_matches(d):
       """ d is a dict
       Returns how many entries in d have the key equal to its value
       """
       count=0
       for k,v in d.items():
              if k == v:
                     count+=1
       return count

d = {1:2, 3:4, 5:6}
print(count_matches(d))   
d = {1:2, 'a':'a', 5:5}
print(count_matches(d))


##To make copy of a dictionary:

d={1:"hello",2:"hiii"}
d1=d.copy()
print(d1)

##Aliasing a dictionary:

d2=d1
print(d2)
d2[5]="welcome"
print(d1,d2)

##Program to find the most repeated words on a song:

song="RAH RAH AH AH AH ROM MAH RO MAH MAH"
def dict_rep(song):
       low_s=song.lower()
       list_song=low_s.split()
       dict={}
       for w in list_song:
              if w in dict:
                     dict[w]+=1
              else:
                     dict[w]=1
       return dict

print(dict_rep(song))#{'rah': 2, 'ah': 3, 'rom': 1, 'mah': 3, 'ro': 1}

def find_freq_word(dict):
       highest=max(dict.values())
       words=[]
       for k,v in dict.items():
              if v==highest:
                     words.append(k)
       return (words,highest)

print(find_freq_word(dict_rep(song)))##(['ah', 'mah'], 3)


       







       




    





