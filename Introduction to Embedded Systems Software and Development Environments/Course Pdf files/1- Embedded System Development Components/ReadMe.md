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
   
******************************************************************************************************************************   
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

Video 7: Development Environments Overview

-> Development environments are key for software engineers as they are the means with which a software project is created. The embedded system target is important, but
   all of the software is designed outside of that system. You need some method of generating an executable file and installing it onto the device. 
    
-> The primary goal of the development environment would be to allow engineers to write, compile, install and debug a program.
   There will be many options for the tools you can write code in. But a project will often have very few options for the compiler, installer and debugger.
   And unfortunate consequence to this will be that some of these programs may not be supported on every desktop OS    
    
-> In order to show all of the features that the development environment offers. We'll be using two different desktop environments. A command line in a Linux environment and
   a vendor's Integrated Development Environment    

-> Building software project using command line is the de facto standard amongst software engineers. The command line interface gives you a powerful level of control
   of applications at the expense of user interface. You'll provide complex commands to the computer via text input. The command line is typically a power user interface.
   Command lines are not regularly used because they are not as intuitive, but they exist on many computers.     
   
-> For command line we can ch0ose a Linux based machine. However, there are many distributions of Linux, you can choose from, such as RedHat, SUSE, Gentoo and Arch.     
   This host machine will be used to run tests and simulate certain pieces of software. 
   
-> For compilation, we can use GNU's toolset to generate our software executable files. Installation and debugging will be an architecture dependent thing.
   However, installation could be as simple as copying our executable or invoking an installer program. Debugging will depend on the target.
   Host debugging can utilize a command line tool GDB, the GNU project debugger. On target debugging can be done through a network debugger or connected hardware debugger.
   These two require some type of physical control of our microcontroller.
   
-> The second environment you want to interact with is a vendor provided integrated development enviroment. IDEs encapsulate all of the functionality that we get from the command line.
   But they provide a much more interactive use interface. The IDE will hide all of the details of how the compiler, installer and debugger application are being invoked from the developer.
   This interface is usually less ideal for software engineers because the trade off for a good UI might restrict a developer's capabilities.     
   However, many features of the IDE provide more user friendly methods for developing and debugging an application including more informative memory graphics.  
   
-> These environments will be key, not only to the development of our projects but to the validation    
    
-> While using the IDE's inside the properties are all the fine controls of development environment. Here, we can modify compilers, installers, and debugger configurations.     
   However, they make use command line variables to make the interface more dynamic. With the compiler integrated, we can build from this window by selecting from the drop down menu Project Build.   

************************************************************************************************************************************    
    
Video 8: Development Kits and Documentation (IMPORTANT ONE!!)

-> In this video, we'll look at the manufacturer and third party hardware development kits and the important documentation that is needed to configure your microcontroller. 

-> Development kits are an important tool for software engineers to start becoming familiar with an architecture. Designing hardware takes a lot of experience and you hope your platform has no   
   hardware bugs that stall your software progress. By using evaluation kits, you have a pretty generic hardware platform with lots of vendor support for you to get your software design started.
   Most projects begin by using developers kit to evaluate platform options. There are many manufacturers of microcontroller integrated circuits, ICs, or application-specific integrated circuits,    
   ASICs, in the industry. Some examples include Texas Instruments, Silicon Labs, Atmel, or NXP Semi-conductors. 

-> By using evaluation kits, you have a pretty generic hardware platform with lots of vendor support for you to get your software design started.
   Most projects begin by using developers kit to evaluate platform options. There are many manufacturers of microcontroller integrated circuits, ICs, or application-specific integrated circuits,    
   ASICs, in the industry. Some examples include Texas Instruments, Silicon Labs, Atmel, or NXP Semi-conductors.     
    
-> The silicon manufacturers often make many different type of chips with an assortment of features, and they sell their chips for a variety of vendors.
   Knowing how to pick a particular chip is difficult because there are particular factors you need to investigate before committing a product to a particular chip choice.     
    
-> Note: Inside the IC, there's also a chance that different parts of silicon were built by different people.
   ARM is a good example, as they build CPU cores and other technology for silicon manufacturers. Microcontrollers have many features that you need to know about before making
   a selection, especially because there will be software implications. Some important features include the word size, the number of registers, flash and RAM sizes, branch prediction support,    
   instruction and data cache support, floating point arithmetic support, or DMA support.     
 
