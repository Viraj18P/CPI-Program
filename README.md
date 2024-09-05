#TechSOC Task-2
#BY-Viraj Samir Patel

Code starts from line 209.
Above i have defined variable and fucntions.
Note-Download all files before running code on pc.

-First i ask user for SignUp/Login
-Then user is student/admin based on that i have main 4 blocks of code. I have defined loginS/loginA functions above.
-I have 3 main .json file data-->for student login credentials ; dataA-->for admin login credentials, dataG-->for storing student grades.
-I have added a sample admin/student data on these files. User can add later based on the requirements.
-Student signup, once it is successful i also created a nested dictionary, that has the structure of storing the grades.
-I have kept a check on right username entered or not, and also in case of signup if existed username is entered it throws up an error.
-Further, i have given user 3 retries for entering password, in case of any mistake.
-I have added from my end, the courses(not exactly copied from IITI website, but that can be copy pasted)(4 credit each), which have by default 'NA' value.
 So incase admin does not want to enter course grades, maybe because student has not opted for them, then he can leave them as it is, it won't be counted for SPI/CPI calculation.
 Admin can see all available courses in each semester, and can enter grades.
-Could be different admin entering different grades, so admin has option to exit code after entering any course grade, or can see updated student dashboard.
-Admin must enter either int 1-10 or "NA" otherwise it will throw up an error.
-Admin has power to enter and view grades.
-Student can view his detailed dashboard, which includes grades,SPI,CPI.
-I have defined function for calculating SPI,CPI above, both under the function name SPI().Since all courses were 4 credit, it made function simpler, otherwise weighted mean formula can also be inserted.

Features
1.Role-Based Access Controls
 -Student-->View Grades,SPI,CPI
 -Admin-->Modify/View Grades
2.Storing User Credentials/Grades in separate files.
3.SPI/CPI Formula Functions
4.Edge cases Handling
 -Incorrect username
 -Correct username, Wrong Password-->Total 3 tries provided
 -Correct student id entered by admin or not
 -Grades value entered within correct range

Improvements Possible

1.Can add courses based on admin input, just like the addkey function, but thought it would be tedious for admin to enter so much.
2.Could shorten code by defining func for read/write .json files
3.Can improve SPI/CPI fomulae by used weighted mean concept, if courses had varying credits.(My func can handle varying courses in each sem, but cannot handle varying credits in each course)(Didn't try since PS
  stated each course has 4 credits.)
4.For student i can create better interface by asking which course does he/she want to see OR wants to see whole dashboard(what i did). Ask which sem SPI does he/she wants to see.Ask for CPI.

But all this i could not do due to time constraint, however these are minor things which can be implemented later on.

        



