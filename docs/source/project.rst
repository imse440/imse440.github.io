Project guidelines
==================

A big part of this course is for you to do a team project. 
This is your opportunity to take what you learned for a spin and try to get some insights to a real-world problem of your interest.

Team forming
------------

- At the beginning of the semester, you will fill out a course survey in which you are asked to indicate your project topic interests (e.g., transportation, healthcare, environment)
- You will then be assigned to a multi-disciplinary team of three with similar project topic interests (when possible).
- Your team assignment will be announced on Canvas around the third week.

General requirements
--------------------

.. - For the project you should use Python and JupyterLab (the same tools that we use in the class).
.. - You are free to include data analysis, visualization, and modeling methods that we do not cover in the class However, they should only serve as supplementary components of your project.
.. - You need to submit the PDF files generated from Overleaf (see below) to the Canvas assignments.

- You are required to use Python (version 3+) and JupyterLab for the project.
- You are free to include additional relevant work using other software or languages that we do not cover in this course. However, they should only serve as supplementary components of your project.
.. You are free to include data analysis, visualization, and modeling methods that we do not cover in the class.
- All members of a team are expected to work with about even workload on all key parts of the project, including discussions, programming, and working on Overleaf. 
- Do not modify the formats (e.g., font size, etc.) of the Overleaf templates.
- To get graded, you need to submit the PDF files generated from Overleaf (see below) to the according Canvas assignments.
- All team members are responsible to make sure the submitted files accurately reflect their work. It is highly recommended to submit early and download the submitted files to double check that no corrections are needed. 


Important dates
---------------

- **March 6 (Wed) at 6:11 PM**: Project proposal submission (team)
- **April 8 (Mon) at 6:11 PM**: Project poster submission (team)
- **April 15 (Mon) at 6:11 PM**: Final poster submission (team)
- **April 17 (Wed) at 11:00 AM (lecture time)**: Project poster presentation (team)
- **April 18 (Thu) at 6:11 PM**: Jupyter notebook and data submission (team)
- **April 19 (Fri) at 6:11 PM**: Project peer review form submission (individual)
- **Date TBA**: `CECS Senior Design Day <https://umdearborn.edu/cecs/life-cecs/senior-design-competition>`__ poster presentation (for invited teams)

Project proposal (10% of project grade)
---------------------------------------

Your team will select your own project topic and find the data that you wish to use. 
You are required to submit a project proposal, so we can make sure your selected topic and data set(s) are suitable for the project and you are on the right track.

Your project needs to be

- *authentic* (i.e., the research questions come from a real-world problem.)
- *meaningful* (i.e., the outcomes would provide values to others or are something you care deeply about.)
- *reasonably complex* (so that you can showcase a variety of things that you learned from this course with reasonable depth.) As a rule of thumb, your project should be significantly more complex than the homework problems.
- *feasible* given the project timeline. 


Proposal requirements
^^^^^^^^^^^^^^^^^^^^^

.. - One submission per team.

- **Proposal template**: You are required to use the proposal template on Overleaf (which will be provided to you later).

    - `Overleaf <https://overleaf.com/>`__ is an online collaborative `LaTeX <https://en.wikipedia.org/wiki/LaTeX>`__ editor for scientific writing. 
    - If you do not already have an Overleaf account, you will need to register for one. The *free* plan is good enough. When register, use your UMICH email. 
    - You will need to learn some basic LaTeX using online resources. You are encourage to teach each other. Below are two good starting points:

        - `The Overleaf LaTex Tutorials <https://www.overleaf.com/learn/latex/Tutorials>`__
        - `How to write a thesis using LaTeX full tutorial (YouTube video) <https://www.youtube.com/watch?v=zqQM66uAig0>`__

    .. tip::
        - You just need a few basic things to get started. Learn more as you go. 
        - **Recompile** often in Overleaf, so that if an error occurs, it's easier to track it down. 

    .. note::
        We expect *all* team members to use Overleaf as a collaborative tool (think of a Google Docs) when drafting the proposal (and the project posters in the following sections).

