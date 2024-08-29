
#Open file in read mode
file_read = open('Codingal.txt','r')
print("File in Read Mode - ")
print(file_read.read())
file_read.close()


#open file in write mode
file_write = open('Codingal.txt','w')
# write in the file
file_write.write("File in write mode........")
file_write.write("Hi! I am Penguine. I am 1yr old")
file_write.close()


#open file in append mode
file_append = open('Codingal.txt','a')
#append in the file
file_append.write("\n File in append mode......")
file_append.write("Hi! I am Penguine. I am 1yr old")
file_append.close()
