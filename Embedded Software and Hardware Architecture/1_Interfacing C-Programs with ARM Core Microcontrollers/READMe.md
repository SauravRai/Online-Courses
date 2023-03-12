
Lecture 1: Architecture-Software Interface
******************************************

-> It is important as a software engineer that you attempt to develop code to be architecture independent as much as possible. This is because it allows us to have portable and reusable code for other platforms and architectures.

-> It is nearly impossible to write architecture independent microcontroller program. In fact, embedded systems really require the software designer to know as much about the architecture and platform as possible. This allows us to optimize our designs, utilize certain features or hardware elements in an application, and create portability between different platforms.

-> We discussed some basic high level software that has platform dependencies, like the Linker File with the program coded program data. The way that a compiler allocates program code and data memory is highly architecture dependent as there are certain specifications that map the C programming constructs to the physical memory more than just the Linker File. 

-> How does your code and your data get oriented in memory? How does your code and data get moved between the CPU and the memory interface? These are barely introduced, but they have some serious implications on your program efficiency. There are many more architecture specific concepts an embedded software engineer needs to know about, more than just this memory interaction and allocation.

-> In addition to the engineer, your compiler must adhere to these same specifications in order to compile and install a statically linked executable into a platform. These specifications are referred to as an application Binary Enterface, or in the case of embedded system, an Embedded Application Binary Interface, or EABI. An EABI is the specification that will provide us the details on the interoperability of our program with other statically linked programs and the underlying architecture.

-> Let us highlight some of the basic EABI specifications you might read about. First and foremost, the EABI will specify information on how your program must be complied. The translation of high-level to low-level language has specific requirements on things like register use and word size. The word size is the operand size the Instruction Set Architecture was defined around. All operations are written to perform actions on data of this size most optimally.

-> There are specifications on how program code and data are physically sized and placed into memory. The C programming language does provide us with data types, but unfortunately these are not necessarily portable. Some data types have varying size. And a compiler may even implement these types as different sizes optimized for its architecture. The C standard types are actually not the standard way developers declare data, as they can be ambiguous. Even further, allocated information will be aligned within specific boundaries with memory.

-> There are also addressing modes that tell you how your program operates on memory. This specifies information like how your program reads and writes program data. The assembly instructions need to know where that data is and the best way to access it. In addition, the compiled segments that we discussed regarding a Linker File and the outputs of building, are also specified in an ABI. 

-> The calling conventions we discussed briefly with the stack memory segment, are specified in the ABI as well. This gives details on how routines are called and returned from. It will provide responsibilities on what needs to be saved or restored by the calling routine, and what needs to be done by the routine being called. This process is directly related to the implementations of the stack and the CPU registers. 

-> Finally, the ABI will also specify which libraries or helper software functions that perform more difficult software algorithms that you can write and see, but not necessarily are supported by an architecture. Hardware without floating point support must implement all Floating Point Math with software routines. If there are existing statically linked libraries like the C-standard Library, this will also specify how executables need to interact with the standard library

-> All of these examples were just basic introductions into some architectural requirements that the compiler handles behind the scenes. Developers need to know these too, as some serious bugs can be introduced without understanding how your hardware will implement your C program code on your platform.

-> The first module of this course will give you your first step into writing C programs that are optimized for an architecture. By knowing the details of how memories manage, how to define portable and explicit data, and how to interface with peripheral memory to configure our micro-controller, we will be nearly ready to start writing an embedded application.
*********************************************************************************************************************

