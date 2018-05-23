#1. Open the filenames.txt file with read-only access with the open() function

open_file = open('filenames.txt', 'r')

#2. Print the name of the file and if it is open or closed using the .name and .closed properties

print(open_file.name)

print(open_file.closed)

#3. Use a for loop to read all lines of filenames.txt into a list variable

print('\n')

some_list = []

for line in open_file:
    some_list += [line]

#4. Print out all the lines from the file from your variable

for i in some_list:
    print(i)

#5. Close the filenames.txt file and print if the file is open or closed

open_file.close()

print(open_file.closed)

#6. Create a file using the open() function called secrets.txt

open_file = open('secrets.txt', 'w')

#7. Write your own secrets to the file with the write() function

open_file.write('your own secrets')

#8. Close the secrets.txt file using the close() method. DON'T FORGET!

open_file.close()

#9. Print out the contents of the text file in your terminal to prove it worked

print('\n')

open_file = open('secrets.txt', 'r')
open_contents = open_file.read()
print(open_contents)

#10. Open your secrets.txt file in append mode and write some more super secret info

print('\n')

open_contents = open_file.close()

open_file = open('secrets.txt', 'a')
open_file.write('\nsome more secret info')


#11. Close the secrets.txt file again using the close() function

open_file.close()

open_file = open('secrets.txt', 'r')

content_file = open_file.read()

print(content_file)

content_file = open_file.close()

#12. Rename the secrets.txt and make it a "hidden" file named .supersecret.txt using the os.rename() function

import os

os.rename('secrets.txt', 'supersecret.txt')


#13. See if you can see the file in your file explorer



#14. Create a list variable named file_names that contains a list of filenames

file_names = ['file_a', 'file_b']

#15. Use the writelines() function to append the filenames to the filenames.txt file

open_file = open('filenames.txt', 'a')
open_file.writelines(file_names)
open_file.close()

#16. Delete the initial secrets.txt file now that you have a super secret hidden version

#17. BOSS LEVEL: Use the input() function to accept user input of a filename to create and create that file.
