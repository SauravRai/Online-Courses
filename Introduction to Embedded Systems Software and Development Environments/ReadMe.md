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
    This includes a number of hardware and software elements, describe the target architecture and the design environment. Each embedded system has a special purpose and constraints in their system resources. Such as processing, memory, and peripherals. 

->  The hardware is a combination of a processing core, and external circuits for the processor to interact with.
    A software installer combines these two pieces by loading software image into the processor's memory. This differs from any general computer systems that you've worked on such as your personal computers or server architectures. Those platforms are designed to work with a variety of applications dynamically adding and removing programs through the lifetime of the platform. This is made possible because of an extensive amount of processing power and memory resources. 
 
->  Specific design decisions will be made in each embedded application for levels of performance, power, and timing. 
    By directly quantifying these characteristics, you can begin to create a list of functional specifications. These specs provide detailed criteria needed to evaluate the capabilities of different target platforms.   
    This analysis is dependent on the hardware architecture and how efficient your coding is.
    
->  The software development platform you will interact with has many parts. First, the target embedded system will likely use printed circuit board technology, or PCBs.
    A PCB is a substrate with conductive wires. It interconnects many integrated circuits and passive developments that all have been soldered on to the board.
    This includes your processor and your power converters. An external programmer is connected to the embedded systems processor, in order to install a target application into the internal memory.     
    
->  An embedded software engineer will focus in becoming an expert on the host development environment, the tools and most importantly, the processor. 
   
->  One solution for the processing core would be a microcontroller. Microprocessors and microcontroller are not the same.
    A microcontroller is a microprocessor with added functionality such as memory and peripheral hardware.
    The processor part of the microcontroller is called the CPU or the Central Processing Unit. This is a piece of hardware that runs our software by fetching and executing assembling instructions for memory. These instructions perform math and logic operations as well as coordinating data movement.     
    
-> The CPU has many sub components with many responsibilities. Many registers, general purpose and special purpose, store operations data and systems state. The CPU and its subsystems interact with other microcontroller resources through one or more buses. A bus controller aids the processor in this data transmission between memory and peripherals. Memory holds data that we operate on as well as the program that we're executing. This data is stored in a combination of flash and Random Access Memory or RAM.
   A clock system provides synchronizations across all these components. And to wrap up on trip power management hardware is used for regulation and monitoring.     
        
-> A variety of peripheral hardware maybe included in a micro controller. Some typical peripheral functionality you will see include communication,
   analog signal processing, input and output, timing and processor support.     
   
-> An example Microcontroller can be seen in the Texas instrument's MSP432. This contains one of the arm cortex info processors and a large number of peripheral harbor sub systems    

Conclusion: Embedded systems are unique software platforms because they do not have an abundance of computation power, memory, or peripheral hardware.
Focusing on writing software that can officially code around those limitation Will be a prime focus for this course.
To do this, we will need to bring into play many software tools and our knowledge of the processor. 

************************************************************************************************************************************

Video 3: Embedded Software Engineering

-> Good software design needs to understand what the purpose and required operations specifications that a project needs. It's good to start by breaking a software concept down into flow diagrams or software blocks a flow diagram can depict, how a particular piece of software or algorithm should behave. Often it contains a same functional software contracts, such as conditional decisions and high level function calls.

->  An example of a typical software organization can be seen with an OS-based design. There are low-level Device Drivers that interact with Hardware. There are software to help boot or start the system. There's an operating system to schedule processes and manages resources. There are shared libraries that many software components use and finally the higher level software reflects user applications.

-> Writing code to direct the interface of the hardware is referred to as bare-metal firmware.  

-> A firmware engineer requires deep knowledge of the hardware, not only for configuration of the bare-metal but also for hardware timing and limitations related to their software design. A software engineer's role will be to try and segment the hardware interface into something referred to as a HAL or Hardware Abstraction Layer.

-> By design this interface works as a module component but they well defined interface. It allow software above the HAL layers become platform independent or agnostic to the specific hardware     
   implementation, a concern layers, portable across platforms.
   In general for each of the box in our software system, you need to know what the responsibilities are and how the different blocks interface one another.  
    
-> Some time into understanding the hardware specs that affect the software design as we try to engineer the best solution as embedded systems are highly specialized with limited resources
    
-> A  common software block design method is called component design. This is where we define small functional software blocks that have certain tasks.
   We define the interface mechanism and the specs that each modules needs to adhere to. By doing this, you can build modulized software that is reusable across different
   systems, architectures and platforms.      
   
-> On-target testing is just a term that refers to installing your code on to your particular embedded system instead of another.
   So new chip sets or printed circuit boards had to be built with the desired hardware and connections so the software engineer knew what they needed to configure.
   Thankfully, new hardware development techniques and system emulation provide quality resources for low level development.     
   
   Take for example the introduction of development kits and the SDKs that allow us to rapidly prototype software.
   It's not only enabled engineers to begin writing low level code or firmware but also provided them with the physical resources to test code on
 
