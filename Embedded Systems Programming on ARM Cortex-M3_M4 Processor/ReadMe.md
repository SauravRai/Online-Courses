
COURSE STRUCTURE: 
*****************

SECTION I:INTRODUCTION
**************************************************************************
1. Motivation to learn the Cortex Family of processors
2. Processor core VS Processor
3. Processor VS Microcontroler
4. Download source code and slides 

-> SOFTWARE IP OF THE ARM CPU IS OWNED BY ARM AND VARIOUS OTHERS COMPANIES BUYS THIS BEFORE USING THEM. THEY MAY USE IT ACCORDING TO THEIR NEEDS. 

Motivation to learn the ARM-CORTEX-M processors 
************************************************
1. Floating point unit: 
A floating-point unit (FPU, colloquially a math coprocessor) is a part of a computer system specially designed to carry out operations on floating point numbers.


2. What is a DSP? Digital Signal Processors (DSP) take real-world signals like voice, audio, video, temperature, pressure, or position that have been digitized and then mathematically manipulate them. A DSP is designed for performing mathematical functions like "add", "subtract", "multiply" and "divide" very quickly.


3. The Memory Protection Unit (MPU) is a programmable unit that allows privileged software, typically an OS kernel, to define memory access permission. It monitors transactions, including instruction fetches and data accesses from the processor, which can trigger a fault exception when an access violation is detected.
-> Arm Cortex M processor is customizable to include FPU, DSP unit, MPU, etc



4. What RTOS means? Real-time operating system
What is a real-time operating system (RTOS)? A real-time operating system (RTOS) is an OS that guarantees real-time applications a certain capability within a specified deadline. RTOSes are designed for critical systems and for devices like microcontrollers that are timing-specific.


5. Arm Cortex M processor uses Thumb Instruction set which is a collection of 16 bit as well as 32 bit instructions It cannot execute the ARM instruction set instructions but it uses Thumnb instruction set which gives the same 32 bit ARM instruction performance but in 16 bit format. 


Definition: 
***********
DIFFERENCE = PROCESSOR VS CORE:

6. Processor is nothing but a core + lots of supported peripherals. core is basically a ALU where data computation takes place and result will be generated.  
   Processor is also called as CPU and core is called as CPU core. A Processor may contain many cores. (BINGO!!!)
     
DIFFERENCE = PROCESSOR VS MICROCONTROLLER:
eg, STM32F446RE is the microcontroller with the ARM-cortex-M4 CPU.   
*********************************************************************************************************************************************************************************************




SECTION II: HARDWARE AND SOFTWARE REQUIREMENTS 
***********************************************



SECTION III: IDE INSTALLATION 
*******************************
1. About IDE 
2. Installing IDE on windows
3. Installing IDE in ubuntu 
4. Embedded Target used in this course
5. Documents



SEC IV: EMBEDDED HELLO WORLD 
******************************
1. Creating the helloworld project
2. Printf using SWV
3. Testing helloworld program on target 
4. Printf using semihosting 





SEC V: Access level and operation modes of the processor 
*********************************************************
1. Features of Cortex Mx processor
2. Operational modes of the Cortex Mx processor 
3. Operational modes code demonstration
4. Access level of the processor 
5. Core registerPART -1 -Talks about different registers 
6. Core registerPART -2
7. Core registerPART -3 
   Check the Cortex-M4 document, section 2.1.3
8. Non-memory mapped and Memory mapped registers     


Operational modes of the Processors (M0/M3/M4)

Processor gives 2 operational modes
1) Thread Mode
2) Handler mode 

1-> All the application code will execuet under the "Thread mode" of the processor. This is also called as the "User Mode"
2-> All the exception (interrupts) handler works on the "Handler mode" of the processor. 
3-> Processor wil starts with the "Thread mode"
4-> Whenever the code meets the system exception or any external interrupts then the core will changed its mode to the handler mode in order to service the ISR associated with that system
    exception or the interrupt.
    
Difference between the thread mode and the handler mode:
********************************************************
-> In the handler mode, we have complete access to the processor. We can use the processor for our purpose. That is the priviledge mode access 
   All the thread mode also has the priviledged mode access. The only difference is that we can't have the handler mode code as unpriviledged where are we can for the thread mode.



