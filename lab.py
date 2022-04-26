myList = ["Ahmed", "Mohammed", "Mona",
          "Khareem", "Moayed", "Khadeeja", "Salim"]

filteredList = list(filter(lambda ele : ele[0:2]== "Kh" or ele[0:2] == "Mo" , myList))

print(filteredList)