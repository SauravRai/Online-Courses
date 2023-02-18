
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