SEC VI: ARM GCC INLINCE ASSEMBLY CODING 
*****************************************
1. ARM GCC Inline assembly coding part-1
2. ARM GCC Inline assembly coding part-2
3. ARM GCC Inline assembly coding part-3
4. ARM GCC Inline assembly coding part-4
Defintion: 
**********
-> Inline assembly code is used to write pure assembly code inside a ‘C’ program.
   Assembly instruction : MOV R0,R1
   Inline assembly statement : __asm volatile(“MOV R0,R1”);
-> Different compilers has different syntax
-> The ISA document will tell about different instructions such as load, store, move and others and    how the source, destination and operations and how they are used. 
-> We must study them when we start writing the ASM code.
-> Note that we use the general registers for data movement and they are actual used directly by the processor 
-> Note that in the "debug" folder there is a file named as "fileName.list" which contains the disassmenly of the code.




SEC VII: RESET SEQUENCE OF THE PROCESSOR
*****************************************
1. Reset sequence of the processor

Note: In the case of the windows there is already this "ADD PATH TO THE ENVIRONMENT VARIABLE OPTION" while installing from the installer. 
Incase the case of the ubuntu, I had to explicitly set the path to the bnary file of the toolchain. 
     
Note that I have downloaded the IDE and kept it in the place where I am keeping all the resources of the STM board. 
Need to search for the board next time. 




SECTION VIII: ACCESS LEVEL AND T-BIT 
************************************
1. Demonstration of access level of the processor
2. Importance of T-bit of the EPSR
-> T bit basically decides which ISA to use, either the ARM ISA or the Thumb ISA




SECTION IX: MEMORY MAP AND BUS INTERFACES OF ARM CORTEX Mx PROCESSOR
********************************************************************
1. Memory Map of the processor (processor addressable memory)
-> Code memory is where we store the instruction and 
-> Data memory (SRAM) is where we keep the temporary data of the program.
ARM Cortex has 32 bit address and data channels so it can store up to 4GB different memory location values, so from 0 to FFFF.
That range is process addressable memory range.

2. Bus Protocols and bus interfaces
Arm Cortex M4 processor has 4 bus interfaces, all are based on AHB protocol. I-bus, D-bus, S-bus and PPB(Private peripheral bus) bus 
D and I interface buses are used to communicate with a code and memory to fetch instruction and data 
simulatenously.
S-bus interface is used to communicate with the SRAM  and to the on-chip peripherals of the microcontrollers. 
Private peripheral bus is used ti talk to the private peripheral bus region registers. 

3. Bit banding
It is the capacity to address a single bit of memory address. This feature is optional i.e MCU manufacturee supports it or many mot support this feature. 

Byte addressing: Address is of size 1 byte and the total no of address is 2^8 i.e 1024 (1kb) addresses
1 byte will be loaded once we load it.
B -> LDRB (Load byte)
HW(2B) -> LDRH (Half word)
W(4B or 32 bits) -> LDR (Complete word)
Note: Half byte access or accessing to the bits are not possible in this processor. So the lowest addressable thing is byte. 

But using the but banding techniques we can address individual bits by using a unique address. That is bit addressable or bit banding. 
Advantage: We can individually modify each single bits without modifying other bits of the byte snice it has a single unique address.  

This feature is only available for the SRAM and the peripheral regions and not for other regions. Also initial 1MB in SRAM and peripheral is only bit bandable and not other regions. 
This address regions is modified by the alias address.

Atomic operations means-> Not affected by the system exceptions and interrupts of the processor

4. Bit band excercise (since it is BIT addressable)  -> IMPORTANT CONCEPT 
Calcualtion of the bit band alias address



SECTION X: STACK MEMORY AND PLACEMENT 
**************************************
1. Introduction to stack memory -DONE
In ARM Cortex Mx processor, stack consumption model is Full Descending (FD)
Address will keep on decreasing to the lower address.

2. Different stack operation models -DONE

3. Stack placement
Linker script decides the boundaries. Such as where should data section whould start in the RAM and also captures the end of data section.

4. Banked Stack pointer registers of ARM Cortex Mx
Cortex M Processor physically hAS 3 STACK POINTERS
a. -> Stack pointer or current Stack pointer (SP), Main Stack pointer (MSP), Process stack pointer (PSP)
b. -> After processor reset, by default, MSP will be selected as current stack pointer. That means, SP copies the contents of MSP
c. -> Thread mode change the current stack pointer to PSP by configuring the CONTROL register's SPSEL bit. 
d. -> But Handler mode code execution will always use MSP as the current stack pointer. That means that, changing the value os SPSEL bit being in the handler mode does not make any sense. 
      The write will be ignored. 