-> These features affect the operation and performance on embedded platform. For instance, as you design your project, you will have to answer questions such as,
   How much memory will I need for my application? How fast does my application need to run? And what kind of mathematical support do I need?
   You likely need to have some of these answers before you commit to a particular microcontroller. The process of creating this feature andoperation requirements checklist 
   is called a specification, or a features spec. It's possible that you need to make significant software changes, or even a hardware change, in the middle of a design process 
   if you did not evaluate your initial designs correctly. In general, you do not select a chip or a part at random. There is some investigation of features and specs needed at the beginning 
   of a project, which includes some prototyping and proof of concept.
   Fortunately, manufacturers help with this process by providing resources to analyze their products     

>  We start with discussing the Selector Guide. This helps a user slip down choices by interactively selecting feature sets for our design.
   It shows a full processor family. A chip family will share the same chip architecture. Each sub-family typically has more differences in supported hardware.
   And each device in a sub-family only has a slightly variances from one sub-family part to another.This guide example is somewhat of a painful chart to look at to select the part.      
  
-> The product brief gives a concise overview for quick evaluation of a platform for design, but more details than what you will see in the selector guide.
   This is much more marketed, and is far less dense than strict product specifications.         
         
-> Once you have slimmed down your selections to a subset of models, you can start getting into much more detailed documentation sources like the datasheet.
   This document gives technical specifications on a chip or a family of chips with a breakdown of all the differences between each version or part number within the family.
   Pin counts as well as operation specifications are provided with diagrams, tables and plots. These operation specifications can include many things such as the Contains detailed
   Technical Specifications
   • Electrical
   • Timing
   • Environmental
   • Physical Package      
 
-> The materials in the datasheet is not just for a hardware engineer to use. Timing characteristics are very important for a software engineer to know about so they may predict or calculate runtime   
   requirements and performance. In addition, the datasheet is going to detail the pinpoint mappings for a peripheral device you might use.         
   This is a table that describes which pins match up to the general IO ports of the microcontroller, and subsequently, which pins can connect to certain peripheral devices.
   The datasheet does not typically provide information on configuration. For that, we need to look at the Family Technical Reference Manual. This manual describes information on general platform   
   components and configuration. You may then have a sub-family reference manual which covers particular settings of a specific device.
   These are manuals that you need to look up to know how you go about configuring a chip using Bare-Metal Firmware. 

-> It is important that if something is operating unexpectedly with your chips that you consult the errata.         
        
-> Now that a chip has been chosen, we need to start on a proof of concept and software prototyping.
   Not all customers have the time or ability to design a printed circuit board or a evaluate their chosen chips and design. Many businesses just create development kits and
   module boards so that prototyping can be be done easily, speeding up the time it takes chip manufacturers to get their products in customer hands for evaluation.
        
-> Here we have two example development kits. The first is a microcontroller development kit called the Freedom FRDM-KL25Z.
   This board is a product of NXP and has many impressive features including some supplemental external hardware, a capacitive touch slide, an RGB LED, and an accelerometer.         
   A second example is the wireless module featuring the Nordic nRF24L01 chip. This is not a microcontroller development kit      
        
-> As an embedded software engineer, you can easily acquire many of these module boards or microcontroller development kits without deep hardware knowledge.
   Although you will need to figure out the connection and interface requirements between your boards.    
 
-> Once a chip and development kit has been acquired, you need to get access to a compiler, some programmer debugger hardware and the executable installer software.
   The design of these support systems, dev kits, debuggers, programmers and software, are often done by applications and tool engineers from the chip manufacturer companies or third party vendors.
   But these kits, extra hardware and software tools often come at an expensive price from the manufacturer. Competition in this market of dev kits has grown significantly with the need for
   even faster prototyping. As a result, four dev kits have become even more widely available at a cheap price with free software tools and
   integrated programmer debugger hardware on the kit itself.      
   Example, This board has a secondary processor which is used to run as an onboard program debugger adaptor that can flash our target processor, the KL25Z.
   This adaptor is called OpenSDA.
        
-> These onboard programmer debuggers provide much cheaper options for the software development tool sets you can use to interact with the desired
   embedded platform.         
        