The proposal should be no more than two (2) pages (not including the cover page and the References section). 
It should include the following

- **Project tentative title**: Note your team may choose a topic that is different from what you indicated in the course survey.
- **Background**: A brief description of the background of the problem
- **Research questions**: What do you want to figure out? 
  You may want to check the :ref:`Schedule` on the remaining lecture topics (check the :ref:`Textbooks` and the web if you are unfamiliar with the topics).
  Note your research questions should relate to statistical modeling, rather than exploratory data analysis (e.g., what are the five largest countries in the world?) 
- **Literature review**: What has been done by others regarding the research questions? 
  Report on at least two relevant scientific articles.
  You can use `Google Scholar <https://scholar.google.com/schhp?hl=en>`__ to search for scientific articles.
  
      .. tip:: 
        
        To cite an scientific article in your proposal, you can follow the steps below. 
        (Also check the example on the proposal template.)

          - First find the article on Google Scholar. 
          - Click the **Cite** button near the bottom of the article.
          - Click the **BibTeX** button.
          - Copy and paste the text (starting with, for example, ``@article{feng2018drivers``) into the ``references.bib`` file on Overleaf.
          - Go to the place where you want to cite the article, 
            type something like ``A new study \autocite{feng2018drivers} found that``.
            This will automatically generate the citation and the Reference section. 
- **Data set(s)**: Briefly describe the data set(s) you plan to use. 
  Include the URLs to access the data. 
  Typically a single data set is sufficient for this project. 
  It is recommended to use publicly-available data. 
  See the :ref:`Data sources` section below for starting places to look for data. 
      .. attention::
        Regression models are mostly suited for `cross-sectional data <https://en.wikipedia.org/wiki/Cross-sectional_data>`__
        (Think of the data sets we used in the lectures and homework.)
        Do *not* use `time-series data <https://en.wikipedia.org/wiki/Time_series>`__ (e.g., temperature by dates), as the independence assumption in regression models is likely violated.
        For example, today's temperature is highly correlated with (thus not independent to) yesterday's temperature.
- **Method description**: what are the technical plans on how the research questions will be answered 
  (e.g., how you plan to analyze the data? what modeling work to conduct? how to address the research questions based on the results?) 
  We understand that we have not covered some of the modeling methods. 
  Check the :ref:`Schedule` on the remaining lecture topics and describe your methods as best as you can.   
- A brief description of what you have done so far.

You need to submit the PDF file generated from Overleaf to the according Canvas assignment.

One submission per team.

Proposal rubric
^^^^^^^^^^^^^^^

Your proposal will be graded based on each of the following components. 
Under each component are the descriptions for three levels of "Excellent", "Good", and "Poor".

- **Background & data description**
    - **Background and data clearly described**
    - Background and data described but lacking clarity
    - Background and data not described
- **Research questions**
    - **Defined clear and meaningful research questions**
    - Research questions are present but not articulated clearly
    - Did not define any research questions
- **Literature review**
    - **Identified 2+ relevant scientific work and extensive discussion of at least two**
    - Identified and discussed at least two relevant scientific works
    - Did not look into the literature
- **Methods description**
    - **Clear plan on how analysis and modeling would be used to answer research questions**
    - Plan on how to answer question described but lacking clarity
    - No discussion of how analysis and modeling may be used to answer research questions
- **Composition**
    - **The proposal was clearly written, coherent, and well organized**
    - Writing and organization needs improvement
    - Not clear, coherent, or lacks overall organization


Research poster
---------------

Your team will submit a research poster at the end of the project.
There will be two rounds of submission: Round 1 (20% of project grade), final poster (30% of project grade)

Poster requirements
^^^^^^^^^^^^^^^^^^^

- **Poster template**: You are required to use the provided poster template on Overleaf.
- See the template for all the required sections. 
- One submission per team.

Things to keep in mind when working on the poster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Your poster should be different from your JupyterLab in some major ways:
    - The audience of the poster is someone who have general knowledge about statistics, but may not necessarily be familiar with either Python or the data sets you are using.
    - Thus, your poster should not include any codes (leave them in the notebook). Rather, describe things in plain English.
    - You should also avoid using programming jargons (e.g., function names such as ``groupby``), or anything specific to the data set (e.g., variable names such as "co2_level_mi").

Poster rubric
^^^^^^^^^^^^^

.. Your poster will be graded based on each of the following components. 
.. Under each component are the descriptions for three levels of "Excellent", "Good", and "Poor".

- **Subject knowledge**
    - **The poster demonstrated excellent knowledge of the course content and skills by integrating major and minor concepts and methods into the work;
      It also demonstrated evidence of extensive research effort and a depth of thinking about the topic.**
    - The poster demonstrated good knowledge of the course content and skills by integrating major concepts and methods into the work;
      It also demonstrated evidence of limited research effort and/or initial of thinking about the topic.
    - The poster did not demonstrate sufficient knowledge of the course content, skills, evidence of the research effort or depth of thinking about the topic;
- **Correctness**
    - **The methods and discussions (e.g., data analysis, modeling, interpretations of results) were correct and appropriate to answer the research questions.**
    - The methods and discussions were mostly correct with some minor errors.
    - The methods or discussions have major errors.
- **Composition**
    - **The poster was clearly written and well organized;
      The contents are easy to follow and the viewer can easily understand order without narration;
      Sentences were grammatical and free from errors.**
    - The poster was organized and clearly written for the most part;
      Content arrangement is somewhat confusing and does not adequately assist the viewer in understanding order without narration.
      Sentences were mostly grammatical and/or only a few spelling errors were present but they did not hinder the viewer.
    - The poster lacked overall organization;
      Content arrangement is confusing and the viewer has to make considerable effort to understand the order without narration.
      Grammatical and spelling errors made it difficult for the viewer to interpret the text in places.
- **Visual presentation**
    - **Overall visually appealing; not cluttered; 
      Colors and patterns enhance readability; 
      Uses font sizes/variations which facilitate the organization, presentation, and readability of the research;
      Graphics (e.g., tables, figures, etc.) are easy to read and enhance the text.**
    - Visual appeal is adequate; somewhat cluttered; colors and patterns detract from readability;
      Use of font sizes/variations to facilitate the organization, presentation, and readability of the research is somewhat inconsistent/distractions;
      Graphics (e.g., tables, figures, etc.) are somewhat difficult to read or do not adequately enhance the text.
    - Not very visually appealing; 
      Cluttered; 
      Colors and patterns hinder readability;
      Use of font sizes/variations to facilitate the organization, presentation, and readability of the research is inconsistent/distracting;
      Graphics (e.g., tables, figures, etc.) are difficult to read or do not enhance the text.
- **Contribution**
    - **The project offered some new or interesting insights to the topic under discussion;
      Study limitations were discussed in detail.**
    - The methods and discussion were mostly correct with some minor errors;
      Study limitations were briefly discussed.
    - The project offered no insights to the topic under discussion;
      No study limitations were discussed.

Poster checklist
^^^^^^^^^^^^^^^^

Use this checklist to help you to avoid common mistakes when preparing for your poster. 
Note it is not a complete list. 

- **Are the texts in the figures or tables too small to read?** All text should be reasonably legible. 
- **Are the figure axis clearly labeled and with units?**
- **Does the poster include dataset specific names (e.g., "co2_level_mi") or domain/programming-specific jargons?** 
  They should be avoided as general audience may not know what they mean.
- **Does the poster comply with the Honor Code, including avoiding plagiarism?** Have you cited all the work (e.g., text, images) in the poster that were not created by you? 
- **Are all the numbers have clear units?** This is important for the viewer to be able to understand the results. E.g., The RMSE from the model is $123.4 US Dollars. 
- **Are there in-depth discussions on the study limitations?** They should be included.
- **Are the citations correctly used?**. Check the template for an example.


Project poster presentation (20% of project grade)
---------------------------

Your team will present your research poster to the class.
During your presentation, your submitted project poster will be shown on the classroom screen. 
The presentation should include all major parts of your project, including results and discussions.

- The following time allocation should be roughly followed.
    - 1 min: Introduction/background
    - 1 min: Research questions and the methods to answer them.
    - 1 min: Data description
    - 3 min: Results (e.g., data analysis, modeling results, etc.)
    - 1 min: Discussions (the implications of the results, study limitations, etc.)
    - 1 min: Conclusions
- The presentation should be **under 8 minutes**. A one-minute-left reminder will be given to the team.
- In the presentation, each team member should speak for roughly even amount of time (i.e., about 2-3 minutes each).


Presentation rubric
^^^^^^^^^^^^^^^^^^^

.. - **Knowledge**
..     - **The presenters demonstrated sufficient knowledge of the material.**
..     - The presenters demonstrated sufficient knowledge of most of the material but struggled with some.
..     - The presenters struggled with most of the material.
.. - **Presentation**
..     - **The presenters spoke well and established rapport with the audience.**
..     - The presenters spoke well only some of the time. Established limited rapport with the audience.
..     - The presenters did not speak well most of the time and established little rapport with the audience.
.. - **Questions and answers**
..     - **Narration and answering of questions are engaging, thorough, and adds greatly to the presentation.**
..     - Narration and/or answering of questions is somewhat lacking.
..     - Narration and/or answering of questions is lacking.

- **Content**
    - **The presentation demonstrated excellent knowledge of the course content. 
      All major parts of the project were included. 
      The presentation utilized an abundance of materials, including visuals to clearly and effectively communicate the work with the audience.**
    - The presentation demonstrated good knowledge of the course content. 
      All major parts of the project were included. 
      The presentation utilized materials including some visuals to clearly and effectively communicate the work with the audience.
    - The presentation did not demonstrate sufficient knowledge of the course content. 
      Major parts (e.g., results, discussions) were absent. 
      The presentation lacked materials to communicate with the audience.
- **Coherence and organization**
    - **The project was clearly presented. 
      The transitions and flow were easy to follow. 
      The visuals were error-free and logically presented.**
    - The project was mostly clearly presented. 
      The transitions and/or flow were some time difficult to follow. 
      The visuals were mostly error-free and logically presented.
    - The audience had to make considerable effort to understand the underlying logic and flow of ideas. 
      The transitions and flow were not logical. 
      The visuals contained many errors and a lack of logical progression.
- **Presentation skills** (this part is graded individually for each team member.)
    - **The speaker was fluent on the topic and had clear articulation.
      Enthusiasm and confidence were exuded. 
      The speaker made frequent eye-contact with the audience. 
      The materials were presented in a way that held audience attention. 
      The presentation did not exceed the time allotment by more than one minute.**
    - The speaker was mostly fluent on the topic. 
      Light discomfort with public speaking was exuded. 
      The speaker made some eye-contact with the audience. 
      The presentation only somewhat held audience attention. 
      The presentation did not exceed the time allotment by more than one minute.
    - The speaker was not fluent on the topic. 
      A high level of discomfort with public speaking was exuded. 
      The speaker made little eye-contact with the audience or was mostly reading notes.  
      The presentation did not hold audience attention. 
      The presentation went over by more than one minute.


Jupyter notebook & data (20% of project grade)
----------------------------------------------

You are required to submit all the jupyter notebook(s) and data used for the project.

Submission requirements
^^^^^^^^^^^^^^^^^^^^^^^

- You will submit a single ZIP file. 
  When I extract the file, the result should be a directory containing your Jupyter notebook(s) and all other files (e.g., data). 
  The bottom line is I should have all the files needed to reproduce all your results by running your code on my machine.
- Similar to the homework, before submission, make sure that *Kernel* --> *Restart and Run All* runs without errors.
- If your data files are large, it may take time to upload them to Canvas. 
  It is advised to submit the ZIP file at least one hours before the deadline, so you have some buffer time.
- If your data files are larger than 1 GB, contact the instructor at least two academic calendar day before the deadline to arrange alternative ways to submit the data.

Jupyter notebook rubric
^^^^^^^^^^^^^^^^^^^^^^^

- **Correctness**
    - **The implementations of the methods in the codes were correct and appropriate.**
    - The codes were mostly correct with some minor errors.
    - The codes contain major errors or were mostly not appropriate.
- **Research reproducibility**
    - **Complete code, data, and other necessary files were provided so that the instructors are able to reproduce all your work. 
      The codes in the Jupyter notebook were well organized and easy to read. 
      An abundance of clear and informative Markdown cells as well as code comments were used to enhance the notebook's readability**
      (see `Markdown for Jupyter notebooks cheatsheet <https://medium.com/ibm-data-science-experience/markdown-for-jupyter-notebooks-cheatsheet-386c05aeebed>`__).
    - Complete code, data, and other necessary files were provided to reproduce all your work. 
      The codes in the Jupyter notebook were somewhat easy to read. 
      A few Markdown cells and code comments were used with mostly clear information.
    - The submission did not include all files needed to reproduce your work.
      The codes in the Jupyter notebook were difficult to read or lack organization. 
      Almost no Markdown cells or code comments were used to enhance the notebook's readability. 


Peer evaluation form
--------------------

A peer evaluation form will be provided for you to evaluate your peer team members with structured questions (0% of project grade). 
The instructor may adjust an individual's project grades based on the responses at their discretion.
Your response will not be shared with other students. 

*For each person in your team (other than yourself), indicate the extent to which you agree with each of the statements below, using a scale of 1-5 (1=strongly disagree; 2=disagree; 3=neutral; 4=agree; 5=strongly agree).*

- Attended group meetings regularly and contributed meaningfully to group discussions. 				
- Completed group tasks on time and in a quality manner.				
- Demonstrated a cooperative and supportive attitude.				
- Overall, this member contributed significantly to the project.				

Project policies
----------------

Honor Code
^^^^^^^^^^

Before working on your project, make sure to understand the general and project-specific Honor Code on what you are and are not allowed to do. 
They can be found in the course syllabus in the :ref:`Honor Code policies`.

Lateness
^^^^^^^^

- It is recommended to budget enough time for submission. Your team can submit unlimited number of times for a submission. Only the latest submission will be graded.
- For all project submissions (the proposal, progress report, etc.), a late submission (within 24 hours) will receive an automatic 30% point deduction.
- Late submission for more than 24 hours will receive 0 points.
- The late penalties will by default apply to all team members and, in rare cases, may be adjusted at the instructor's discretion.
- The excuses that will not be accepted include, but not limited to,
  - missed the deadline due to last-minute technical or non-technical issues (e.g., network, computer),
  - submitted incomplete or wrong file(s),
  - submitted to a wrong assignment.


Data sources
------------

You can use any data sets of your interest. 
Below are some good starting places to look for data.

- https://datasetsearch.research.google.com
- https://www.data.gov
- https://data.detroitmi.gov
- https://archive.ics.uci.edu/ml/index.php
- http://www.kaggle.com
- Google search "open data portal" + some keywords of your interest. 
  `Click here <https://www.google.com/search?q=%22open+data+portal%22+bicycle>`__ for an example.

Practical advice
----------------

- If you are thinking about including this project to your résumé, keep this in mind from the start (e.g., when selecting the topic and data sets, preparing for the video). 
  We recommend writing down a list of things that you would like to achieve at the end of the project, and working towards them intentionally while doing the project.
- Start early!
- Document as you go the things that you think you would want to include in the deliverables.
- Keep versions of things around: your Jupyter Notebook
    - Explains how you got there
    - In case you have to "go backwards"
    - In case you accidentally delete tons of work
- *Move fast and break things.* 
  `Don't be afraid to make mistakes <https://twitter.com/ThePracticalDev/status/720257210161311744>`__
- *Stay focused and keep shipping.* Build a little, test a little.
- *Done is better than perfect.*

FAQ
---

- Can we change the project topic or data sets after the proposal?
    - Yes. However, please contact the instructors for a discussion before doing so. 


Miscellaneous
-------------

The instructor reserves the rights to make any changes to the project guidelines as deemed necessary.