e. -> MSP will be intialized automatically by the processor after reset by reading the content of the address 0x0000_0000
f. -> If you want to use the PSP then make sure that you initialize the PSP to valid stack address in your code 

5. Stack exercise
Note that the startup file contains the reset handler, interrupt handler and vector tables information, linker script symbols(actually addresses) 

6. Stack exercise contd.

7. Function call and AAPCS standard

AAPCS standard stands for the ARM Architecture procedure call standard 
_________________________________________________________________________
The AAPCS standard describes procedure call standard used by the application binary interface(ABI) for ARM architecture
The AAPCS defines how subroutines can be separately written, separately compiled, and separately assmebled to work together. It describes a contract between a calling routine and a called routine. 

Procedure Call Standard for the Arm Architecture(AAPCS)
____________________________________________________________
• R0, R1, R2, R3, R12, R14(LR) registers are called "caller saved registers, "it's the responsibility of the caller to save these registers on stack before calling the function if those values will still be needed after the function call and retrieve it back once the called function returns. Register values that are not required after the function call don't have to be saved.

• R4 to R11 are called "callee saved registers." The function or subroutine being called needs to make sure that, contents of these registers will be unaltered before exiting the function

8. Stack activities during interrupt and exception 
Note that the interrupt and exceptions need not worry about the AAPCS rules since there is no caller for them. So we can write an interrupt and exception handler as normal 'c' function without worrying about the rules. 
Registers are saved automatically by the process hardware. And that we call as the stack frame.   
The registers that are saved are R0,R1,R2,R3,R12, LR, PC and XPSR together called as the stack frame.

Stack initialization
• Before reaching main
• After reaching the main function, you may again reinitialize the stack pointer SO that the vector table is having the valid address. 

*********************************************************************************************************************************************************************************************


Section -XI:
************
Exception model of the ARM Cortex Mx processor
**********************************************
1. Exception model 
There are two types of exception
(a) System exceptions and (b) Interrupts

System exceptions are generated by the processor itself internally.  
Interrupt come from the external world to the processor. 
Collectively they are called as the Exceptions  	
Whenever the processor core meets with an exception, it changes the "Operational mode" to "Handler mode"
There are 15 different system exceptions supported by the Cortex-M processors and 240 interrupts. In total there are 255 exceptions.


2. Different system exceptions 


3. NVIC (Nested Vector interrupt controller)
   It is one of the Cortex M processor core
   System control block is used to control the system exceptions where as the NVIC peripheral is used to control the 240 interrupts 


4. NVIC Registers
5. Peripheral interrupt excercise
*********************************************************************************************************************************************************************************************


Section -XVII:
************

A processor that is executing Thumb instructions is said to be operating in Thumb state. A Thumb-capable processor that is executing ARM instructions is said to be operating in ARM state.
The Thumb instruction set is a subset of the most commonly used 32-bit ARM instructions. Thumb instructions are each 16 bits long, and have a corresponding 32-bit ARM instruction that has the same effect on the processor model.


1. Bare Metal Embedded 
2. Cross compilation and toolchains 
3. Installing GCC ARM cross toolchain 
4. Build process

5. Compilation and compiler flags 
6. Makefile 
-> Makefile is used to automate the build 
   {arm-none-eabi-objdump.exe -D main.o > main_log} to get the disassembly of the file 

7. Analyzing the relocatable object files 

8. Code and data of a program 
-> Data sections contains only the data and not the instructions. So dont check that part of the data as the instruction. 
-> Code will be stored in the Code memory which will be stored in the Flash memory
-> Data can be stored in the Flash or in the RAM depending upon the nature of the data. Constant data wlll store in the flash memory (Read only memory) and non-constant data willl
   be stored in the RAM, eg (Variables in the RAM(which is read and write both))
-> ROM is Flash 

9. Linker and Locator 
   The final linking will be done by the linker and locator with the help of the linker script provided by me. 
   They will take all the elf file (which is .o file of various source files) and generate the final ELF file which is used by concatenating all the text section, data section and others. 
   The final ELF file is what we all want.
   
   Ah!!. And the final ELF object file is what will get stored in the ROM(flash). The executable will be stored in the memory permanently. 
   Note that the initial addresses of the ROM or code memory is occupied by the Vector table. We have to write the vector table and that we have to write it in the startup file. 
   This is one of the requirements of the firmware which we use for the ARM Cortex Mx based processors. 
   The intialized global and the static variables are stored in the ROM, which needs to be copied into the RAM which will be done by the Startup code. 
      
   The startup file should copy all the data section contains from the FLASH to the SRAM. The process of copying is called the C startup. 
   The startup code then also can reinitialize the stack pointer and the C startup code calls the main function. 
   
   Note that the startup code should know the initial address and size of the data section from the ROM, so that it can copy from that to the SRAM. 
   That particular symbols are called as the _sdata and _edata. We need to create those symbols
   Startup code will need these boundary values to copy the data.  
   
   
