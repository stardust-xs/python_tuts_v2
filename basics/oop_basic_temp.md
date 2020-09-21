# Object Oriented Programming

Types of **Paradigm** (notion/method/framework) of programming.

- OOP - Python, C++, Java, VBS, JS
  - Map, Filter and Reduce
- **Declarative** (What to do) - Python, HTML, VBS, Markdown, DB Query Languages.
- **Imperative** (Opposite of declarative/Calling objects) - Python, CSS, VBS, Java, C++

- Functional (similar to OOP **BUT** with only functions and has nothing to do with **Classes**!!!!) - **Only Functions**! - Python, C, C++
  - Map, Filter and Reduce


# collections

  
## OOP - Classes and Objects (Functions)

1. Concepts of Classes - class.
2. Objs - All python objects.
3. Inheritance - To take/inherit the properties of parent obj.
4. Encapsulation - Wrapping of data.
5. Polymorphism - Transforms the way an object works.
6. Abstraction - displaying only essential information and hiding the details

## OOP (Classes and Objs)

Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects" simply Object-oriented programming uses objects. But it is more than just classes and objects. It's a whole programming paradigm based around objects (data structures/types) that contain data (attribute) and methods (functions).

### Classes

```python

class LivingObject(object):
  breathe = True
  born = 0
  die = 100

  def movements():
    for i in movement:
      pass

  def thinking(): pass
  def feeling(): pass

  def growing():
    for i in range(born, death):
      grow += i


class Bipedals(LivingObject):
  leg_count = 2
  speed = "Slow"
  jump = "Low"


class Apes(Bipedals, LivingObject):
  tail = True
  big_face = True
  posture = "Crooked"
  hair = True

class Humans(Bipedals):
  tail = False
  big_face = False
  posture = "Straight"
  hair = True


class Quadrapedals(LivingObject):
  leg_count = 4
  speed = "Fast"
  jump = "High"


class Humans(object):
    name = ""
    intelligence = ""

    breathe = True
    born = 0
    die = 100

    def movements():
      for i in movement:
        pass

    def thinking(): pass
    def feeling(): pass

    def growing():
      for i in range(born, death):
        grow += i


class Canine(living_object):
  fur = "Red"
  breed = "German Shepherd"
  age = "2 yrs"
  height = "Shorter than me"

  def barks():
    print("Bark...!")

  def born_die():
    print("Exist")

  breathe = True
  born = 0
  die = 100

  def movements():
    for i in movement:
      pass

  def thinking(): pass
  def feeling(): pass

  def growing():
    for i in range(born, death):
      grow += i


class Feline(living_object):
  fur = "White"
  teeth_count = 12
  breed = "Bad"
  gender = "female"
  age = "17 months"
  height = "Defo shorter than me"

  def sleep():
    print("Sleeping...")


class Fossil(non_living_object):
  carbon_level = 0.96
  burn_ratio = 0.9833

  def release_nrg():
    print("Give NRG")

  def born_die():
    print("Exist")

```

### Parting words about objects...

- Everything in an OOP is an object and every activity in OOP has to do something with the object.
- Consider OOP objects as real world example for quick OR naive way of understanding.
- All objects have data (attributes) and functions (methods).

## CLASSES

Think it as of a blueprint for a particular object. (Try to relate with above example classes).
They are considered to be **first-class** objects in Python (OOP in general). Being a blueprint, it can be used for creating new objects thus defining new **datatypes**...

**First class** means hi-fi objects. They get first class treatment, meaning they can be used anywhere. You can create, modify, assign it to other variable, delete a class. They're also referred as **First Class Citizen**.

- W/O class an object cannot exist.
- You can define/declare multiple objects of a same class.

# T

```python

class object:
  data = None
  
  def some_method():
    pass

class int(object):
  data = "..."
  def new_xa_methods():
    pass
```

```python
class Humans(object):
    name = ""
    intelligence = ""

    breathe = True
    born = 0
    die = 100

    def movements():
      for i in movement:
        pass

    def thinking(): pass
    def feeling(): pass

    def growing():
      for i in range(born, death):
        grow += i


class vehicle(object):
  pass


class Car(vehicle):
  color = "Red"
  engine_type = "Electric"
  max_speed = 350
  manufacturer = "Tesla"

  def accelerate():
    pass # something to do with max_speed.


class TeslaModelY(Car):
  type_of_car = "Sedan"
  max_speed = 380
  auto_pilot = True

```
# Blueprint of a Car
## Audi, Tesla, Alto and Lamborghini

```python

class Car(object):
  speed = 350
  manufacturer = "XA"
  engine_type = ["Diesel", "Petrol", "Electric", "Solar", "Gas"]
  type_of_car = ["Manual", "FSD", "Semi"]
  cooling = False

  def accelerate():
    pass

  def operate_gears():
    pass

  def stop():
    pass

  def autopilot():
    pass


class Audi(Car):
  engine_type = "Petrol"
  year = 2014


class Audi2020(Audi):
  year = 2026
  engine_type = ["Dyson Sphere", "Black Hole"]
```


```python
class CellPhone(object):
  model_name = "xyz"
  interactivity = ["Touch", "Keypad"]
  manufacturer = "XA"
  battery = 1560
  storage = 16
  display = ["LCD", "AMOLED"]
  processor = ["ARM", "QC"]
  camera = 2.0
  port = "Micro USB"
  connectivity = "3G"

  def calling():
    pass # calling other people

  def recording():
    pass # recording videos

  def multimedia():
    pass # stalking people

  def charging():
    pass # something to do with battery variable.

  def google_assistant():
    pass


class Apple(CellPhone):
  model_name = "iPhone 11 Pro Max"
  interactivity = "Touch"
  battery = 3500
  storage = 16
  display = "AMOLED"
  processor = "Apple Bionic"
  camera = 13.0
  port = "Lightning"
  connectivity = "4G"
  manufacturer = "Apple"
  nfc = True

  def video_calling():
    return calling() + recording()

  def animoji():
    pass

  def siri():
    pass # AI


class SamsungGalaxyNote(CellPhone):
  model_name = "Galaxy Note 20 Ultra"
  stylus_supported = True
  stylus = "spen"
  interactivity = "Touch"
  battery = 3500
  storage = 64
  display = "AMOLED"
  processor = ("QC", "Exynos")
  bluetooth = True

  def video_calling(self, safe, camera):
    return calling() + recording()

  def note_taking(self):
    pass

  def bixby(self):
    pass # AI


bt_check = SamsungGalaxyNote()
vdo = SamsungGalaxyNote()
ai = SamsungGalaxyNote()

SamsungGalaxyNote().stylus_supported
SamsungGalaxyNote().bluetooth

my_phone = SamsungGalaxyNote()
SamsungGalaxyNote().video_calling(my_phone)

```

# Encapsulation

pass

# Polymorphism

pass
