# Building Computer-Aided Surgery System Using 3D Slicer

The goal of this hands-on seminar is to learn how to prototype a computer-aided surgery (CAS) system using an open-source software platform, [3D Slicer](https://slicer.org/). The scale of software systems in modern CAS systems has grown rapidly even in academic settings partly due to the emergence of new computing technologies, including virtual reality/augmented reality, informatics, machine learning, and autonomous robots. As a result, researchers in this research field are forced to dedicate a significant portion of their time to coding, yet most of those efforts are likely to be consumed in reimplementing existing algorithms or features, which have already been developed by others. This engineering problem is often referred to as “reinventing the wheel.” In addition, the maintenance of such a large-scale software system usually requires extensive documentation and continuous testing, which are not necessarily the priorities of academic researchers, especially for those who work on the projects as part of their theses for 2- to 3-year periods.

In the past decade, many research groups have shifted their effort from in-house development to open-source development, where a project-specific software application is built on an existing open-source software platform. Those platforms allow sharing a wide range of algorithms and methods that have been implemented, documented, and rigorously tested among the developers in the community. Therefore, the developers can leverage those existing algorithms and methods for their new applications with a minimal coding effort and focus on the implementation of new algorithms and methods. The newly implemented algorithms and methods can then be contributed back to the platform so that the other researchers can reproduce the results or reuse them for different applications. As a result, researchers can increase their presence in the community boosting the citations to their research publications.

In this seminar, I will present a brief overview of the 3D Slicer platform and demonstrate how the platform can be used to build a research CAS system. The seminar will consist of two sessions: 1) a short lecture on the architecture of 3D Slicer and several use-case scenarios; 2) a tutorial session where the participants build a simple image-guided system using the Python scripting language on their computers. After the seminar, the participants are expected to be able to start their projects with 3D Slicer and/or participate in the 3D Slicer community to gain further knowledge about the platform.

Topics/Keywords:

- Computer-aided surgery
- Image-guided Therapy
- Medical robotics
- Software integration
- Open-source software

## Seminar Information

### Date/Time

August 18, 2021, 10am-12pm JST (Online; Invetation will be sent separately)

### Language
English (Q/A in both Japanese and English)

### Lecturer
[Junichi Tokuda, Ph.D.](https://scholar.harvard.edu/tokuda/home) (Associate Professor of Radiology, Brigham and Women’s Hospital / Harvard Medical School)

## Timetable

- 10:00am-10:20am  Introduction 
- 10:20am-10:50am  Hands-On Tutorial 1: 3D Slicer basics
- 10:50am-11:00am  (Break)
- 11:00am-12:00pm  Hands-On Tutorial 2: Building a 3D Slicer module for CAS applications

## Prerequisite (TBD)

Prerequisite Knowledge:
- Principle of Computer-Aided Surgery (CAS) / Image-Guided Therapy (IGT)
- Basic programming (C/C++, Python, etc)


Computer Setup (for hands-on tutorial):

- One of the following operating systems (see [details](https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements))
  - Windows 10
  - macOS High Sierra or later
  - Ubuntu 18.04 or later
  - Cent OS 7 later
- 3D Slicer 4.11.20210226 (Can be downloaded from [the download page](https://download.slicer.org))
- [Git](https://git-scm.com/) client software ([GitHub Desktop](https://desktop.github.com/) is recommended, if not familar with Git)
- Python 3.8 or later
- Text editor to edit a source code

## Seminar Materials

- Introduction Slides (to be uploaded)
- [Tool Tracking Tutorial](Instructions/ToolTracking.md)
- [SlicerIGT Introductory Tutorial](Instructions/SlicerIGTIntroduction.md)
- [Custom Module Tutorial](Instructions/CustomModule.md)


## References
- [3D Slicer](https://slicer.org/)
- [OpenIGTLink](http://openigtlink.org/)
- [SlicerIGT](http://www.slicerigt.org/)
- [3D Slicer Training](https://www.slicer.org/wiki/Documentation/4.10/Training)
- [3D Slicer scripting and module development tutorial provided by Queen's University](https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true)
- [Issues with Qt Designer on macOS (Discussion in Discourse)](https://discourse.slicer.org/t/edit-ui-raies-designer-cannot-be-opened-because-of-a-problem/13176)


### Acknowledgements

This seminar is hosted by [BMPE Lab., University of Tokyo](http://www.bmpe.t.u-tokyo.ac.jp/en/member.html) and [National Center for Image-Guided Therapy, Brigham and Women's Hospital](https://ncigt.org/), and supported in part by The U.S. National Institutes of Health (R01EB020667, R01CA235134, P41EB028741, and P41EB015902). 

[3D Slicer](https://www.slicer.org/) is developed by the 3D Slicer community. [SlicerIGT](http://www.slicerigt.org/) and [PLUS Toolkit](https://plustoolkit.github.io/) are developed at [Perk Lab., Queen's University, Canada](http://perk.cs.queensu.ca/). OpenIGTLink is developed by the OpenIGTLink community. Lists of contributors for those software packages can be found at:

- [3D Slicer - Acknowledgements](https://slicer.readthedocs.io/en/latest/user_guide/about.html#acknowledgments)
- [SlicerIGT - Contributors](http://www.slicerigt.org/wp/contributors/)
- [PLUS Toolkit - About](https://plustoolkit.github.io/about)
- [OpenIGTLink - About](http://openigtlink.org/about)




