Compilation with GCC and GNU make
*********************************
(Refer to this for notes from the Course: https://github.com/MohammAAA/Introduction-to-Embedded-Systems-Software-and-Development-Environments )

Week 2
Video 1 Introduction to Build Systems using GNU Toolsets   
(Only Provided points which are missed in the notes)
  
-> Providing specific guidance and optimizations during the build process, is important for our embedded platform as the assembly instructions are the objects that need to be optimized before they are 
   converted into the processor executable.       
 
-> Managing the compilation of many files, with all their respective compile options becomes very cumbersome. To help with this, we'll be introduced to another useful tool in the GNU tool chain called 
   Make. Make is a tool that controls the generation of executables and other non source files of a program from the program source files.    
   
-> Make will help us manage this whole process of building our executable.    
   
-> Instead of installing on a target system, we will start first by learning to simulate our software on a host machine, and validate non architecture specific pieces before moving on to our intended 
   target. Mastering how to use these build tools will prove immensely valuable in industry and in your own projects.    
   
-> We will learn to
  (i) Implement a build system using GNU's make and GCC compiler tool chain.
  (ii) Examine the pre-processors role in compilation, and
  (iii) Integrate new libraries to a build system.     
   
   ![image](https://user-images.githubusercontent.com/34119879/213915413-b60fb175-67bc-4c4b-acec-eced4335821e.png)

