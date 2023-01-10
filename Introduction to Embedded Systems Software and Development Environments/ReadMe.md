Course: Introduction to Embedded Systems Software and Development Environments
*******************************************************************************

Video 0: Introduction to the course

-> Nearly all embedded systems contain a processing core like a micro controlle and these require the design of low level software in order to function.
   However, software design is just one piece of the embedded system that a software engineer must be familiar with. 

-> You must start with the environment you design in or the development platform. The development platform components include a host machine, a development environment to write and test code in.
   A compiler toolchain to generate designs, development kits to integrate with, and version control to track software history. 

-> This course starts by first defining all parts of the Embedded Systems including the enviroment, hardware and software. 
   
-> SCM indicates how you will organize and manage software project. 

-> We'll be spending a lot of time compiling software with a GCC Tool chain and GNU Make.
   With the tool chain we'll be able to break up our build process and analyze compiled code. We then finish up the module with low level concepts of memory systems for
   our embedded architecture.    
   This includes memory systems, software to hardware memory interface, and writing code for different program segments. 

-> Goal of the course: Develop both portable and architecture specific software for embedded systems in C-programming.  
  
  
************************************************************************************************************************************
Video 1:  Introduction to the Module  

-> In this module, we'll explore the components of the embedded systems design platform. Designing embedded systems takes a lot expertise in both hardware and software disciplines.

-> Embedded software engineers need to have expertise and understanding hardware concepts, knowing how to correctly write and design low-level software, and knowing how to use tools to interact and     
   evaluate their platform

-> Embedded software engineers start their code development process on a host machine, working with tools like compilers, debuggers, and version control.
   A significant amount of time is spent away from hardware, as you develop code and prepare it to test on your target embedded system. 

-> For your software development environment, you will interact directly with tools like GCC, GNU Make, Linux Command Line, Version Control, and an IDE. Also need to install a Serial Terminal program that we can interact
      
************************************************************************************************************************************
Video 2: Introduction to Embedded Systems

->  In this video, we'll introduce the concept of an embedded system and what basic components are needed to bring an embedded application to life.
    This includes a number of hardware and software elements, describe the target architecture and the design environment. Each embedded system has a special purpose and constraints in their system    
    resources. Such as processing, memory, and peripherals. 

->  The hardware is a combination of a processing core, and external circuits for the processor to interact with.
    A software installer combines these two pieces by loading software image into the processor's memory. This differs from any general computer systems that you've worked on
    such as your personal computers or server architectures. Those platforms are designed to work with a variety of applications dynamically adding and removing programs through the lifetime of the    
    platform. This is made possible because of an extensive amount of processing power and memory resources. 
 
->  Specific design decisions will be made in each embedded application for levels of performance, power, and timing. 
    By directly quantifying these characteristics, you can begin to create a list of functional specifications. These specs provide detailed criteria needed to evaluate the capabilities of different   
    target platforms.   
    This analysis is dependent on the hardware architecture and how efficient your coding is.
    
->  The software development platform you will interact with has many parts. First, the target embedded system will likely use printed circuit board technology, or PCBs.
    A PCB is a substrate with conductive wires. It interconnects many integrated circuits and passive developments that all have been soldered on to the board.
    This includes your processor and your power converters. An external programmer is connected to the embedded systems processor, in order to install a target application into the internal 
    memory.     
    
->  An embedded software engineer will focus in becoming an expert on the host development environment, the tools and most importantly, the processor. 
   
->  One solution for the processing core would be a microcontroller. Microprocessors and microcontroller are not the same.
    A microcontroller is a microprocessor with added functionality such as memory and peripheral hardware.
    The processor part of the microcontroller is called the CPU or the Central Processing Unit. This is a piece of hardware that runs our software by fetching and executing assembling instructions for 
    memory. These instructions perform math and logic operations as well as coordinating data movement.     
    
-> The CPU has many sub components with many responsibilities. Many registers, general purpose and special purpose, store operations data and systems state. The CPU and its subsystems interact with    
   other microcontroller resources through one or more buses. A bus controller aids the processor in this data transmission between memory and
   peripherals. Memory holds data that we operate on as well as the program that we're executing. This data is stored in a combination of flash and Random Access Memory or RAM.
   A clock system provides synchronizations across all these components. And to wrap up on trip power management hardware is used for regulation and monitoring.     
        
-> A variety of peripheral hardware maybe included in a micro controller. Some typical peripheral functionality you will see include communication,
   analog signal processing, input and output, timing and processor support.     
   
-> An example Microcontroller can be seen in the Texas instrument's MSP432. This contains one of the arm cortex info processors and a large number of peripheral harbor sub systems    

Conclusion: Embedded systems are unique software platforms because they do not have an abundance of computation power, memory, or peripheral hardware.
Focusing on writing software that can officially code around those limitation Will be a prime focus for this course.
To do this, we will need to bring into play many software tools and our knowledge of the processor. 

