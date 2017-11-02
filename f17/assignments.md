# Homework Projects

All homework must be completed in pairs only. You may discuss the problems with other groups. If you discuss the problems with another group, you must **cite** them (following the [collaboration policy](index.html#collaboration)).

Homework solutions should be submitted by 6:00 p.m. on the due date (with an automatic twenty-four hour extension). Early submissions are welcome.

## Homework Assignment 6

**Due Friday, November 17, 2017**

* Complete the exercises in Chapter 6 resulting in a P3 compiler.

## Homework Assignment 5

**Due Friday, November 3, 2017**

* Complete the exercises in Chapter 5 resulting in a P2 compiler.

## Homework Assignment 4

**Due Friday, October 13, 2017**

* Complete the exercises in Chapter 4 resulting in a P1 compiler.

## Homework Assignment 3
  
**Due Friday, September 29, 2017**

* Complete the exercises in Chapter 3 resulting in a register allocator for your P0 compiler.
* Get started early, as you have to think carefully about several parts.
* You might want to start by refactoring your code to use an x86-like IL before code generation if you haven't already.

## Homework Assignment  2
  
**Due Tuesday, September 19, 2017**

* Complete the exercises in Chapter 2 resulting in a parser for P0 to add to your P0 compiler.

## Homework Assignment 1
  
**Due Friday, September 8, 2017**

* Complete the exercises in Chapter 1 resulting in a compiler for P0 and tests for your compiler.
* You can upload your tests and compiler as many times as you want. Each time you submit your compiler, it will be tested against the grading benchmarks.
*  **Stress Testing for Extra Credit**. You will receive extra credit if you are the one who breaks the most compilers produced by your classmates (and more than 0). Note that your tests must satisfy the input constraints to qualify, that is, they must be P0 programs (e.g., a test case that triggers integer overflow does not count). Your own compiler must also pass your test cases to qualify.

# Class Participation and Online Discussion

It is important to attend class and read the readings. Lively class discussion is also important, which includes in-class participation, as well as participation in the online forums.

Students are expected to be active participants in the online forums (e.g., around at least 1 substantive post per week). You may and are encouraged to post comments or questions about the reading before the class where we will cover it. Posting early will help focus our discussion.

Here are some examples of good comments:

*   Questions about the reading or the class discussion.
*   Thoughtful answers to other people's questions.
*   Clarification of some point discussed in class.
*   What you think is the main point or key idea in the reading set.
*   An idea of how some work could be improved from the reading or class discussion.

If everything from a class meeting seems clear to you, try to come up with a question that tests your classmates' understanding. Put yourself in the position of an instructor!

Overall, the intent is for you to to take a moment to reflect upon the day's reading or class discussion. I will read all posts, but I may not respond to all of them (e.g., if I believe your classmates' answers are sufficient).

# Final Project

## Project Guidelines

Students are expected to select and complete a substantial course project during the semester on a topic related to the class.

Projects should be done in groups of three to four (other group compositions must be discussed on a case-by-case basis). The expectations will naturally depend on the number of group members. These groups can be different than your pair programming groups during the semester. For the final project, a group should consist of all undergraduate students or all graduate students (unless you get special permission from the instructor).

The first step is to submit a _project proposal_. The proposal should explain what you expect to learn from the project (i.e., why is it interesting to you?) and should include a work schedule. Make sure to budget time for writing a short _project paper_ (~5 pages) describing the project and for preparing a short (~15-20 minutes, depends on number of projects) _project presentation_ during the last week of classes. The main purpose of the proposal is for me to give you feedback on its feasibility.

The main goal of the project is to allow you to customize the content of the course to your own interests. The goal is not to force you all to produce novel results in one semester. Course projects like this often lead to collaborations that eventually yield exciting research. In the hopefully-likely event that you end up enjoying your project, come see me about taking it further (say, to publication).

The expectations for a graduate-level project will be differentiated from an undergraduate-level project.

## Project Dates

* A pre-proposal is due on Friday, October 27, 2017.
* The project proposal is due on Friday, November 3, 2017.
* A project status update is due on Friday, November 17, 2017.
* Project presentations will be held during the last week of classes.
* The project paper is due on Sunday, December 17, 2017.
* Peer reviews on project papers are due on Monday, December 18, 2017.

## Project Scale

I do not expect each project to lead to novel results, though I hope some projects could eventually lead to publication!

* I do expect a consistent effort on the project. Once we stop having weekly homework assignments, that amount of time should be entirely directed towards your project.
* Notably, "one long weekend" will _not_ suffice. I can tell. Trust me.
* You are welcome to tackle a more ambitious project. Such a project should have "stages" so that you have something to show at the end of the semester. I (or your advisor) can provide extra guidance on such projects.
* The number of group members should depend on the size of the project. Note that the grading for a two-person project will actually require "twice as much work" than a one-person project rather than the standard "1.5-times as much work". You should be able to split up the project paper (e.g., "I did section 1, Grace Hopper did section 2, and we shared section 3").

## Project Kinds

Projects on any subject related to the class are acceptable. The goal is to allow you to customize the project to your interests. There are two main types of projects: implementation projects and research projects.

Undergraduate students may undertake implementation projects but are free to pursue research projects. Graduate students must aim for a research project.

### Implementation Projects

Pick a fragment of a language or a relevant algorithm, and implement it! There is no firm limit on the amount of code.

The most straightforward implementation project is to extend your compilers. Two clear options are (a) to extend the input language you compile or (b) to implement optimizations. For all of those attempting optimizing compilers, we will arrange to have a competition.

An implementation project should feature "numbers": controlled, experimental results that help to sway your audience in favor of a point you are making. You should actually have a point: "I implemented a register allocator" is not quite good enough. You will want something more like: "Graph-coloring register allocation yields fewer spills and thus smaller and faster code than greedy register allocation. On the X benchmarks for the Y architecture, replacing a greedy register allocator in the Z compiler with a graph-coloring one resulting in a A% decrease in code size and a B% decrease in average executing time."

Your implementation can be anything relevant to language implementation or analysis. It could also be relevant to language design provided that it close enough to the course content. Implementing register allocation doesn't actually cut it.

### Research Projects

There are many kinds of research projects, including the following:

* Design and implement a program analysis
* Invent a language or a language feature for some particular purpose or with some particular characteristic (e.g., to make program analysis and understanding more tractable) and find a way to compile it.
* Explore novel techniques for implementing a given language fragment

These projects are harder because they always involve some survey work and some implementation. If you want to do a research project, and you are not yet sufficiently familiar with the area of the project, you should start with some concrete implementation tasks and then turn it into a research project. While research is necessarily open-ended, be sure that you have a well-defined goal for the end of the semester so that you have something to write up and present.

## The Proposal

Your proposal should address at least the following questions:

1.  Who are the members of your team?
2.  What basic problem will your project try to solve?
3.  Define the problem that you will solve as concretely as possible. Provide a scope of expected and potential results. Give a few example programs that exhibit the problem that you are trying to solve.
4.  What is the general approach that you intend to use to solve the problem?
5.  Why do you think that approach will solve the problem? What resources (papers, book chapters, etc.) do you plan to base your solution on? Is there one in particular that you plan to follow? What about your solution will be similar? What will be diﬀerent?
6.  How do you plan to demonstrate your idea? Will you use your course compiler. If so, what specific changes do you plan to make to it (e.g., what passes need to be changed or added)?
7.  How will you evaluate your idea? What will be the measurement for success?

Your proposal should be concise and specific. Do not be long-winded or vague. You will not be graded on the length of the proposal, but you will be graded on how many interesting things you say.

Your _pre-proposal_ should consist of answers to at least the first two questions. The purpose of the pre-proposal is to help you get started thinking about your project and discussing with me as needed.

## The Status Update

The status update is a short write-up. It should explain what you have done so far and how you plan to meet your goals in the final weeks of the project. Like your proposal, you will not be graded on the length of your status update but rather on how concrete you are on where you are.

## The Presentation

The presentation should be short and should describe what the problem was, what the difficulties were, and what was accomplished or learned. You will find it much easier to prepare the talk using slides (perhaps 8 to 12 slides, depending on your speed).

While preparing the talk keep in mind who your audience is. You will be presenting to colleagues who are eager to find out (1) about new exciting facets of compilation and (2) how much fun you had. Plan to motivate the project (i.e., why is this important?) and to describe what you learned from it. Keep in mind that your colleagues have not read all the papers that you have read to do the project.

Project presentations will be held on the final week of classes. Students presenting on Tuesday will receive a small amount of extra credit to make up for presenting earlier.

## The Paper

Your write up at the end of the semester should be in the form of a short research paper. The project paper should have an abstract and an introduction describing the tackled problem, its motivation, and a very brief summary of the accomplishment. Then you should write a description of your notations (especially if they are different from what we used in class). Then you continue with the body of the material. The paper should end with a conclusion putting in perspective the accomplishment of the project and mentioning the open problems and with a bibliography of cited papers. Research papers should also have a related work section in which they compare the work with previous research results.

You might want to browse the papers from [PLDI 2016](http://www.informatik.uni-trier.de/~ley/db/conf/pldi/pldi2016.html) or [POPL 2017](http://informatik.uni-trier.de/~ley/db/conf/popl/popl2017.html). Aside from giving you a number of data points for how the paper should look graphically, reading the electronic editions might help you to find a topic. Extending previously-published work is often not a bad start.

Your project paper should be ~5 pages, as necessary, while being as concise and concrete as possible. Like your proposal, you will not be graded on length but on how many interesting things you say. You will turn in a PDF _as well as your implementation code_. You will want to use the [LaTeX class file](http://www.sigplan.org/authorInformation.htm) produced by ACM/SIGPLAN. Please use the two-column format.

## Peer Review

You will have the opportunity to write reviews of your peers' project papers _for extra credit_. Take a look at the [Paper Review Form](assignments/paper-review.txt) for further details.
