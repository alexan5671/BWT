Implementation of a Distributed Client-Server Architecture using TCP Sockets for Burrows-Wheeler Transform Data Processing in Python - Computer Science Laboratory Report

**Author:** Birca Alexandru Gabriel

**Istituto di Istruzione Superiore “Archimede” - Treviglio**

---

## Abstract

This report describes the development of a local distributed system based on a client-server architecture using TCP sockets in Python. The main goal of the project is to implement the Burrows-Wheeler Transform (BWT) and its inverse (IBWT) algorithms for text string manipulation and data compression preparation. The system is split into three main components: a core logic module (`Main.py`) containing the transformation algorithms, a network server (`server.py`) that handles incoming requests and processing, and an interactive client (`client.py`) for user input and output presentation.

---

## Introduction

In the context of the computer science laboratory, we developed an application capable of applying the Burrows-Wheeler Transform (BWT) to user-supplied text strings. The BWT is a fundamental algorithm in data compression (commonly utilized in compression tools like `bzip2`) because it permutes character sequences to group similar characters together, increasing text redundancy and compressibility.

To simulate a real-world network service, the computational logic was separated from the user interface using a client-server paradigm over the TCP transport protocol. Python was chosen as the programming language due to its powerful string manipulation capabilities and the built-in `socket` library, which allows for straightforward network communication management. Information and technical guidelines were retrieved from official documentation sources such as programming guides like Real Python and presentations made by Mazzocca Antonio.

---

## Methods

### System Architecture and Modules

The project is divided into three separate Python script files:

1. **`Main.py` (Core Logic):** Contains the core algorithms for transformation.
* `bwt(s: str)`: Generates all cyclic rotations of the input string, sorts them lexicographically into a matrix, extracts the last column (`bwt_str`), and records the row index of the original string (`original_index`).
* `ibwt(bwt_str: str, original_index: int)`: Rebuilds the original text iteratively by prepending the BWT column, sorting the table alphabetically at each step, and retrieving the target string using the saved index.


2. **`server.py` (Network Server):** Sets up a TCP socket listener on the local loopback address (`127.0.0.1`) and port `65432`. It accepts incoming client connections, appends the mandatory end-of-string marker (`$`), processes the text via `Main.py`, packs the results into a dictionary, serializes them using `json`, and sends the response back.
3. **`client.py` (Network Client):** Collects user input from the console, establishes a TCP connection to the server, sends the raw text, receives the JSON-serialized package, and displays the processed results.

### Tools and Libraries

* **Development Environment:** Linux Terminal/Neovim with custom configuration for programming.
* **Gemini AI:** essential for learning json and support on the writing the server side
* **Programming Language:** Python (v3.10+).
* **Standard Libraries:**
* `socket`: For low-level TCP/IP networking communication.
* `json`: For structuring and transmitting data objects between client and server.



---

## Results and Discussion

Testing the application with sample text (such as `"banana"`) demonstrated that the BWT algorithm functions correctly. By appending the end-of-string marker (`$`), the server successfully generated the permuted string and its corresponding row index.

The reverse transformation (IBWT) executed on the server and verified at the client end successfully restored the exact original text, confirming data integrity across the network boundary. The combination of TCP sockets and JSON serialization proved to be reliable for local communication.

---

## Conclusions

The project objectives were fully achieved by successfully integrating string manipulation algorithms, modular programming principles, and network socket programming. The distributed architecture ensures a clean separation of concerns between business logic and user interaction. Potential future improvements include extending the server implementation using the `threading` module to support multiple simultaneous client connections.

---

## References

* Real Python - *Socket Programming in Python (Guide)*
* GeeksforGeeks - *Burrows–Wheeler Data Transform Algorithm*
* Mazzocca Antonio - *Teoria - 03 Comunicazione Client-Server con socket TCP*
