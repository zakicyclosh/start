exemple = [[[1,2,3],2,[1,3]],[1,2,3]]
element = 2

def index_all (exemple, element) :
  indices = []
  for index , value in enumerate(exemple) :
    if value == element :
      indices.append([index])
    elif isinstance(exemple[index],list) :
      for i in index_all(exemple[index],element):
         indices.append([index]+i)
      
  return indices

print(index_all(exemple,element))

