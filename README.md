# Python_task_Grid_Dynamics

1) Install Git bash to clone the repository
            https://git-scm.com/downloads

2) Install python to execute the script
            https://www.python.org/downloads/release/python-3911/

3) After installing python in windows, setup the environment variable for python. following path is python installation folder
            C:\Users\manik\AppData\Local\Programs\Python\Python39

4) To execute the scrit in your local system please clone the repository  by using following command
            Git clone https://github.com/mani5a3/Python_task_Grid_Dynamics.git

5) cd Python_task_Grid_Dynamics

6) python justify.py --paragraph-string "Write your own text here" --paragraph-width 20

7) To ran the unit test cases use this command python -m unittest tests.test_paragraph_formatter.TestParagraphFormatter.test_justify_paragraph


Sample outputs i am attaching below

    C:\support-terraform\Python_task_Grid_Dynamics>python justify.py --paragraph-string "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works." --paragraph-width 20
Array [1] = "This is a sample    "
Array [2] = "text but a          "
Array [3] = "complicated problem "
Array [4] = "to be solved, so we "
Array [5] = "are adding more text"
Array [6] = "to see that it      "
Array [7] = "actually works.     "

C:\support-terraform\Python_task_Grid_Dynamics>python justify.py --paragraph-string "this is manikanta gaddam from epam system and working as devops engineer" --paragraph-width 20
Array [1] = "this is manikanta   "
Array [2] = "gaddam from epam    "
Array [3] = "system and working  "
Array [4] = "as devops engineer  "

C:\support-terraform\Python_task_Grid_Dynamics>python justify.py --paragraph-string "this is manikantagaddam from epamsystem and working as devops engineer" --paragraph-width 20
Array [1] = "this is             "
Array [2] = "manikantagaddam from"
Array [3] = "epamsystem and      "
Array [4] = "working as devops   "
Array [5] = "engineer            "

C:\support-terraform\Python_task_Grid_Dynamics>python justify.py --paragraph-string "this is manikanta gaddam from epam system and working as devops engineer" --paragraph-width 25
Array [1] = "this is manikanta gaddam "
Array [2] = "from epam system and     "
Array [3] = "working as devops        "
Array [4] = "engineer                 "

C:\support-terraform\Python_task_Grid_Dynamics>python justify.py --paragraph-string "this is manikantagaddam from epamsystem and working as devops engineer" --paragraph-width 30
Array [1] = "this is manikantagaddam from  "
Array [2] = "epamsystem and working as     "
Array [3] = "devops engineer               "


Unit testcases result:

C:\support-terraform\Python_task_Grid_Dynamics>python -m unittest tests.test_paragraph_formatter.TestParagraphFormatter.test_justify_paragraph
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