-> There are five main development tools that allows software engineers to get started on development and testing of their applications.
   These are first simulators, software that imitates or intended to hardware's behavior without the actual hardware. Emulators, the hardboard platform that imitates the operation of your
   intended system. Compilers, it's the software that allows developers to pre-executable code for their intended architecture.
   Installers, a software-hardware combination that allows compiled executable programs to be installed onto a platform.     
    
   And debuggers, a hardware-software solution that allows programmers to test and validate their executable programs. These tools are important because developing hardware takes time and
   it's expensive. 

-> Simulators and emulators will allow validation of design to occur before the arrival of hardware. Compilers, Installers, and debuggers will provide a quick development of features for your     
   embedded target and an easy way to fix off our bugs.     

-> Code should be such that is maintainable, testable, portable, robust, efficient and consistent. 

-> By putting time into architecting your software, writing code effectively. Making it modular, you can extend the lifetime and re-usability of this pieces,
   of your various projects and platforms. This obviously speeds up embedded systems prototyping time lines and the rate with which you can hit the market with your product. 

-> C-Programming has benefits for both low level hardware interactions and high level software language features. This provides portability across different embedded platforms. 
   C is high level enough that you do not need to know every detail about the very specific assembly level architectures. 

-> Typical embedded engineers actually write a form of C called Embedded C. Embedded C differs from C because it puts a focus on the following features.
   Efficient memory management, timing centric operations, direct hardware/IO control, code size constraints, and optimized execution. 
   We can thinkn Embedded C as optimum features in minimum space and time. 

Video 4: C programming review 

-> Embedded C focuses on some certain features that are extremely relevant to low-level design. However, Embedded C and C program are still the same language. 

-> Data types are actually architecture-dependent, and the C standard specifies minimum sizes for the data types.

-> Translation between decimal and unsigned binary can be done very simply because unsigned numbers use a positional number system representation to express value.
   Each position represents a value and a magnitude. 
   
-> Signed numbers are represented with the two's complement form. The conversion of signed numbers is a little more complex because they split the numbers of unique binary combinations in half. One    
   half for your positive number set and the other one for your negative set. The positive bit mappings look just like unsigned numbers with a zero in the most significant position. The negatives are  
   represented with a one in the most significant position, the base value represents a very large negative number. Lastly, fractional numbers can be represented with fixed point or floating point 
   representations.  
 
-> Embedded applications will favor the use of binary and hexadecimal for firmware as well as both signed and unsigned number representations. Data is assigned and manipulated using a variety of   
   operators. There are multiple types of operators which include logical, bitwise, arithmetic, and relational. 
    
-> Bitwise operators are logic operators that operate on an individual bit basis instead of a full expression. The bitwise operators include right and left shifts, OR, AND, EXOR, and a one's    
   complement or a bitwise invert. Arithmetic operators perform your typical math operations, such as add, subtract, multiply, divide, increment, decrement, and modulus
   Also, bitwise and arithmetic operators can be combined with an assignment operator for simple expressions. 

   Binary to Hexadecimal example:
   0b0111_1111 -> 0x7F
   
   0b1111_1111 -> 0xFF
   
   0b1000_0000 -> 0x80
   
******************************************************************************************************************************   
Video 6: C standardization and team coding standards
****************************************************** 

-> Software languages will evolve over time just like software applications do. New versions with new features will be released, and software teams will need to make important decisions. What language 
  should they use? What version should they support? 
      
-> Organizations like the International Electrical and Electronics Engineers IEEE, the International Organization for Standardization, ISO, and the American National Standards Institute, ANSI, are 
  three groups that are involved with the process of standardizing various technical ideas including software. Without organizations like these, creating portable projects would require much more    
  engineering overhead.       

-> In 1970s the first unofficial standard of C programming was created by Ken Thompson and Dennis Richie. This classic version of C was referred to as K&R C.     
   This version of C was the standard for C programming for about 15 years. More importantly, in 1989, ANSI-C standard was introduced, and in 1990, ISO adopted the standard officially.
   These are referred to as C89 or C90. C99 came out about a decade later with some more features. And C11 is the most recent C standardization, and it has introduced many features specifically 
   related to multi-threading.  
   The reason why it is important to know about these standard diversions,is that many compilers have been built to default to various versions or even only support only one standard of C programming.

-> In our projects, we will be specifying a specific standardized C version during compilation and utilizing important new features from C99, like the inline keyword.
   This keyword will be crucial for how we design our firmware for embedded systems. 

-> In addition to discussing C standardization, we will discuss the topics of a coding guideline, or a coding standard. A coding standards is simply a list of software guidelines a project
   will need to be written to. These standards can be a mixture of requirements. There could be special format and documentation of the code needed. We many need to program the flow of routines in a   
   certain way. How you name functions, files, and variables may need to fit a certain scheme. We may even have limits on the types of features, a developer can use on a platform.    
    
-> The Motor Industry Software Reliability Association introduced an industry standard coding guideline called MISRA C,
   which was specifically aimed at embedded architectures.
************************************************************************************************************************************    
