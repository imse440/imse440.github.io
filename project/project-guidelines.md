<h2 style="text-align: center;"><a href="../">IMSE 440: Applied Statistical Models in Engineering</a></h2>

<h2 style="text-align: center;">Project Guidelines</h2>

## Introduction

Part of our course activities is for you to do a project. 
This is your opportunity to take what you learned in this class for a spin and try to get some insights into a real-world problem of your interest. 
You will decide on your own project topic and find the data that you want to use.

You need to identify research questions and select data set(s) that are meaningful, reasonably complex (so that you can showcase a variety of things that you've learned), and feasible given the project timeline. 
As a rule of thumb, your project should be significantly more complex than the homework problems and lecture examples.

## General requirements

- You are required to use Python and Jupyter Notebook for this project.
- You are free to include data analysis and modeling methods that we do not cover in the class. However, they should only serve as supplementary components of your project.

## Important dates

Throughout the second half of the semester, there will be four submissions: a project proposal, two project presentations (in pre-recorded videos), and a final report.

- **March 7 (Monday) at 6:11 PM**: Project proposal submission deadline
- **April 11 (Monday) at 6:11 PM**: Video presentation submission deadline
- **April 22 (Monday) at 6:11 PM**: (1) Final video presentation and (2) final report submission deadline

## Project proposal (10% of project grade)

- You are required to submit a project proposal (in PDF). 
The goal of the proposal is to make sure you select a topic and data set(s) that are suitable for the project and you are on the right track.
- The proposal should be about two pages. It should include the following
    - **Project tentative title**
    - **Background**: A brief description of the background of the problem
    - **Research questions**: What do you want to figure out?
    - **Literature review**: What has been done by others regarding the research questions? Report on at least two relevant references.
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
- Your proposal may serve as part of your final report later on.
- If for any reason you are considering making major changes to your project topic and/or data sets after the proposal submission, consult with the instructor as early as possible.

Note regression models are mostly suited for [cross-sectional data](https://en.wikipedia.org/wiki/Cross-sectional_data). 
Think of the data sets we used in the lectures and homework. 
Cross-sectional data are what you should use for your project.
Do *not* use [time-series data](https://en.wikipedia.org/wiki/Time_series) (.e.g, outdoor temperature by dates), as the independence assumption in regression models is likely violated (e.g., today's temperature is highly correlated with (thus not independent to) yesterday's temperature.) 

### Proposal grading rubric

Each component listed below will be graded. 
Under each component are the descriptions for three levels of "Excellent",
"Good", and "Poor".

- **Background & data description**
    - Background and data clearly described
    - Background and data described but lacking clarity
    - Background and data not described
- **Research questions**
    - Defined clear and meaningful research questions
    - Research questions are present but not articulated clearly
    - Did not define any research questions
- **Literature review**
    - Identified more than two relevant works or extensive discussion of at least two
    - Identified and discussed at least two relevant works
    - Did not look into the literature
- **Methods description**
    - A clear plan on how analysis and modeling would be used to answer research questions
    - Plan on how to answer questions described but lacking clarity
    - No discussion of how analysis and modeling may be used to answer research questions
- **Composition**
    - The proposal was clearly written, coherent, and well organized.
    - Writing and organization needs improvement
    - Not clear, coherent, or lacks overall organization.

## Project presentation (20% of project grade)

-   You are required to submit a video of you presenting your project.
    The video should be **under 10 minutes**.
-   The presentation should include *all major parts of your project, with a focus on the results*.
    The following time allocation should be roughly followed.
    - 1 min: Introduction/background
    - 1 min: Research questions and the methods to answer them:
    - 1 min: Data description
    - 5 min: Data analysis, modeling, and results
    - 1 min: Discussions and conclusions
-   To record your presentation you are free to use whatever recording software that you are comfortable with. 
    If you are not familiar with the tools, we recommend the free and open-source software [OBS Studio](https://obsproject.com). 
    It is fairly easy to use, but do make sure to budget some time to learn the basics.
- The video file should be in one of the following formats: MP4 (preferred), MOV, WMV, and AVI.

### Things to keep in mind when preparing for the presentation (and the final report)

- The audience of the project presentation and final report is someone who has general knowledge about statistics, regression, and machine learning, 
    but may not necessarily know anything about Python, and they may not be familiar with the data sets that you are using.
- Thus, your presentation and report should generally not include any codes (leave them in the Jupyter notebook as part of the final submission).
- You should also avoid using programming jargons (e.g., "dataframe" or any function names such as `groupby`), 
    or any dataset-specific terms (e.g., "co2_level_mi").
    Rather, describe things in plain English.

### Presentation self-checklist

- Are the texts in the visuals (e.g., figures, tables, slides) easy for the audience to read? 
    If not, use larger fonts and better text/background colors.
- Am I just reading the texts in the slides? Generally, do not putting long sentences in your slides. Rather, use keywords, charts, tables. They are much easier for the audience to read and understand.
- Are all the axis in the charts labeled? Are the units of the measurement clear to the audience?
- Are all the images and text not created by me clearly cited? 

### Presentation rubric

- **Content**
    - The presentation demonstrated excellent knowledge of the course content. 
        All major parts of the project were included with a focus on the data analysis methods/results and discussion. 
        The presentation utilized an abundance of materials, including visuals or diagrams to clearly and effectively communicate the work with the audience.
    - The presentation demonstrated good knowledge of the course content. 
        All major parts of the project were included. 
        The presentation utilized materials including some visuals or diagrams to clearly and effectively communicate the work with the audience.
    - The presentation did not demonstrate sufficient knowledge of the course content. 
        Major parts (e.g., results) were absent. 
        The presentation lacked materials to communicate with the audience.
- **Coherence and organization**
    - The project was clearly presented. 
        The transitions and flow were easy to follow. 
        The slides were error-free and logically presented.
    - The project was mostly clearly presented. 
        The transitions and/or flow were sometimes difficult to follow. 
        The slides were mostly error-free and logically presented.
    - The audience had to make a considerable effort to understand the underlying logic and flow of ideas. 
        The transitions and flow were not logical. 
        The slides contained many errors and a lack of logical progression.
- **Presentation skills**
    - The speaker was fluent on the topic and had clear articulation.
        Enthusiasm and confidence were exuded. 
        The materials were presented in a way that held audience's attention. 
        The presentation fit into the time allotment.
    - The speaker was mostly fluent on the topic. 
        Light discomfort with public speaking was exuded. 
        The presentation only somewhat held audience's attention. 
        The presentation went over by less than 3 minutes.
    - The speaker was not fluent on the topic. 
        A high level of discomfort with public speaking was exuded. 
        The presentation did not hold audience's attention. 
        The presentation went over by more than 3 minutes.

## Final project presentation (20% of project grade)

After you submit your first presentation, the instructor will provide feedback on your project, so that you can make improvements on your final presentation and report.

The final presentation will be graded using the same rubric as the preliminary presentation described above.
## Final report (50% of project grade)

You are required to submit a final report of your project, which should include the following sections.

- Project title
- Abstract (a self-contained, short summary of your project, 250 words or less)
- Introduction (e.g., background, motivations)
- Research questions
- Methods
    - A description of the data and access to the data (i.e., how one
        can gain access to the data)
    - A detailed description of your data treatment, analysis, and
        modeling workflow. Data treatment could include data cleaning,
        treating missing data, and other steps taken.
- Results (e.g., modeling work)
- Discussions
    - How the research questions were answered
    - Any practical implications based on the findings
    - Study limitations
    - Any interesting insights (optional)
- Conclusions
- References
- Appendix (if needed)


### Final report submission requirements

- You will submit a single ZIP file. 
    When I extract the file, the result should be a directory containing, at the minimum, your report (.PDF), Jupyter notebooks (.ipynb), and all other files (e.g., data files) that are needed to run your code.
- I should be able to reproduce all your results by running your code on my machine.
- Before submission, make sure that *Kernel* --> *Restart and Run All* runs without errors.
- If your data files are large, it may take time to upload them to Canvas. 
    It is advised to submit your report at least two hours before the deadline, so you have some buffer time.
- If your data files are larger than 1 GB, contact the instructor at least two (2) academic calendar days before the deadline to arrange alternative ways to submit the data.

### Final report rubric

- **Subject knowledge**
    - The report demonstrated excellent knowledge of the course content and technical skills by integrating major and minor concepts and methods into the work. 
      The report also demonstrated evidence of extensive research effort and a depth of thinking about the topic.
    - The report demonstrated good knowledge of the course content and technical skills by integrating major concepts and methods into the work. 
      The report also demonstrated evidence of limited research effort and/or initial thinking about the topic.
    - The report did not demonstrate sufficient knowledge of the course content, technical skills, evidence of the research effort, or depth of thinking about the topic.
- **Correctness**
    - The methods and discussions (e.g., data analysis, modeling, interpretations of results) were correct and appropriate to
        answer the research questions.
    - The methods and discussion were mostly correct with some minor errors.
    - The methods or discussion were incorrect or not appropriate to answer the research questions.
- **Research reproducibility**
    - Complete code, data, and other necessary files were provided so that I'm able to reproduce all your work. 
        The codes in the Jupyter notebook were well organized and easy to read. 
        An abundance of Markdown cells was used to enhance the notebook's readability (see [Markdown for Jupyter notebooks cheatsheet](https://medium.com/ibm-data-science-experience/markdown-for-jupyter-notebooks-cheatsheet-386c05aeebed)).
    - Complete code, data, and other necessary files were provided so that I'm able to reproduce all your work. 
        The codes in the Jupyter notebook were somewhat easy to read. 
    A few Markdown cells were used.
    - The submission did not include all files needed for others to reproduce your work. 
        The codes in the Jupyter notebook were difficult to read or lack organization.
- **Composition**
    - The report was clearly written and well organized. 
        The underlying logic was clearly articulated and easy to follow.
        Sentences were grammatical and free from errors.
    - The report was organized and clearly written for the most part.
        In some areas the logic and/or flow if ideas were difficult to follow. 
        Sentences were mostly grammatical and/or only a few spelling errors were present but they did not hinder the reader.
    - The report lacked overall organization. 
        The reader had to make a considerable effort to understand the underlying logic and flow of ideas. 
        Grammatical and spelling errors made it difficult for the reader to interpret the text in places.
- **Contribution**
    - The report offered some new or interesting insights into the topic under discussion. 
        Study limitations were discussed in detail for others who may want to use the results.
    - The methods and discussion were mostly correct with some minor errors. 
        Study limitations were discussed.
    - The report offered no insights into the topic under discussion. 
        No study limitations were discussed.

## Policies

### Honor Code

- Before working on your project, make sure to read and understand the general and project-specific Honor Code on what you are and are not allowed to do. 
    They can be found in the [course syllabus](../syllabus) in the Honor Code section.

### Lateness

- For all project submissions (the proposal, presentation, and report), a late submission (within 24 hours) will receive an automatic 30% point deduction.
- Late submission for more than 24 hours will receive 0 points.


<!-- - 🎈**IMSE 440 Expo**🎈 (COVID-pending event, date TBD):
To showcase what you accomplished in this course, we *may* host an expo for you to present your project. 
The event will be open to all. 
Your participation is encouraged.
However, you can opt out if you do not wish to participate for any reason, and it will not affect your grade in any way. -->
<!-- - **April 21 (Tuesday) starting at noon **: 🎈**IMSE 440 Expo**🎈 
To showcase what you accomplished in this course, we will host a Zoom Expo that streams the videos that you and your fellow classmates submitted. 
This event will be advertised to our College and open to the public.

 -->


## Data sources

You can use any data set(s) of your interest. Below are some good starting places to look for data.
- <https://datasetsearch.research.google.com>
- <https://www.data.gov>
- <https://data.detroitmi.gov>
- <https://archive.ics.uci.edu/ml/index.php>
- <http://www.kaggle.com>
- Google search "open data portal" + some keywords of your interest.
[Click here](https://www.google.com/search?q=%22open+data+portal%22+bicycle) for an example.

## Practical advice

- If you are thinking about including this project in your résumé, keep this in mind from the start 
(e.g., when selecting the topic and data sets, preparing for the video). 
We recommend writing down a list of things that you would like to achieve at the end of the project and working towards them intentionally while doing the project.
- Start early!
- Document as you go the things that you think you would want to include in the final report.
- Keep versions of things around: your Jupyter Notebook
    - Explains how you got there
    - In case you have to "go backwards"
    - In case you accidentally delete tons of work
- *Move fast and break things.* [Don't be afraid to make mistakes.](https://twitter.com/ThePracticalDev/status/720257210161311744)
- *Stay focused and keep shipping.* Build a little, test a little.
- *Done is better than perfect.*

## FAQ

- Is it ok my video is longer than 10 minutes?
    - See the Presentation Rubric --> "Presentation skills" above for details.
- Are there format requirements for the final report?
    - No
- Are there requirements or limits on how many pages the final report should be?
    - No
- Why is it an individual project instead of a team project like in some of my other classes?
    - This is an introductory data science course and we want you to have an opportunity to practice *all* essential components and steps of an end-to-end data science project from data processing, visualization, exploratory data analysis, to modeling and reporting.
