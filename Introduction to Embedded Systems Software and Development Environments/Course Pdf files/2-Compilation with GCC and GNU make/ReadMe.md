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
   Compile Time Switch for making our code support multiple platforms. How we do it is up to the Software engineers. A useful example was provided using      the platform.h file in the course which we can  check always.
    
************************************************************************************************************************************    

Video 5: Linkers 

->Each architecture is very different from others, so the locator needs a special file to provide instructions about how to assign architecture specific addresses to the generic object file. This special file is called linker file or linker script

-> Linker file provides the locator with information on where are the physical memory regions of the processor that will interface with the defined code regions. Linker file is architecture dependant

-> Linker file specifies details such as:
   (i) segment name
   (ii) region name
   (iii) memory sizes
        We need to assign the exact start address of the data and code memory (origin), and also the memory length of each segment (length)
   (iv) access permission
        Each memory region specifies access permission such as read (R), write (W), and execute (X) for memory blocks

-> Each memory region specifies access permissions such as read, write, and execute for memory blocks. Typically, the data memory, which will be in the SRAM, will be set as read and write, or RW.
   This is because we will often read, modify, write data from SRAM. Code memory, on the other hand, will have read execute or RX permissions. This is because we will read our instructions from code   
   memory like flash and execute them on the CPU. 
   
-> There are a handful of reasons why we want to make code memory not writable during program execution. One reason is to prevent an accidental overwrite 
   of the code memory, causing the program to be corrupted. Additionally, this is also for security. By making the code memory only readable after programming, then we are making it harder for people 
   who hack programs by exploiting the hardware to add new code into the code memory region. Some processors even cause a fatal error or exception if the processor tries to execute code out of SRAM or 
   data memory regions. 


-> After we've finished linking and locating, we may be interested in seeing how the memory allocation was done. For this, we can tell the linker to produce a map file.
   This file will provide information on how all of these regions and memory segments were used and allocated. This map file also gives us specific addresses for the allocations. 

-> Program memory is generally used for storing program code, although it can be used for storing data; while, as its name indicates, Data memory is used for storing data.
   Program Memory (ROM) is used for permanent saving program being executed, while Data Memory (RAM) is used for temporarily storing and keeping intermediate results and variables. Program Memory    
   (ROM) is used for permanent saving program (CODE) being executed. The memory is read only.
    
-> Linking is a complicated process and involves many different types of input files, including object files, library files, and linker files.
   The process of relocating is yet another example where expertise on an architecture is needed, as we must define the memory regions of our architecture. Embedded software engineers must be involved 
   in this, not only because of how they design their code, but also how it's going to fit into the memory space. 

************************************************************************************************************************************    

Video 6:

Motivation for the Makefile:

-> To create a build system to simplify and improve our process of building a software target. The process software teams used to create a software product    using a lot of tools to build, test, and version and develop code. 
   However this process can be very tedious. There are numerous commands and many flags that are needed for our advanced use of    the command line tools.      To memorize all of these options is not feasible   

-> Next, software companies and projects usually support multiple build targets and architectures, both of which affect how we build. Now the concern has to    do with the large number of source files a typical software project will contain.
   If we compare these concerns with our IDE build process, we do not see any differences. Behind the scenes the IDE is running any other same compile    commands for every single source file you have added to your project and each with many options.

-> To automate the build process to save efforts and time is called as make

-> Make is yet another free tool we get from the GNU tool chain that is utilized from the command line in the exact same way as GCC.
   It lives in the executable program binaries folder on Linux and has many options just like GCC did.

-> One big difference is that it is not part of the GCC tool chain as it is independent of the Compiler or the architecture you're using. Therefore there is    no arm-none-eabi prefix to the command.
   This is a good thing since it provides more examples of software abstraction and independence for our course as we want to build a tool that can support    many types of compilers and architectures.

-> The GNU Makers formally defined as a tool that controls generation of executables and non-source files of a program, from the program source files. This    is very important because we can use GNU Make to do more than just compile but also generate software dependencies, statistical information and many    other items. Best of all it's free
 
-> Careful and educated use of this tool can help you create an extremely consistent software built With very low developer time for compiling.

-> This Makefile provide special directions and procedures to make in order to create an executable file from a multitude of input files. Each make file    contains specific recipes for building particular targets. These recipes usually have some dependencies and produce some type of output.

-> Think of including header files and C files as dependencies for a recipe to build a particular object file. These dependencies can be auto-generated and    output to .dep or .d files automatically by make.

-> We could invoke make and we can execute many define targets with just the single command. Each target can follow a particular recipe depending on how you    defined your targets.

-> Make can be configured to use whichever Complier Toolchain and build process of your choosing. You could use vendor provider toolchains or continue to    use GCC as the toolchain with the same process to generate files that we did with our five steps of building. Make could even be configured to support      multiple versions of a compiler or even multiple compilers with the same Makefile.

-> Further, the same object files, Dependency Files and Map File can output from the process of Make with careful structure of your Make system.

-> The one difference in writing our own Makefiles versus using an IDE is that the IDE is going to auto-generate their Makefiles depending on how you       configured your software project. Meaning it will generate all of the specific flags and linker files for the guards to your architecture. This is good    for parading a very simple interface for developers wanting to start fast. But very bad for maintainability and portability. 
************************************************************************************************************************************    


Video 7:
Makefiles Part 1

->  Automating the build process is just like writing software. In some cases, you will use shell scripts or other scripting languages to run a series of commands to generate needed executable files. These commands will of course be a mixture of our GCC commands to produce executables. In our case, you will be writing a makefile that stores all of the necessary configurations, flags, and commands in order to generate our build in other non-source files.
************************************************************************************************************************************    


Video 8:
Makefiles Part 2

->  As we learned earlier, make and makefiles can give us an opportunity to simplify and improve our build process. In this day and age of technology, the     need to support many architectures, compilers, or even versions of software, is pretty typical.
    Not only do you want a code base that can be flexible to support these variations, we want your build system to support them as well. Just like with         our software design and architecture, we need to engineer good quality into our build system. We already learned some basic features of make and         makefiles to design our system. Now, we will learn some more advanced features to make our build systems even better.

-> What if we wanted to make file that could support multiple architectures in addition to multiple build targets.
   We could define completely different custom build targets for different compilers or architectures. Or we could have make do some conditional execution      and assignment in the makefile, based on input parameters or system information. This should sound familiar, since this is similar to the compile time       switches we have used before. We will implement them similarly as we did in C with compile time switches. Except, we might set some make file flags to       define different variables, flags, or applications that we should use in the make file.
************************************************************************************************************************************    
