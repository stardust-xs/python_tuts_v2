# Introduction to Python

## What is Python

As per **[Wikipedia](https://en.wikipedia.org/wiki/python_(programming_language))**, "*Python is an **[interpreted](https://en.wikipedia.org/wiki/Interpreted_language)**, **[high-level](https://en.wikipedia.org/wiki/High-level_programming_language)**, **[general-purpose programming language](https://en.wikipedia.org/wiki/General-purpose_programming_language)**.*"

Well this definition doesn't really help unless you understand every single term in it. So let's break it down into smaller digestable bits.

- Interpreted language
  - Interpreting languages are the one which executes **line by line**.
  - They **don't [compile](https://en.wikipedia.org/wiki/Compiler)**, they just run (execute) the code.
  - Python, **[Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language))**, **[Javascript](https://en.wikipedia.org/wiki/JavaScript)**, etc are examples of Interpreting language.

- High-level language
  - A High-level language (HLL) means **human understandable** language.
  - They use **common english words** (natural language) to describe their functions (For example: join, import).
  - Python, **[C](https://en.wikipedia.org/wiki/C_(programming_language))**, **[C++](https://en.wikipedia.org/wiki/C%2B%2B)**, **[Java](https://en.wikipedia.org/wiki/Java_(programming_language))**, etc are examples of High-level language.

- General-purpose language
  - General-purpose programming languages are the ones which are used in **wide applications** across multiple domains and on various platforms in some form.
  - Python running on a development board like **[Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi#Software)** is an example of Python's general purpose roots.
  - Python, C, C++, **[Go](https://en.wikipedia.org/wiki/Go_(programming_language))**, etc are examples of General-purpose language.

## Why to use Python

- Well why not?
  - It's free and kinda **[Open-source](https://en.wikipedia.org/wiki/Open-source_software)**.
  - Best way to get started with any programming language is to learn from and contribute into an Open-Source community and Python has a massive pool of open-source packages.
  - Many industry grade Python based projects/package fall under an open-source umbrella.
  - It's **easy** to learn. Infact in the UK, Python is taught as the primary programming language in some Northern Universities.

- It covers most (if not all) of the **computer science** fundamentals
  - Python was built by considering **[Object Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming)** in mind.
  - Python is built upon many computer science fundamentals and supports various algorithms (For example: **[Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)**).
  - Python can be also used for building and visualizing some abstracted (no pun intended) concepts like **[Design patterns](https://en.wikipedia.org/wiki/Software_design_pattern)** (For example: Singletons).

- It is one of the **mainstream** programming languages of 2020.
  - Python has been one of the most **trending** programming languages for couple of years now because of traction it is getting in domains like **[Machine Learning](https://en.wikipedia.org/wiki/Machine_learning)** and **[Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)**.
  - Commonly used applications (unlocking phone, filtering messages/mail) have roots in Python.

- Wide variety of softwares or tools can be/are built using Python (not entirely true).
  - Since Python is a general-purpose programming language, it provides frameworks for building applications in another domain (For example: **[Django](https://en.wikipedia.org/wiki/Django_(web_framework))**).
  - Instagram being a website (web application) was built on Django. Django is a web development framework built with Python. Pinterest also has a similar back story. But **this is not completely true**, you need to understand that there are a lot of things that goes in a basic application (**[Databases](https://en.wikipedia.org/wiki/Database#Database_languages)**, **[GUI](https://en.wikipedia.org/wiki/Graphical_user_interface)**, **[Web security](https://en.wikipedia.org/wiki/Internet_security)**).
  - Python does provide frameworks or a wrapper for each of these actions but its **not perfect**.

- It is the best programming language for **automating tasks**.
  - You can literally automate each of your activities/tasks using Python (assuming you're interested in doing some hardcore research).
  - Python is **officially supported** on mainstream platforms like Windows, Mac and Linux. It has support or patches for triggering or fetching system related tasks/informations.

- It is used by many tech giants like Google, Facebook, NASA, etc.
  - Google and Facebook are **infamous** for their **[AI](https://en.wikipedia.org/wiki/Google_AI)**. Their AI is backed by many programming frameworks and Python is one of them.
  - **[Google Brain](https://en.wikipedia.org/wiki/Google_Brain)**'s **[TensorFlow](https://github.com/tensorflow/tensorflow)** is one of **best deep learning frameworks** in the industry.
  - Facebook backed **[PyTorch](https://github.com/pytorch/pytorch)** is an another deep learning framework which is **very simple** to learn and follow along.
  - Both are built on/for Python (along with dependencies with C++ and **[Cython](https://en.wikipedia.org/wiki/Cython)**.

- Many more...

## How to get started with Python

These are some ways by which you can install or try out Python all by yourselves. I've ranked them by their ease of use and comfort.

**Disclaimer:** These rankings are based on my opinion for a **beginner**, yours may vary.

- Best & most recommended way of getting Python is by a simple search on **[YouTube](https://www.youtube.com/watch?v=wp15jyylSEQ)**.
  - This method will ensure you have Python up and running on your machine **locally**.
  - If you face any issues while installing Python on your machine, you can try with other videos.

- Using a **[Colab Notebook](https://colab.research.google.com/notebooks/intro.ipynb)** on **Google Colab** (Best & quickest way to get familiar with Cloud).
  - This method requires you to have a valid Google account. All you need is to visit the above URL and click on **New Notebook**.
  - This method obviously requires internet connection and doesn't work with relative local paths.
  - The notebook or rather the entire session is deleted by Google after every **12** hours.
  - But this method is quickest way to get started for newbies.

- Naive way!
  - The most naive way to get started with Python is to visit **[Python](https://www.python.org/downloads/)**'s website.
  - This will provide you with vanilla Python **Shell** and an **IDLE** (editor for writing Python code).
  - Most of the YouTube tutorials will explain this method. Python's installation is fast, easy and free.
  - This methods provides you complete freedom on how you can configure Python to suit your needs.
  - You'll also probably need a detected IDE or a fancy editor. I suggest you use **VSCode**.

- Using a distribution like **[Anaconda](https://www.anaconda.com/products/individual)**.
  - If you want to have no fuss during the installation then go for this method.
  - Anaconda is **too much** for a new Python developer.
  - But Anaconda wraps a lot of cool packages (including the final one) by default which are catered towards Machine Learning or **[Data Science](https://en.wikipedia.org/wiki/Data_science)** roles.

- Using a **[Jupyter Notebook](https://www.youtube.com/watch?v=o6aOqkmrrb4)** (Best way for beginners).

## Key takeaways from Python

- Everything is an **object** in Python.
  - Python is an Object Oriented Programming Language, hence it treats every syntactically valid thing as an object and follows its concepts **strictly**.
  - This object can be a simple number, string or any other datatype.
  - Each assignment (using equal to **"="**) creates some object in Python.

- Python is an **interpreted** language.
  - Interpreted languages are **slower** than the compiling languages like C, C++.
  - As we know by now, interpreted languages run line by line so there's no way the interpreter knows what comes next. This doesn't happen in compiling languages.
  - Compiling languages on the other hand have a dedicated **compiler** (tool to convertnormal code into **[bytecode](https://en.wikipedia.org/wiki/Bytecode)**).
  - The compiler essentially keeps everything ready (allocating memory for variables) for the interpreter to run. Hence, its **fast**.

- Python is a **[dynamic](https://en.wikipedia.org/wiki/Dynamic_programming_language)** language.
  - Dynamic language means you can change the object (variable) type however you want.
  - You don't need to declare the variable type. You can create an object of one type **dynamically** and overwrite the same object (variable) with different datatype.
  - This is feature of being an interpreted language.

- Python **3.x+** is the way to go as Python 2.x has officially reached **EOL** (End of Life).
  - Python supports 2 primary versions, Python 3 and Python 2. You'll come across these when you try to install Python by yourself on your locally.

- Python doesn't actively support **[access modifiers](https://www.studytonight.com/python/access-modifier-python)** (it does, but theoretically).

- Python follows **precedences** (order of operations).
  - Precendences are the way or priority in which the mathematical operations (**+, -, *, ()**) are carried out.
  - Python has strong mathematical roots and hence it follows mathematical rules of operations.
  - Check out the **precedence table** **[here](https://en.wikipedia.org/wiki/Order_of_operations#Programming_languages)**.
  - Python operates on the variables or objects in the sequence defined in the above table i.e parenthesis (round brackets **"()"**) are executed first, then the exponential powers and so on...

- Python uses **indentations** for denoting the block of code (scope of code).

- Python's **[syntax](https://en.wikipedia.org/wiki/python_syntax_and_semantics)** is simple.
  - Like every programming language, Python also has some rules of writing code. These rules are called as **Syntax**.
  - Python has a simple and beginner friendly code syntax.
    - For displaying values we use `print()`.

      ```python
      print("This is how we print messages or values on screen.")
      ```

    - Anything and everything in **"like this"** or **'like this'** or **'''like this'''** is considered to be a string.

      ```python
      str_1 = 'This is a string.'
      str_2 = "This is also a string."
      str_3 = """This is also considered to be a string."""
      ```

    - **Never** use combination of both quotes while creating a string object.
    - For denoting **floating** point numbers or floats in general we use decimal point **"."**.

      ```python
      float_1 = 69.0
      float_2 = 6.9e+12
      float_3 = -6.9
      ```

    - For executing any **block of code**, we indent them.
      - These blocks of code could be a **loop**, **function** or a **class**.
        - Loops look like this:
          - For loop

            ```python
              for idx in range(15):
                  print(idx)
            ```

          - While loop

            ```python
            while True:
                print("This is an infinite loop.")
            ```

        - Functions look like this:

          ```python
          def function_name():
              print("This is how functions are written.")
          ```

        - Classes look like this:
  
          ```python
          class ClassName():
              print("This is a class in Python.")
          ```
