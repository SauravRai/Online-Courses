Video 1:
Introduction to Memory Organization

-> Registers, code memory, and data memory fundamentally require different physical characteristics. There are many features that we want for memory, such as high capacity, low power, low latency, and high reliability. The closer to the CPU the memory is, the faster you need it to be. However, these features often come at a price, and it forces us to utilize different types of memories. Some with low latencies, also with smaller capacities. Therefore, you usually build a hierarchy of memory systems to help with this. If you need more memory, or a different capability, you may have to change chipsets as with different hardware. This is why multiple chips were offered in a subset family with varying amounts of internal memory capability. So they meet a variety of applications with different price points.

***************************************************************************************************************
Video 2:
Memory Architectures

-> An embedded system is defined to be a computerized system with a specific function. This could be implemented purely digitally or with a processor and    some software.  

-> A process of writing a program and then compiling an executable is only a part of this design process. We need to install this executable, and it needs to    be installed into physical memory. And not just any memory, memory that can retain the software programs so they can be run over and over again. This    program contains both operations in upper ends that need to be processed in order to meet a desired functionality. 

-> The ability to retain a program, execute it and operate on data are just three of the characteristics of memory that we need to discuss further.

-> Memories come in many different forms and characteristics. Knowing the features of memories can help us optimize our software and understand how it    interacts with hardware.

-> We need to provide the controller a minimum two to three pieces of information such as Read/Write, Data, Address, etc depending on the type of operation      we are intended to perform on the memory. 

-> The most important characteristics about memory are memory capacity, volatility, access, power consumption, latency, durability, and transaction size.

***************************************************************************************************************
Video 3: Memory Segments

-> Note that all the other memory segments has one unified address space and only the registers has a separate address space (register memory)
   As for the register memory, we also need to map between the code and these platform specific registers at compile time, this occurs in something called    "register definition file" which allows address translation for external CPU segments to occur before linking.

-> All the other memory map is provided in the linker script. 

***************************************************************************************************************
