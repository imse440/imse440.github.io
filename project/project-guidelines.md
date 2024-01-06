<h2 style="text-align: center;"><a href="../">IMSE 440: Applied Statistical Models in Engineering</a></h2>

<h2 style="text-align: center;">Project Guidelines</h2>

<!-- ## Introduction -->

A big part of this course is for you to do a team project. 
This is your opportunity to take what you learned in this class for a spin and try to work on a real-world problem. 

<!-- You need to identify research questions and select data set(s) that are meaningful, reasonably complex (so that you can showcase a variety of things that you've learned), and feasible given the project timeline. 
As a rule of thumb, your project should be significantly more complex than the homework problems and lecture examples. -->

## Team forming

- At the beginning of the semester, you will fill out a course survey in which you are asked to indicate your project topic interests (e.g., transportation, healthcare, etc.)
- You will then be assigned to a multi-disciplinary team of three (3) with similar project topic interests (when possible). 
<!-- - After around the third week, check Canvas for your team assignment.  -->

## General requirements

- For the project you are required to use Python and Jupyter Notebook (the same tools that we use in the class).
<!-- - You are free to include additional analysis or visualization using other software or languages that we do not cover in this course.  -->
- You are free to include data analysis, visualization, and modeling methods that we do not cover in the class However, they should only serve as supplementary components of your project.
<!-- - Do *not* modify the formats (e.g., font size, etc.) of the Overleaf templates.  -->
- To get graded, you need to submit the PDF files generated from Overleaf (see below) to the according Canvas assignments.

## Important dates

- **March 8 (Wednesday) at 6:11 PM**: Project proposal (team)
- **April 5 (Wednesday) at 6:11 PM**: - Project poster (team)
- **April 18 (Tuesday) at 6:11 PM**
    - Final poster (team)
    - Jupyter notebook and data (team)
- **April 19 (Wednesday) at 6:11 PM**: - Project peer review form (individual)
- **Date TBA**
    - Poster exhibition

<!-- Throughout the second half of the semester, there will be four submissions: a project proposal, two project presentations (in pre-recorded videos), and a final report.

- **March 7 (Monday) at 6:11 PM**: Project proposal submission deadline
- **April 18 (Monday) at 6:11 PM**: Video presentation submission deadline
- **April 25 (Monday) at 6:11 PM**: (1) Final video presentation and (2) final report submission deadline -->


---

## Project proposal (10% of project grade)

Your team will decide on our own project topic and find the data that you wish to use.
You are required to submit a project proposal, so we can make sure your selected topic and data set(s) are suitable for the project and you are on the right track.

Your project needs to be
- authentic (e.g., it comes from a *real-world* problem.)
- meaningful (i.e., the outcomes would provide values to others or are something you care deeply about.)
- reasonably complex (so that you can showcase a variety of things you learned from this course with reasonable depth.) 
As a rule of thumb, your project should be significantly more complex than the homework problems.
- feasible given the project timeline. 


### Proposal requirements
- **Proposal template**: You are required to use the proposal template on Overleaf (which will be provided to you later).
    - [Overleaf](https://overleaf.com/) is an online collaborative [LaTeX](https://en.wikipedia.org/wiki/LaTeX) editor for scientific writing. 
    - If you do not already have an Overleaf account, you will need to register for one. 
    The *free* plan is good enough.
    When register, use your UMICH email. 
    - Note we expect *all* team members to use Overleaf as a collaberative tool (think of a Google Docs) when drafting the proposal.
    - You will need to learn some basic LaTeX yourself and with your team using online resources. Here are two good starting points:
        - [The Overleaf LaTex Tutorials](https://www.overleaf.com/learn/latex/Tutorials)
        - [How to write a thesis using LaTeX full tutorial (YouTube video)](https://www.youtube.com/watch?v=zqQM66uAig0) 
    - Note you just need a few basic things to get started.
    Learn more as you prepare for the proposal. 
    - Tips: *Recompile* often, so that if there is a compile error, it's easier to track it down. 


- The proposal should be no more than two (2) pages (not including the cover page and the References section). 
  It should include the following
    - **Project tentative title**
    - **Background**: A brief description of the background of the problem
    - **Research questions**: What do you want to figure out?
    - **Literature review**: What has been done by others regarding the research questions? Report on at least two (2) relevant scientific articles.
    - **Data set(s)**: Briefly describe the data set(s) you plan to use.
        Include the URLs to access the data. 
        Typically a single data set is sufficient for this project.
        It is recommended to use publicly-available data.
        See the Data Sources section below (near the bottom of this document) for starting places to look for data. 
    - **Method description**: what are the technical plans on how the research questions will be answered 
        (e.g., how you plan to analyze the data? what modeling work to conduct? 
        how to address the research questions based on the results?)
        Note I understand that we have not covered some of the modeling methods. See the [scheduled course topics](../) for more information. Describe your methods as best as you can.   
    - (Optional) A brief description of what you have done so far.

- You need to submit the PDF file generated from Overleaf to the according Canvas assignment.
- One submission per team.

Note if you plan to use regression models in your project, they are mostly suited for [cross-sectional data](https://en.wikipedia.org/wiki/Cross-sectional_data)
(Think of the data sets we used in the lectures and homework.)
Cross-sectional data are what you should use for your project.
Do *not* use [time-series data](https://en.wikipedia.org/wiki/Time_series) (e.g., outdoor temperature by dates), as the independence assumption in regression models is likely violated (e.g., today's temperature is highly correlated with (thus not independent to) yesterday's temperature.) 

### Proposal grading rubric

Each component listed below will be graded. 
Under each component are the descriptions for three levels of "Excellent", "Good", and "Poor".

- **Background & data description**
    - Background and data clearly described
    - Background and data described but lacking clarity
    - Background and data not described
- **Research questions**
    - Defined clear and meaningful research questions
    - Research questions are present but not articulated clearly
    - Did not define any research questions
- **Literature review**
    - Identified more than two relevant scientific work and extensive discussion of at least two
    - Identified and discussed at least two relevant scientific works
    - Did not look into the literature
- **Methods description**
    - Clear plan on how analysis and modeling would be used to answer research questions
    - Plan on how to answer question described but lacking clarity
    - No discussion of how analysis and modeling may be used to answer research questions
- **Composition**
    - The proposal was clearly written, coherent, and well organized.
    - Writing and organization needs improvement
    - Not clear, coherent, or lacks overall organization.

<!-- ---
## Progress report (10% of project grade)

To make sure your team are making satisfactory progress, your are required to submit a project progress report.

### Progress report requirements
- **Template**: You are required to use the progress report template on Overleaf (which will be provided to you later).
- In the progress report, describe what your team has already completed and the remaining work plan. See the template for the required sections. 
- The progress report should be around three (3) pages (not including the cover page and the References section).
- One submission per team.

### Progress report grading rubric

- **Project progress**
    - The project has made significant progress since the proposal.
    - The project has made some, but not significant progress since the proposal.
    - The project has made little to no progress since the proposal.
- **Composition**
    - The report was clearly written, coherent, and well organized.
    - Writing and organization needs improvement
    - Not clear, coherent, or lacks overall organization.

--- -->

<!-- ## Video presentation (20% of project grade)

Near the completion of the course, your team will submit a video presentation of your project.
The presentation should include all major parts of your project, with a focus on the *results*. 

- The following time allocation should be roughly followed.
    - 1 min: Introduction/background
    - 1 min: Research questions and the methods to answer them:
    - 2 min: Data description
    - 8 min: Results (e.g., data analysis, modeling results, etc.)
    - 2 min: Discussions (the implications of the results, study limitations, etc.)
    - 1 min: Conclusions
- The video should be **under 15 minutes**.
- In the presentation, each team member should speak for roughly even amount of time (i.e., about 5 minutes each).
- To record your presentation you are free to use any recording software that you are comfortable with, for example, a recorded Zoom meeting. 
- The video file should be in one of the following format: MP4 (preferred), MOV, WMV, and AVI.
- One submission per team.
### Video presentation rubric

- **Content**
    - The presentation demonstrated excellent knowledge of the course content. 
        All major parts of the project were included with a focus on the data analysis methods/results and discussion. 
        The presentation utilized an abundance of materials, including visuals or diagrams to clearly and effectively communicate the work with the audience.
    - The presentation demonstrated good knowledge of the course content. 
        All major parts of the project were included. 
        The presentation utilized materials including some visuals or diagrams to clearly and effectively communicate the work with the audience.
    - The presentation did not demonstrate sufficient knowledge of the course content. 
        Major parts (e.g., results, discussions) were absent. 
        The presentation lacked materials to communicate with the audience.
- **Coherence and organization**
    - The project was clearly presented. 
        The transitions and flow were easy to follow. 
        The slides were error-free and logically presented.
    - The project was mostly clearly presented. 
        The transitions and/or flow were some time difficult to follow. 
        The slides were mostly error-free and logically presented.
    - The audience had to make considerable effort to understand the underlying logic and flow of ideas. 
        The transitions and flow were not logical. 
        The slides contained many errors and a lack of logical progression.
- **Presentation skills**
    - The speaker was fluent on the topic and had clear articulation.
        Enthusiasm and confidence were exuded. 
        The materials were presented in a way that held audience attention. 
        The presentation did not exceed the time allotment.
    - The speaker was mostly fluent on the topic. 
        Light discomfort with public speaking was exuded. 
        The presentation only somewhat held audience attention. 
        The presentation went over by less than one (1) minute.
    - The speaker was not fluent on the topic. 
        A high level of discomfort with public speaking was exuded. 
        The presentation did not hold audience attention. 
        The presentation went over by more than one (1) minute. -->

---
## Research poster: round 1 (20% of project grade), round 2 (40% of project grade)

You are required to submit a research poster in two rounds.

### Poster requirements
- **Poster template**: You are required to use the poster template on Overleaf (it will be provided).
- See the template for all the required sections. 
- One submission per team.

### Things to keep in mind when working on the poster

Your poster should be different from your Jupyter notebook in some major ways:

- The audience of the poster is someone who have general knowledge about statistics and machine learning, 
    but may not necessarily know anything about Python, and they may not be familiar with the data sets you are using.
- Thus, your poster should not include any codes (leave them in the notebook). 
    Rather, describe things in plain English.
- You should also avoid using programing jargons (e.g., function names such as `groupby`), 
    or anything specific to the data set (e.g., column names such as "co2_level_mi").

### Poster rubric

- **Subject knowledge**
    - The poster demonstrated excellent knowledge of the course content and technical skills by integrating major and minor concepts and methods into the work. 
      The poster also demonstrated evidence of extensive research effort and a depth of thinking about the topic.
    - The poster demonstrated good knowledge of the course content and technical skills by integrating major concepts and methods into the work. 
      The poster also demonstrated evidence of limited research effort and/or initial of thinking about the topic.
    - The poster did not demonstrate sufficient knowledge of the course content, technical skills, evidence of the research effort or depth of thinking about the topic.
- **Correctness**
    - The methods and discussions (e.g., data analysis, modeling, interpretations of results) were correct and appropriate to answer the research questions.
    - The methods and discussion were mostly correct with some minor errors.
    - The methods or discussion were incorrect or not appropriate to answer the research questions.
- **Composition**
    - The poster was clearly written and well organized. 
        The underlying logic was clearly articulated and easy to follow.
        Sentences were grammatical and free from errors.
    - The poster was organized and clearly written for the most part.
        In some areas the logic and/or flow if ideas were difficult to follow. 
        Sentences were mostly grammatical and/or only a few spelling errors were present but they did not hinder the reader.
    - The poster lacked overall organization. 
        The reader had to make considerable effort to understand the underlying logic and flow of ideas. 
        Grammatical and spelling errors made it difficult for the reader to interpret the text in places.
- **Contribution**
    - The project offered some new or interesting insights to the topic under discussion. 
        Study limitations were discussed in detail.
    - The methods and discussion were mostly correct with some minor errors. 
        Study limitations were briefly discussed.
    - The project offered no insights to the topic under discussion. 
        No study limitations were discussed.

### Poster checklist (not a complete list)
- **Are the texts in the figures or tables too small to read?** All text should be reasonably legible. The texts in figures and tables should not be much smaller than the text in the main texts.
- **Are the figure axis clearly labled and with units?**
- **Does the poster include dataset specific names (e.g., "co2_level_mi") or domain/programming-specific jargons?** They should be avoided as general audiance may not know what they mean.
- **Does the poster comply with the Honor Code, including avoiding plagiarism?** 
- **Are all the numbers have clear units?** E.g., The RMSE from the model is $123.4 US Dollars. 
- **Are there in-depth discussions on the study limitations?** They should be included.
- **Are the citations correctly used?**. Check the template for an example.

---
## Jupyter notebook & data (30% of project grade)

You are required to submit all the jupyter notebook(s) and data used for the project. 

### Submission requirements

- You will submit a single ZIP file. 
    When I extract the file, the result should be a directory containing your Jupyter notebook(s) and all other files (e.g., data files). The bottom line is I should have all the files needed to reproduce all your results by running your code on my machine.
- Similar to the homework, before submission, make sure that *Kernel* --> *Restart and Run All* runs without errors.
- If your data files are large, it may take time to upload them to Canvas. 
    It is advised to submit the ZIP file at least one hours before the deadline, so you have some buffer time.
- If your data files are larger than 1 GB, contact the instructor at least two (2) academic calendar day before the deadline to arrange alternative ways to submit the data.

### Jupyter notebook rubric

- **Correctness**
    - The implementations of the methods in the codes were correct and appropriate.
    - The codes were mostly correct with some minor errors.
    - The codes contain major errors or were mostly not appropriate.
- **Research reproducibility**
    - Complete code, data, and other necessary files were provided so that the instructors are able to reproduce all your work. 
        The codes in the Jupyter notebook were well organized and easy to read. 
        An abundance of clear and informative Markdown cells as well as code comments were used to enhance the notebook's readability (see [Markdown for Jupyter notebooks cheatsheet](https://medium.com/ibm-data-science-experience/markdown-for-jupyter-notebooks-cheatsheet-386c05aeebed)).
    - Complete code, data, and other necessary files were provided so that the instructors are able to reproduce all your work. 
        The codes in the Jupyter notebook were somewhat easy to read. 
    A few Markdown cells and code comments were used with mostly clear information.
    - The submission did not include all files needed for the instructors to reproduce your work. 
        The codes in the Jupyter notebook were difficult to read or lack organization.
        Almost no Markdown cells or code comments were used to enhance the notebook's readability. 


---
## Peer evaluation form (0% of project grade)

A peer evaluation form will be provided for you to evaluate your peer members in your team with structured questions. 
Your response will not be shared with any other students. 

*For each person in your team (other than yourself), indicate the extent to which you agree with each of the statements below, using a scale of 1-5 (1=strongly disagree; 2=disagree; 3=neutral; 4=agree; 5=strongly agree).*

- Attended group meetings regularly and contributed meaningfully to group discussions. 				
- Completed group tasks on time and in a quality manner.				
- Demonstrated a cooperative and supportive attitude.				
- Overall, this member contributed significantly to the project.				


---
## Policies

### Honor Code

- Before working on your project, make sure to understand the general and project-specific Honor Code on what you are and are not allowed to do. 
    They can be found in the [course syllabus](../syllabus) in the Honor Code section.

### Lateness

- For *all* project submissions (the proposal, progress report, etc.), a late submission (within 24 hours) will receive an automatic 30% point deduction.
- Late submission for more than 24 hours will receive 0 points.
- The late penalties will by default apply to all team members and, in rare cases, may be adjusted at the instructor's discretion.

## Data sources

You can use any data sets of your interest. Below are some good starting places to look for data.
- <https://datasetsearch.research.google.com>
- <https://www.data.gov>
- <https://data.detroitmi.gov>
- <https://archive.ics.uci.edu/ml/index.php>
- <http://www.kaggle.com>
- Google search "open data portal" + some keywords of your interest.
[Click here](https://www.google.com/search?q=%22open+data+portal%22+bicycle) for an example.

## Practical advice

- If you are thinking about including this project to your résumé, keep this in mind from the start 
(e.g., when selecting the topic and data sets, preparing for the video). 
We recommend writing down a list of things that you would like to achieve at the end of the project, and working towards them intentionally while doing the project.
- Start early!
- Document as you go the things that you think you would want to include in the deliverables.
- Keep versions of things around: your Jupyter Notebook
    - Explains how you got there
    - In case you have to "go backwards"
    - In case you accidentally delete tons of work
- *Move fast and break things.* [Don't be afraid to make mistakes.](https://twitter.com/ThePracticalDev/status/720257210161311744)
- *Stay focused and keep shipping.* Build a little, test a little.
- *Done is better than perfect.*

## FAQ

- Is it ok that my video is longer than 15 minutes?
    - See the Presentation Rubric --> "Presentation skills" above for details.

---

<br>