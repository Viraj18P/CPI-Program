#TechSOC Task-2

First I have imported JSON library.

Then the code starts from line 210.
Where i first ask the user either he/she wants to login or signup. I have not added any data in the files at first, so we will start with signup.

##Signup
Here, now i will ask you, that are you a student or an admin?
Based on that i have created if else statements.

###Signup Student
First I have created a file named data.json to save the username and password of the students.
So first i will open the file in read format by the code
'''python
with open(filepath,'r') as file:
  data=json.load(file)
  '''