10. Different data of a program and related sections      
   How to obtains these boundary values will be talked here?  
   Static data are like the private data. 
   Local intialized static data will be treated as the global data and which is a private data to a function. 
   
   Note: In the world of microcontroller everything is real and nothing virtual. 
   
11. .bss Vs data section
    .bss contains all the unintialized global and static variables. Not stored in the flash unlike the .data section.
    But we must reserve RAM space for the .bss section by knowing its size and initialize those memory space to zero. This is typically done in the startup code. 
    Linker helps you to determine the final size of the .bss section. So, obtain the size information from a linker sript symbols.
    
12. Startup file of Microcontroller 
   
13. Writing startup file of Microcontroller from sractch part-I
14. Writing startup file of Microcontroller from sractch part-II 
15. Writing startup file of Microcontroller from sractch part-III        
    Start up file can be created in .c or .s file since it is an ASM file. 
         
    Start up file contains 
    (1) Vector table for the microcontroller. Vector tables are MCU specific
    (2) Start-up-code which initializes .data and .bss section in SRAM
    (3) call main()    

    Startup code contains the Reset handler which does the following
    (1) Copy .data section to SRAM
    (2) Init the .bss section to zero in SRAM
    (3) Call main() function 
    
    While copying the data from the flash to SRAM, we need to know the boundaries and size of the data section. For that, we use the information from the linker file. 
 
16. Writing linker script from scratch part -1 and part -2
    Linker script is a text file which explains how different sections of the object files should be merged to create an output file
    Linker and locator combination assigns unique absolute addresses to different sections of the output file by referring to address information mentioned in the linker script
    Linker script also includes the code and data memory address and size information.
    You must supply linker script at the linking phase to the linker using –T option
    
    Linker scripts commands
    • ENTRY
    • MEMORY
    • SECTIONS
    • KEEP
    • ALIGN
    • AT>
 
    VMA -> Virtaul memory address
    LMA -> Load memory address
    They are used in the SECTIONS part

17. Location counter    
    The boundaries of the data section can be found in the linker script which then can be passed in the C program.
    Special linker symbol denoted by a "." called as the location counter.
    This is used for tracking and defining the boundaries of various sections.
      
18. Linker Script symbol
    Note that the symbol is not same as the variable. I will store the address and not values. 
    This is used for the tracking and defining boundaries of various sections. 
    
19. Writing linker script from scratch -part 3
    Location counter always tracks VMA of the section in which it is being used. 
    
20. Linking and linker flags
    WE can pass the linker script (*ld) using the -T flag. 
    example
    arm-none-eabi-gcc -T someLinkerFile.ld *.o  -o final.elf 
    
21. Analyzing the ELF File 
    We can instruct the linker to create a special file called as the map file. 
    Using the map file, we can analyze various resource allocation and placement in the memory.
    
    Command to generate is add one more flag which is:
    -Map = final.map  (add it in the Linker flags)
    Also, sometimes we need to explicitly tell that it is the linker command so we need to add one more flag which is the -Wl
    So, the final command becomes 
    -Wl, -Map = final.map 
              
    Note: Its better to align the memory (something like 0,4,8,12,16).
    We can use the ALIGN command to align the location counter for the word alignment. 
    
    To check how the different sections are distributed, we can use the command below as
    "arm-none-eabi-objdump.exe -h final.elf" 
    
    
    
22. Implementing the Reset handler
    If we want to see all the symbols created by the application, we can use the command
    
    Command is: "arm-none-eabi-nm.exe final.elf"
    Every loadable or allocatable output section in a binary has two addresses: VMA (Virtual Memory Address) and LMA. The VMA is the address the section will have when the output file is run. The LMA  
    is the address to which the section will be loaded. In many cases, VMA and LMA are the same.
    
    

