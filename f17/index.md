# Fall 2017

Class meetings are Tuesdays and Thursdays 9:30-10:45 in ECCS 1B28.

Please check the following calendar for the latest information about office hours and potentially review and help sessions.
<iframe src="https://calendar.google.com/calendar/embed?showCalendars=0&amp;mode=WEEK&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=colorado.edu_j87qtg7ug60hp0q92lnv85tmtg%40group.calendar.google.com&amp;color=%23182C57&amp;ctz=America%2FDenver" style="border-width:0" width="600" height="450" frameborder="0" scrolling="no"></iframe>

# Course Staff

We post our regularly-scheduled office hours below, but please check the course calendar above for any special changes.

## Instructor

![Bor-Yuh Evan Chang](assets/chang.jpg) | [Prof. Bor-Yuh Evan Chang](http://www.cs.colorado.edu/~bec) <br/> **Regular Office Hours**: Tue 10:45am-11:45am, Thu 8:30am-9:30am in CSEL ECCS 112.

## Grading Assistants

![]() | Shantanu Karnwal
![]() | Priyanka Selvan 
![]() | Eirian Perkins (distance)

## Learning Coordinator

![]() | Spencer Wilson

## Course Assistants

![]() | Juraj Culak <br/> **Regular Office Hours**: Wed 2:30pm-4:00pm, Thu 11:00am-12:30pm in CSEL ECCS 112.
![]() | Andrew Guttman <br/> **Regular Office Hours**: Mon 3:00pm-4:30pm, Thu 5:00pm-6:30pm in CSEL ECCS 112.
![]() | Benno Stein <br/> **Regular Office Hours**: Wed 1:00pm-2:30pm, Fri 2:00pm-3:30pm in CSEL ECCS 112.

# Course Overview

High-level programming languages like Python make programming a
breeze, but how do they work? There's a big gap between Python and
machine instructions for modern computers. Learn how to translate
Python programs all the way to Intel x86 assembly language.

Most compiler courses teach one phase of the compiler at a time,
such as parsing, semantic analysis, and register allocation. The
problem with that approach is it is difficult to understand how the
whole compiler fits together and why each phase is designed the way it
is. Instead each week, we implement a successively larger subset of
the Python language. The very first subset is a tiny language of
arithmetic statements, and by the time we are done, the language
includes objects, inheritance, and first-class functions.

The course has two broad topics:
- Compilation and Language Transformation: How do we manipulate and translate programs?  You will gain experience building such programming language tools.
- Research Applications: You will explore more advanced ideas of your choosing through a final course project.

# Prerequisites

Fluency in at least one programming language (e.g., Java, C, C++,
Python) and experience in picking up new languages independently
is required.
Students will do a lot of programming in Python, but prior
knowledge of Python is not strictly required as long as
there is a motivation to learn it independently and quickly.
Prior knowledge of an assembly
language and language tools (e.g., interpreters) helps but is not strictly required.

The official prerequisites for this course are
CSCI 2400 (Computer Systems) or ECEN
2120 (Computers as Components) and
and CSCI 2824 (Discrete Mathematics).  It is also suggested that
CSCI 3155 (Principles of Programming Languages) be previously taken.

If you have not already taken these courses or if you have any concerns,
please talk with the instructor. Proficiency in programming is absolutely
expected, though there is no specific language required. This means that you
should be able to pick up a new programming language with relative ease.

# Requirements

You will be responsible for the following:
- [**Homework Projects**](assignments.html#homework-projects) (25%).  There will be bi-weekly homework projects during the first part of the course. This is a project-based course, so this projects will be the main learning vehicle.
- **Exercises** (15%). There will be in-class exercises during the first part of the course. This will be the main learning vehicle to prepare for the examinations.
- [**Final Project**](assignments.html#final-project) (15%). In the final part of the course, you will spend your time on a final project.  You will create a final project that explores, extends, or experiments with the ideas in the course.
- [**Class Participation**](assignments.html#class-participation-and-online-discussion) (5%).  Participation includes both in-class and online discussion.
- **Midterm Exam** (15%).
- **Final Exam** (25%)

## Grading

Your overall grade will be determined using the ratio for homework assignments, exercises, the midterm exam, the final exam, and class participation shown above.  There is no predetermined curve (i.e., I hope everyone gets an A based on the level of mastery demonstrated). Cutoffs will be announced after the midterm exam to give you an idea where you stand.

## Regrades

Any concern about an error in grading must be submitted within **one week** of when it is returned. Any coursework submitted for reconsideration may be regraded in its entirety, which could result in a lower score if warranted.  To request a regrade, please go to the instructor's office hours with your coursework and an explanation of what you believe the grading error to be.

## Make-Up Exam Policy

There will be no special or make-up examinations for any student (except in the case of emergency or the stated [special accommodations](#special-accommodations)).

## Redo Policy

This course is project-based, which means the learning is driven primarily by the homework assignments.  To encourage iteration until mastery, you may "redo" any assignment via an oral interview with the instructor for a maximum of 90%. A "redo" must be completed within **one week** of when the assignment is returned. You may request one interview per assignment. However, you may discuss your solutions with the instructors in office hours as much as you like before requesting your regrade. You must submit your assignment on time to participate in a "redo".

## Extra Credit and Participation

Extra credit opportunities may be offered during the course semester.  Extra credit is recorded separately from normal grades and are only considered after final grades have been calculated.  If your final grade is just below a grade cutoff, extra credit may bump you up to the next grade. Finding a bug in the course materials that is then adopted is standing offer for extra credit.

## Pair Programming

You are asked to work on homework assignments in **pairs**, enabling pair programming. Homework assignments are the main opportunity to learn material in this course and thus they count for a relatively small portion of your final grade. It is strongly advised that you work on all the problems in an assignment together so that you understand all of the material and are prepared for the exam.  Everyone will submit assignments, and you must cite your partner explicitly.  If necessary, you may switch partners between assignments, and you are responsible for all assignments individually (e.g., if your partner drops the course midway though an assignment, you still need to submit on time).

## Workload

This is a senior-level or masters-level project-based, implementation-directed course. A high level of independent learning is expected. The workload is up to approximately 10 hours of out-of-class work per week.

## 4000-level vs. 5000-level

The main difference between between the undergraduate- and graduate-level courses will be the expectations for the final course project.  Additionally, the final assignment of grades will be done separately for the 4000-level and the 5000-level students.  The homeworks, exercises, and exams will be the same.

# Evaluation

Both your ideas and also the clarity with which they are expressed matter—both in your English prose and your code!

We will consider the following criteria in our grading:

*   _How well does your submission answer the questions_? For example, a common mistake is to give an example when a question asks for an explanation. An example may be useful in your explanation, but it should not take the place of the explanation.
*   _How clear is your submission_? If we cannot understand what you are trying to say, then we cannot give you points for it. Try reading your answer aloud to yourself or a friend; this technique is often a great way to identify holes in your reasoning. For code, not every program that "works" deserves full credit. We must be able to read and understand your intent. Make sure you state any preconditions or invariants for your functions (either in comments or as assertions)

# Course Communication

There are two main websites for this course.
- **Public**. This public course website contains the course syllabus (this page), the reading schedule, and assignment links. The public website is your primary source for learning materials.
- **Private**. The [course moodle](https://moodle.cs.colorado.edu/course/view.php?id=501) contains any links that are limited to enrolled students. From the moodle, you will find resources like the discussion forum, private project repositories, submission links, grades, feedback, and interview sign-ups. The instructor will provide the enrollment key.

## Discussion Forum: Piazza

We will be using Piazza for online, outside-of-class discussion.  Rather than emailing questions to the teaching staff, most questions should be posted on Piazza.  I encourage you to make class-wide posts whenever possible, but there is an option to send an instructor-private message.

# Textbook and Resources

There is no required textbook for this course.

## Course Notes

Most of the reading will come from the [course notes](/csci4555-notes.pdf), which may be updated throughout the semester.

## Recommended Supplemental Books

The following are some other resources:
- Appel.
[Modern Compiler Implementation in ML](http://www.worldcat.org/title/modern-compiler-implementation-in-ml/oclc/62502129) or
[Modern Compiler Implementation in Java](http://www.worldcat.org/title/modern-compiler-implementation-in-java/oclc/705678079). There is also a C version of this book.
- Aho, Lam, Sethi, and Ullman.
[Compilers: Principles, Techniques, and Tools](http://www.worldcat.org/title/compilers-principles-techniques-techniques-and-tools/oclc/992259938).
- Martelli. [Python in a Nutshell](http://www.worldcat.org/title/python-in-a-nutshell-3rd-edition/oclc/987027647).

# Distance Learning

This course is also offered through distance education. All assignment
submission and content delivery will be electronic.

## Deadlines

Distances students will follow the same assignment deadlines as in-class students. Content delivery should be essentially immediate. Exceptions will only be made in the case of extreme technical difficulties in publishing content.

## Exercises

The questions for exercises will be made available to you on the morning of the posted date, and you must submit your answers by 11:55 p.m. of the same day. The exercises are closed book, just use your brain and only use the computer to type in your answers. For example, do not use the Python interpreter on your computer to help you answer the quiz.

## Tools and External Links

## Computing

For a Linux environment, the following are some resources:

- Get the [CU CS Virtual Machine](https://foundation.cs.colorado.edu/vm/)
- Get a [CSEL account](https://csel.cs.colorado.edu/) (if you're enrolled in a CSCI course). CSEL has a lab in ECCS 128 and remote access servers with SSH (`elra-01` through `elra-04.cs.colorado.edu`).

### Python

- [Python Lex-Yacc (PLY)](http://www.dabeaz.com/ply/)

## x86 Assembly

- [Intel Manuals](http://www.intel.com/products/processor/manuals/index.htm)
  - [Vol. 1](reading/intel_v1.pdf)
  - [Vol. 2](reading/intel_v2.pdf)
  - [Vol. 3](reading/intel_v3.pdf)

- [IA32 Assembly for Compiler Writers](http://www.cse.nd.edu/%7Edthain/courses/cse40243/fall2008/ia32-intro.html)
- [Nice slides about x86 architecture and assembly language](http://www.ece.unm.edu/%7Ejimp/310/)
- [Introduction to Linux Intel Assembly Language](http://heather.cs.ucdavis.edu/%7Ematloff/50/LinuxAssembly.html)
- [Linux Assembly Hello World Tutorial](http://web.cecs.pdx.edu/%7Ebjorn/CS200/linux_tutorial/)
- [GNU Assembler Manual](http://sourceware.org/binutils/docs/as/index.html)
-[x86-64 Machine-Level Programming](reading/asm64-handout.pdf)

## Debugging Assembly

- [Debugging with DDD](http://www.gnu.org/s/ddd/manual/html_mono/ddd.html)

## Pair Programming

- [Video about pair programming](http://video.google.com/videoplay?docid=5248420497037558712)

# Integrity of the Course Materials

The development effort in the course materials, including the lab assignments, the exercises, and the exams, is significant. You agree that you will not share any course materials publicly or privately outside of your teams. The course materials, include your or anyone else's solutions to the lab assignments, exercises, and exams. In particular, you agree not to post your solutions to the lab assignments in a public source code repository, such as public Github repositories. Please use private source code repositories for your work.

Note that there is no conflict with the [Collaboration Policy](#collaboration-policy) described below. You are welcome and encouraged to support each other in the learning of the material.

# Collaboration Policy

You are welcome and encouraged to work together in learning the material. If you worked with someone on an assignment, or if your submission includes quotes from a book, a paper, or a web site, you should thank the source. Bottom line, feel free to use resources that are available to you as long as the use is **reasonable** and you **cite** them in your submission. However, **copying answers directly or indirectly from solution manuals, web pages, or your peers is certainly unreasonable**. If you have any doubts in this regard, please ask the course staff.

**Academic Dishonesty Policy**. We will go by the [Honor Code](http://honorcode.colorado.edu) set forth by the University:

> All students enrolled in a University of Colorado Boulder course are responsible for knowing and adhering to the [academic integrity policy](http://www.colorado.edu/policies/academic-integrity-policy) of the institution. Violations of the policy may include: plagiarism, cheating, fabrication, lying, bribery, threat, unauthorized access, clicker fraud, resubmission, and aiding academic dishonesty. All incidents of academic misconduct will be reported to the Honor Code Council ([honor@colorado.edu](mailto:honor@colorado.edu); 303-735-2273). Students who are found responsible for violating the academic integrity policy will be subject to nonacademic sanctions from the Honor Code Council as well as academic sanctions from the faculty member. Additional information regarding the academic integrity policy can be found at [honorcode.colorado.edu](http://honorcode.colorado.edu).

Academic sanctions may include, but is not limited to, a zero for the assignment or a failing grade for the course.

# Classroom Behavior

We trust and expect everyone to behave in a civil and courteous manner.

In class, the course staff promises their undivided attention and reciprocally expects the same from you. In today's world, this promise requires **turning off transmitting devices**, such as cell phones and wi-fi on notebook computers. The use of notebook computers should be discussed with the instructor and they should be used only for purposes directly relevant to the class discussion. Please notify the course staff if you encounter behavior that distracts from your learning.

We will also go by the policies set forth by the University:

> Students and faculty each have responsibility for maintaining an appropriate learning environment. Those who fail to adhere to such behavioral standards may be subject to discipline. Professional courtesy and sensitivity are especially important with respect to individuals and topics dealing with differences of race, color, culture, religion, creed, politics, veteran's status, sexual orientation, gender, gender identity and gender expression, age, disability, and nationalities. Class rosters are provided to the instructor with the student's legal name. I will gladly honor your request to address you by an alternate name or gender pronoun. Please advise me of this preference early in the semester so that I may make appropriate changes to my records. For more information, see the policies on [classroom behavior](http://www.colorado.edu/policies/student-classroom-and-course-related-behavior) and the [student code](http://www.colorado.edu/osc/sites/default/files/attached-files/studentconductcode_16-17-a.pdf).

# Sexual Misconduct, Discrimination, Harassment and/or Related Retaliation

We will go by the policies set forth by the University:

> The University of Colorado Boulder (CU Boulder) is committed to maintaining a positive learning, working, and living environment. CU Boulder will not tolerate acts of sexual misconduct, discrimination, harassment or related retaliation against or by any employee or student. CU's Sexual Misconduct Policy prohibits sexual assault, sexual exploitation, sexual harassment, intimate partner abuse (dating or domestic violence), stalking or related retaliation. CU Boulder's Discrimination and Harassment Policy prohibits discrimination, harassment or related retaliation based on race, color, national origin, sex, pregnancy, age, disability, creed, religion, sexual orientation, gender identity, gender expression, veteran status, political affiliation or political philosophy. Individuals who believe they have been subject to misconduct under either policy should contact the Office of Institutional Equity and Compliance (OIEC) at 303-492-2127\. Information about the OIEC, the above referenced policies, and the campus resources available to assist individuals regarding sexual misconduct, discrimination, harassment or related retaliation can be found at the [OIEC website](http://www.colorado.edu/institutionalequity/).

# Disability Accommodations

We will go by the [disability guidelines](http://www.colorado.edu/disabilityservices) set forth by the University:

> If you qualify for accommodations because of a disability, please submit to your professor a letter from Disability Services in a timely manner (for exam accommodations provide your letter at least one week prior to the exam) so that your needs can be addressed. Disability Services determines accommodations based on documented disabilities. Contact Disability Services at 303-492-8671 or by e-mail at [dsinfo@colorado.edu](mailto:dsinfo@colorado.edu). If you have a temporary medical condition or injury, see the [Temporary Injuries](http://www.colorado.edu/disabilityservices/students/temporary-medical-conditions) guidelines under the Quick Links at the [Disability Services](http://www.colorado.edu/disabilityservices/) website and discuss your needs with your professor.

# Religious Observances

We will go by the [policy for religious observances](http://www.colorado.edu/policies/fac_relig.html) set forth by the University:

> Campus policy regarding religious observances requires that faculty make every effort to deal reasonably and fairly with all students who, because of religious obligations, have conflicts with scheduled exams, assignments, or required attendance. we will try to accommodate religious conflicts in a reasonable manner. Please check the [exam dates](schedule.html) and submit all requests for adjustments within the **first four weeks** of class. See the [campus policy regarding religious observances](http://www.colorado.edu/policies/observance-religious-holidays-and-absences-classes-andor-exams) for full details.

# Acknowledgments

This course is based on one taught by [Jeremy Siek](http://homes.soic.indiana.edu/jsiek/) in previous semesters.
