
# ***(a). Problem Statement*** 

## ***1.Need for this project***
*A small, single-counter food outlet needs a way to*

*(a) Show customers an accurate, current
menu,*

*(b) Take a multi-item order without arithmetic mistakes,*

*(c) Let staff correct the menu
the moment a price or item changes, and* 

*(d) Keep a simple record of what was sold — all on a
single machine, with nothing beyond Python installed.*

## *2.What Does it Solves?*

- *Manual order-taking (a verbal order, a paper token, or a mental tally) works at low volume but becomes error-prone as order volume increases:*

  - *Prices drift out of sync between the counter and the till*

  - *Totals get mis-added during a rush*

  - *No record of what actually sold on a given day.*

## *3. What is FOOD SPACE?*
### *FOOD SPACE is a lightweight, console-based Python application built for customer and employee's utility, without requiring a POS terminal, a database server, or an internet connection.*

# *(b). Scope*

## ***(1). In scope:***
- *A single-counter, single-session console workflow for browsing the menu.*
- *Menu can be used for placing and
  modifying an order*
- *Automatically computes the bill.*
- *Basic local *
- *Menu management:*
  - *Add item*
  - *Remove item*
  - *Edit price.*
- *Persistent storage of menu* 
- *Saves order history into a seperate .txt file*

## ***(2). Out of scope (for this version):***
- *Multi-user / concurrent access.*
- *Online payment.*
- *A graphical or web interface.*
- *Networked or multi-branch operation.*

# ***(c). Target Users***

- ***Customers at the counter, choosing what to order and seeing what it will cost.***
- ***Employees / counter staff, who need to keep the on-screen menu and prices accurate from
  day to day.***

# ***(d). High-Level Features***

- ***View the live, numbered menu.***
- ***Place and modify a multi-item order, by item number or by name, with a running total.***
- ***Confirm an order and have it saved to a persistent sales log (`order_history.txt`).***
- ***(Employee-only)* add a menu item, remove a menu item, or update an item's price — changes***
  save immediately to `menu.txt`.