23. OpenOCD and debug adapters
    Once we have the final elf file, we need to download and debug executable (flash into the memory   of the microcontroller)
    
    There are two methods to download executable to Target:
    1. In-circuit Programmer/Debugger (Debug adapter)     
       We have to connect the target to the PC via debug adapter. Called as the IN-circuit programming. The debugger called as the In-circuit debugger. 
       It converts a host protocol to the native target protocol. 
       
       (a). For example, the debug adaptar may support the SWD or JTAG based debug protocol, thst we call as the target interface. 
       (b). Because target understands the debug protocol like SWD or JTAG. Hosts understands interface such as the USB or Serial port, or parallel port or something like that. 
       (c). The debugger does the conversion, It converts the host interface to target interface protocol. 
       (d). On the host side we have to run some application to talk to this debug adapter thereby we ca talk to the target. Talk meaning we can send commands to the target, can send executables to the target. we can debug the board and we can do various things. 
         There are many such applications and one such application is the OpenOCD.
         
         Two main goals of the OpenOCD:
         1. Download the exectable into the internal flash of the microcontroller
         2. Debug the code using the GDB.
         
   The main work of the programming conversion is that it does protocol conversion. For example, commands and messages coming from the host application in the form of USV packets will be converted to equvalent debug interface signalling (SWD or JTAG) and vice versa.
   
   Some of the board has the embedded debugger in their own board. 
   
   FLOW OF THE PROCESS:
   ********************
   HostPC(OpenOCD runs here) <=> It runs some driver here <=> USB <=> SWD or JTAG Based Debug adapter <=> JTAG pins or SW pins <=> Target Board
   Board contains the Microcontroller. SWD needs 2 pins, JTAG needs atleast 4 pins. 
   The final aim will be to use the Flash memory, SRAM and Core of the microcontroller. 
   
   
24. Steps to download the OpenOCD
    Command for the using it is:  "openocd -f board/cfg_file"  ->Target file" 
                                   "make load" for loading the target into the system. 
    We can use the telnet client for Windows, telnet package for ubuntu and gdb client for Mac. 
    
    
25. Using GDB Client   (OpenOCD server and gdb client or telnet client from putty in windows)    
    To use the arm toolchain gdb command, we need to use 
    "arm-none-eabi-gdb.exe"  => This will take me to the gdb command line window
    "monitor" keyword is always preceeded before the command for differentiating between the gdb client command and the openocd command. 
    
    Openocd general commands:
    https://openocd.org/doc/html/General-Commands.html 
    
    We can use the breakpoints using the keyword -> "monitor bp"
         

26. 'C' standard library newlib and newlib-nano 
    Newlib us a 'C' standard library implementation intended for use on embedded systems, and it is introduced by Cygnus Solutions (now Red Hat)      
    It can be use with no OS (bare metal) or with a lightweight RTOS
    It ships with the GNU ARM toolchain installation as the default C standard library.
    (a) libc.a is the Newlib 'C' standard library inside the ARM toolchain 
    
    Newlib-nano
    Due to the increased feature set in newlib, it has become too bloated to use on the systems where the amount of memory is very much limited. 
    To provide a C library with a minimal memory footprint, suited for use with micro controllers, ARM introduced newlib-nano based on newlib.
    (b) libc_nano.a is the Newlib-nano 'C' standard library
    
    Also note that, librdimon.a and librdimon_nano.a are the semi-hosting library that is used for console IO operation like printf
    and the "rdimon.specs, pid.specs and nosys.specs: are the Spec files for the linking stages to these libraries.
    
    "printf() => Newlib-Nano => stubs()"  [ These are low level specific system call implemenyation, Implementing the system calls functions depends on the target and often the hardware/embedded  
    engineer role is to write that one]
    
    
26. Integrating system calls
    The spec files that defines "semi-hosting" or "no semi hosting" is used as one of the arguments in the linker command.
    spec file says:
    It is a file containing switches to override standard defaults for various build components such as the compiler, assembler and linker. For example it can be used to replace the default C library.
    Also linking to standard C library or not. 
 
27. Section merging of the standard library
    Need to all the text, data, bss sections using the linker script. 
    
 
28. Fixing linker script to resolve hardfault 
    
29. Semi-hosting 
    Semihosting is a mechanism that enables code running on an ARM target to communicate and use the Input/Output facilities on a host computer that is running a debugger. Examples of these facilities 
    include keyboard input, screen output, and disk I/O.
    It is a techinique by which we can see the printf messages on the openocd console. 
    Semi-hosting library will provide all the low lovel system calls if it is used.
