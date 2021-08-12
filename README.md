# Building Computer-Aided Surgery System Using 3D Slicer

## Seminar Information

### Abstract

The goal of this hands-on seminar is to learn how to prototype a computer-aided surgery (CAS) system using an open-source software platform, [3D Slicer](https://slicer.org/). The scale of software systems in modern CAS systems has grown rapidly even in academic settings partly due to the emergence of new computing technologies, including virtual reality/augmented reality, informatics, machine learning, and autonomous robots. As a result, researchers in this research field are forced to dedicate a significant portion of their time to coding, yet most of those efforts are likely to be consumed in reimplementing existing algorithms or features, which have already been developed by others. This engineering problem is often referred to as “reinventing the wheel.” In addition, the maintenance of such a large-scale software system usually requires extensive documentation and continuous testing, which are not necessarily the priorities of academic researchers, especially for those who work on the projects as part of their theses for 2- to 3-year periods.

In the past decade, many research groups have shifted their effort from in-house development to open-source development, where a project-specific software application is built on an existing open-source software platform. Those platforms allow sharing a wide range of algorithms and methods that have been implemented, documented, and rigorously tested among the developers in the community. Therefore, the developers can leverage those existing algorithms and methods for their new applications with a minimal coding effort and focus on the implementation of new algorithms and methods. The newly implemented algorithms and methods can then be contributed back to the platform so that the other researchers can reproduce the results or reuse them for different applications. As a result, researchers can increase their presence in the community boosting the citations to their research publications.

In this seminar, I will present a brief overview of the 3D Slicer platform and demonstrate how the platform can be used to build a research CAS system. The seminar will consist of two sessions: 1) a short lecture on the architecture of 3D Slicer and several use-case scenarios; 2) a tutorial session where the participants build a simple image-guided system using the Python scripting language on their computers. After the seminar, the participants are expected to be able to start their projects with 3D Slicer and/or participate in the 3D Slicer community to gain further knowledge about the platform.

### Topics/Keywords

- Computer-aided surgery
- Image-guided Therapy
- Medical robotics
- Software integration
- Open-source software

### Date/Time

August 18, 2021, 10am-12pm JST (Online; Invetation will be sent separately)

### Language
Japanese (with English Slides, Q/A in both Japanese and English)

### Lecturer
[Junichi Tokuda, Ph.D.](https://scholar.harvard.edu/tokuda/home) (Associate Professor of Radiology, Brigham and Women’s Hospital / Harvard Medical School)

## Prerequisite (TBD)

For the tutorial session, the participants are expected to bring their own computer (Windows/Mac/Linux) with the following software installed:

- One of the following operating systems (see [details](https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements))
  - Windows 10
  - macOS High Sierra or later
  - Ubuntu 18.04 or later
  - Cent OS 7 later
- 3D Slicer 4.11.20210226 (Can be downloaded from [the download page](https://download.slicer.org))
- [Git](https://git-scm.com/) client software ([GitHub Desktop](https://desktop.github.com/) is recommended, if not familar with Git)
- Python 3.8 or later

## Seminar Materials

- Introduction Slides (to be uploaded)


## References
- [3D Slicer Official Page](https://slicer.org/)
- [OpenIGTLink Official Page](http://openigtlink.org/)
- [3D Slicer Training](https://www.slicer.org/wiki/Documentation/4.10/Training)
- [3D Slicer scripting and module development tutorial provided by Queen's University](https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true)
- [Issues with Qt Designer on macOS (Discussion in Discourse)](https://discourse.slicer.org/t/edit-ui-raies-designer-cannot-be-opened-because-of-a-problem/13176)
