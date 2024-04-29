with open ('myfile.txt', 'r') as file:
           data = file. read ()
           print(data)
with open ('myfile.txt', 'w') as file: 
           file. write ("Hello world! \n")

with open ('myfile.txt', 'a') as file:
           file. write ("Appending new data\n") 

with open ('myfile.txt', 'r') as file:
           for line in file:
                print (line. strip ())
try:
    with open ('myfile.txt', 'r') as file:
           data=file. read ()
           print(data)
except FileNotFoundError:
    print ("File not found")

except Exception as e:
       print ("An error occurred :" ,e)