Lecture 2: Word Size and Data Types
************************************
-> In this video, we will discuss an architecture word size and the data types. An architecture is designed to implement assembly instructions. Depending on    the type of architecture, these instructions can be extremely complex, like in the case of a CISC machine, or these instructions can be very simple, like in the case of a RISC machine. 
   (RISC VS CISC example described https://www.youtube.com/watch?v=vIphiGCWzIU)

-> ARM, or advanced risk machine, contains many different versions of its architecture; however, we often refer to ARM as a 32-bit or a 64-bit architecture. These numbers represent the word size for two different versions of their RISC instruction sets.
 
-> Physically in hardware, CPU registers and assembly operations will be designed around these sizes. 

-> In C programming, you can define operations around a variety of sizes that do not necessarily map to the word size. However, every operation in C utilizes the word size and the instruction set architecture or ISA. 
 
-> The fundamental unit of work for a processor is the instruction and the word size. The instructions are assembly operations that perform a small amount of work in a CPU. These instructions are fetched from the code memory, decoded and then executed by the CPU. Operations can range from arithmetic to logical to controlling program flow and load store operations of memory. The word is the size of work that each operation performs. For example, an architecture with a 32-bit word could perform an arithmetic add; these mean that the architecture will able to add two 32-bit numbers in one instruction.
 
-> The general purpose registers in the CPU will be sized the same size as the word size. This is because these registers are where the operands are stored for each instruction. 

-> The Cortex-M0 has 16 general purpose registers, most of which are available for use by the programmer. Some are reserved general purpose registers like the link register, the stack pointer and the program counter. The architecture is built around performing the operations on the size of the word with these registers. 

-> However, that does not mean you cannot perform arithmetic or logic operations from C programming with larger or smaller sizes than the word. We oftenhave op erations that do 8-bit, 16-bit or even 64-bit math on a 32-bit architecture. The ISA may have specific assembly operations for these smaller size data actions or it may require multiple 32-bit operations to do larger sizes. 

-> The word size is often confused with the instruction size or the bus width. The ARM Cortex-M series has a 32-bit instruction size. However, ARM can also be configured so that the CPI core can operate with a 16-bit instruction size. This is referred to as the thumb architecture. Thumb is just a reduced number of ARM instructions at a smaller instruction size. The size of instruction can limit the number of supported operations and different features       within each individual operation. These operations are usually referred to as an operation code or an opcode. 

-> The bus width for ARM can vary depending on the different bus architectures you're using. You would typically see a bus width at least the size of the word or the instruction. This helps with efficiency because instructions are read from memory just like data is read. You would want to be able to fetch an instruction from memory in one memory fetch. The bus width does not necessarily have to be the word size, but the bus refers to many things. A bus will contain both data bits, address bits and control bits. 

-> The data bits can be configured for ARM architecture, but usually for sizes equal to or larger than the word size. 
   The address bits would usually map to the size of the word, as this is the way that we will address our microcontroller components within a memory map.Just like a pointer holds an address for a piece of data, an address must be provided to fetch a specific instruction at a given address. The address is referenced by a program counter and the instruction that is being execute is put into the instruction register. 

-> Now you might be asking how does the word size relate to a C program type? When you write C programs, you have utilized a handful of data types and type modifiers for your variable declarations. These have specified size and sign of a type. The types included chars and integers. The modifiers included signed, unsigned, short and long. These types are somewhat ambiguous when it comes to physical sizes and memory. The C standard only guarantees a minimum size that each of these types might be. It's up to the architecture and the compiler to actually sign the sizes at build time. For instance, an integer can be 16-bits or 32-bits, depending on the architecture. The length and size ambiguity does not suffice for software engineers. Instead, we utilize some special types to help provide more insight on what exactly you are reserving in your architecture. These are referred to as the standard integer sizes and are standard practice to use. 

-> There are three forms to these standard references. These include types that describe an exact size, a minimum size and a fast execution size. You can find these defined in your stdint.h library file. The standard types have much more clear definition. They start with a u-int or an int, which represent an unsigned integer or a signed integer. 
   Following this is the number of bits this type will occupy. A uint8 will represent a unsigned 8-bit type, while an int32 represent a signed 32-bit integer. The underscore t at the end just indicates that this word represents a type. 

-> In the standard int file, you will see two other types declared that look very similar to our u-int and int formats. These include the int_fast types and the int_least types. These are slightly different from the compiler perspective. The least type just requests that the compiler select a storage amount of at least n bits. So int_least8_t would be assigned at least 8-bit type. The fast type indicates that this data should be represented in a way that the    access and use of this type occurs as fast as possible in an architecture with at least n bits. So int_fast8 type would be implemented with at least 8-bits. However, it would likely be sized up to the size of the word. These types are set by the compiler or by using the typedef C keyword. 

-> The typedef keyword allows us to create our own types and use them in a short form just like we do with ints, chars and floats. These are extremely helpful for defining structures, enumerations, or unions with custom type names. If we were to open an example of the standard int file, you will see these standard types defined and you could see the typedef keyword is used to map the u_int8 type to the unsigned char type. And the int32 type is type-defined as a signed long int. Many of the tenets of good software design were addressed in this video. 

-> Understanding the architecture word size can help us choose data types that best utilize the architecture. By selecting smaller data sizes, we might be using less memory; but that can be causing excess overhead in operations. Larger types than the word will cause extra operations to do loads and stores of that data as well as the actual operation on that data. In C programming, the types we select can vary or are architecture and compiler-dependent. By utilizing the standard types, we can create unambiguous code that helps us create and write more portable and efficient software.
*********************************************************************************************************************
Lecture 4: Interacting with the Memory

-> A microcontroller involves some type of memory in every single instruction. These can vary fetching an instruction from flash, interacting with a peripheral, manipulating a CPU register, or reading and writing the data memory. 

-> We as the C programmer never really know the details of how these memory interactions occur. We only know that various configuration info, or program data, lives at a specific address. 

-> Behind the scenes of each address, there's some complex hardware interactions that translate this addressto the piece of hardware. 

-> We have many types of memories in a microcontroller. There's flash memory, which primarily stores our code, but can also store some data. The data that we store in code memory represents our constant data and initialization values for run-time variables that get stored in SRAM. 

-> SRAM is primarily run-time read-write memory that is used for many different types of data, such as locals, globals,static memory, and dynamic memory storage. 

-> There are many peripheral devices. Some that are private peripherals with specialized access and some that are general use, like timers and serial devices. Lastly, there are many core CPU Registers, both special purpose and general purpose. Core CPU Registers have their own identifiers and their own address space, as they live directly inside the CPU core. The general purpose registers are the working units for each instruction. The special purpose registers give us the ability to track our program state, like the stack pointer, the program counter, and the program status registers. We are not given direct access to these CPU Registers from a seed programming interface. Instead, we need to use something called Inline Assembly, mixed with C program routines to read or write these from a high level language. 

-> The compiler will automatically convert your high level code to use these registers accordingly. We can perform many different operations in the CPU, such as logical, arithmetic, or even comparison operations. Each of these require the general purpose registers to perform their function. The CPU Registers are too small to store all of our program data. Thus we have memory like Flash and RAM to store needed information. We need to transfer information back and forth between these memories to get them into the CPU. 

-> For instructions that operate on data, we first load data from RAM into a general purpose register. We can then perform our operation. We then store back    that data to memory after we're done with the operation. All processing occurs inside the CPU core and not external to the CPU core. This type of architecture as a Load-Store Architecture. 

-> Unfortunately, we cannot operate directly on memory. The operation needs to occur inside the CPU. There are also two instructions that are needed to get the data to and from that location and those are the load and store. This type of process we refer to as a Read-Modify-Write. We first must load the value into the CPU in order to modify it. Then we must write it back after it's been modified. Regular reading and writing data to and from memory is a lot of overhead for the CPU, making our program less efficient. The compiler will attempt to try and limit data being repeatedly being    loaded and stored. And try to retain that value in the registers for a longer period of time. 

-> However, you cannot keep data in the registers for forever. In some cases, we do not need to store them back. We can just perform a Read. Read-Modify-Write is regularly needed for interacting with Peripheral Registers. We often want to preserved most of the Peripheral Register. In this case, overhead can get worse. If we need to manipulate any data that is smaller than an eight bit chunk, this process is called bit manipulation. 

-> Bit manipulation is required if you need to Read-Modify-Write a value from memory, but not the entire register, just a few bits. Typically, memory is designed to be only byte addressable, as bits are just too small to assign an address to. The architecture gives us the ability to load and store a byte, half word and word size type of data. There are not usually instructions that allow us to do bit-level loads in stores. 

-> However, some hardware might be added to a CPU to help facilitate Read-Modify-Write process for bits. ARM architecture provides something called Bit-Banded Regions. These are sections of the address space where each address maps to a particular bit in a section of SRAM or a section of peripheral memory. 

-> Bit-Banded memory operations are good for avoiding race conditions that could be introduced by doing a Read-Modify-Write operation. At any point in time during that operation, the state of a microcontroller can change and interrupt this process. By using Bit-Banded operations, the manipulation is handled in hardware and is therefore atomic. We will discuss atomics in more detail later in the course. 

-> So how does your data get to and from the CPU? Our previous diagrams of memory system showed a generic interface to a microcontroller via one bus. This is extremely simplified version compared to what our cortex and processors are doing. We actually have many busses that our memory systems in the CPU interact with on a microcontroller. 

-> ARM provides a bus technology to its customers called the AMBA specification, which stands for Advanced Microcontroller Bus Architecture. Regardless if our data is a word, half word, byte or even a bit, they use the same interface. For our cortex and processors, our bus interface is sized to 32 bits. 

-> But the AMBA specification allows allows this bus width to vary in size. There are many types of different busses that uses this specification internal to the microcontroller. These include the system bus, the flash busses and the peripheral bus. These busses use a mixture of the bus architectures AHB and APB. AHB stands for AMBA High Performance Bus. 

-> This bus architecture is used multiple times inside of an ARM microcontroller. The CPU core has two AHB busses that interact with both internal private peripherals and external private peripherals. 

-> Internal private peripherals include things like the system control block, memory protection unit, and the nested vector interrupt controller. External peripheral bus connections include debug hardware. Usually interactions on the private peripheral bus or PPB, must have privileged access to read or write to the devices they are connected to. 

-> AHB buses are used in more than just private connections. There are two more AHB buses used to connect the CPU to code memory and the CPU to data memory. The bus that connects to the SRAM is referred to as the system bus. In microcontrollers of the Cortex-M3 or Cortex-M4, you may have two different AHBbusses i nterfaced to Flash Memory, the I-Code and the D-Code. I-Code is used for fetching instructions, while D-Code is used to fetch data from code memory. By using two interfaces, we can fetch our constant data simultaneously with our code instructions from Flash Memory. 

-> By using different Busses for SRAM and Flash, each can be configured to run at different frequencies optimized for power use and the memory architectures they are connected to. APB stands for Advanced Peripheral Bus. This bus is a Low Bandwidth Bus to interact with the peripheral devices, using group peripherals like timers, communication box and analog-to-digital converters. 

-> One complicated aspect of the APB is it is not directly connected to the CPU. When you need write to the normal peripherals, data leaves CPU on the system bus and then is transferred to the peripheral bus via a bridge. The different bus interfaces that we discuss, are mapped to different memory
regions in our address space. 

-> By writing C code that uses pointers to our various end devices like SRAM or Peripheral, the architecture figures out how to route our data based on the address. Sometimes this data goes to extremely sensitive system control interfaces and sometimes this data goes to really slow general peripherals. Since our CPU is a Load-Store Architecture, these various bus interfaces are used regularly during the execution of our program.
********************************************************************************************************************
















