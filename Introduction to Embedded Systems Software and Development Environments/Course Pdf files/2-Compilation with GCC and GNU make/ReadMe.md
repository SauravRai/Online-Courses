Compilation with GCC and GNU make
*********************************
(Refer to this for notes from the Course: https://github.com/MohammAAA/Introduction-to-Embedded-Systems-Software-and-Development-Environments )

Week 2

Video 1: Introduction to Build Systems using GNU Toolsets   
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

***************************************************************************************************************************************************

Video 2: Compiling and Invoking GCC

-> To translate just the main.c to assembly. We can run the following commands to stop GCC at compilation proper stage
with the -s option.

-> Now we run this flag with a -g flag, which adds debug symbols. This will help us debug executables later. 

***************************************************************************************************************************************************

Video 4: Creating Header and Implementation Files

Video 4: 

-> C programming has a large variety of prewritten code called the standard libraries.

-> We've likely used these before, such as standard IO and standard LIB or even the Math Library.
   These libraries are often provided with our compiler tool set and they are precompiled.

-> We access them through header definitions. We may even have some third party libraries that we  downloaded for some specific function. So, these are not new to us. Regardless of the source o
   a library, an important reminder is that embedded software needs to be efficient and take up as  little code space as possible. When we include a library, we should ask ourself, is this 
   library precompiled? Is it compiled for my architecture? Was it designed to be optimized for my architecture? 

> If we have the library source code, we should wonder, what software features does this use?
  And what other code does this include? The standard libraries provided with our compiler, will likely be pretty optimized for the instruction set architecture we are using.
  This means that they're not likely optimized for our specific embedded platform. There are often hardware blocks, that may allow us to get even better performance than just software solutions.
  Using the hardware blocks to process information is important, because of our limited resources in our embedded platform, including memory. For instance, some libraries may require large amounts of  
  memory space to operate on, and we may not have that much memory. 

-> Many software engineering organizations often rewrite useful functions from these libraries, specialized for their platforms. This applies to third party or open source software as well. We should  
   not include software arbitrarily. We need to check the software's performance and validate it, that it meets our requirements. 

-> Note: The pre-compiled library allows to share the functions of the library without exposing the source code. The only limitation of pre-compiled libraries is that they are only valid for boards 
   MCUs that have been compiled for. In computer programming, a precompiled header (PCH) is a (C or C++) header file that is compiled into an intermediate form that is faster to process for the 
   compiler.
   
-> One important point with using a library is, we still need the declarations of the library's header files to properly link against that library. Otherwise, the linker will try to search its own    
   paths for the undefined symbols. In addition, the header file is the informative interface to this library. We're going to use this to figure out how to use that library. If we make our own 
   libraries, make our header files as descriptive as possible, so other programmers, who wish to use our library code, know how to use it properly. 
    
-> We might ask ourself, how does cross compilation for my ARM architecture affecting including libraries into my project. These libraries has been precompiled for a given architecture by a specific 
   compiler. By using the ARM compiler, we already have libraries defined for the ARM ISA. To complicate this further, is that there are many different flavors of the ARM ISA.
   How do we know if our compiled library is using ARM Thumb encoding, or something like ARMv7? If the library was designed right, it will support multiple architectures, and this is provided via  
   flags at compilation.    

-> Designing libraries effectively is an important software architecture paradigm. We should take time to think through code design, before trying to write any implementation.
   Things like how our code with interface with each other, the purpose of a module, the purpose of the functions, will help us with our software classification and segmentation. 

-> MOST IMPORTANT TAKE AWAY FROM THIS VIDEO:
   Compile Time Switch for making our code support multiple platforms. How we do it is up to the Software engineers. A useful example was provided using the platform.h file in the course which we can 
   check always.
    
