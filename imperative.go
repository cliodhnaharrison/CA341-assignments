package main

import (
    "errors"
    "fmt"
    "log"
)

type Node struct {
    // Node struct with name, phone and address as strings
    // Left and Right are child Nodes
    Name string
    Phone string
    Address string
    Left *Node
    Right *Node
}


func (n *Node) insertName(name, phone string, address string) error {
    // Function to insert based on name
    if n ==  nil {
        return errors.New("Cannot insert an entry into a nil tree")
    }

    switch {

    case name == n.Name:
        return nil

    case name < n.Name:
        if n.Left == nil {
            n.Left =  &Node{Name: name, Phone: phone, Address: address}
            return nil
        }
        return n.Left.insertName(name, phone, address)

    case name > n.Name:
        if n.Right == nil {
            n.Right =  &Node{Name: name, Phone: phone, Address: address}
            return nil
        }
        return n.Right.insertName(name, phone, address)
    }
    return nil
}


func (n *Node) insertPhone(name, phone string, address string) error {
    // Function to insert based on phone number
    if n ==  nil {
        return errors.New("Cannot insert an entry into a nil tree")
    }

    switch {

    case phone == n.Phone:
        return nil

    case phone < n.Phone:
        if n.Left == nil {
            n.Left =  &Node{Name: name, Phone: phone, Address: address}
            return nil
        }
        return n.Left.insertPhone(name, phone, address)

    case phone > n.Phone:
        if n.Right == nil {
            n.Right =  &Node{Name: name, Phone: phone, Address: address}
            return nil
        }
        return n.Right.insertPhone(name, phone, address)
    }
    return nil
}


func (n *Node) findName(name string) []string {
    // Function to find Node from name
    if n == nil {
        return []string{"", "", ""}
    }

    switch {

    case name == n.Name:
        return []string{n.Name, n.Phone, n.Address}

    case name < n.Name:
        return n.Left.findName(name)

    default:
        return n.Right.findName(name)
    }
}


func (n *Node) findPhone(phone string) []string {
    // Function to find Node from phone number
    if n == nil {
        return []string{"", "", ""}
    }

    switch {

    case phone == n.Phone:
        return []string{n.Name, n.Phone, n.Address}

    case phone < n.Phone:
        return n.Left.findPhone(phone)

    default:
        return n.Right.findPhone(phone)
    }
}


func (n *Node) findMax(parent *Node) (*Node, *Node) {
    // Helper function for delete functions
    // Finds largest Node
    if n == nil {
        return nil, parent
    }

    if n.Right == nil {
        return n, parent
    }

    return n.Right.findMax(n)
}


func (n *Node) replaceNode(parent, replacement *Node) error {
    // Helper function for delete functions
    // Replaces Node with given Node
    if n == nil {
        return errors.New("replaceNode() not allowed on nil node")
    }

    if n == parent.Left {
        parent.Left = replacement
        return nil
    }

    parent.Right = replacement
    return nil
}


func (n *Node) deleteName(name string, parent *Node) error {
    // Deletes Node with the given name
    if n == nil {
        return errors.New("Entry to be deleted does not exist in tree")
    }

    switch {

    case name < n.Name:
        return n.Left.deleteName(name, n)

    case name > n.Name:
        return n.Right.deleteName(name, n)

    default:

        if n.Left == nil && n.Right == nil {
            n.replaceNode(parent, nil)
            return nil
        }

        if n.Left == nil {
            n.replaceNode(parent, n.Right)
            return nil
        }

        if n.Right == nil {
            n.replaceNode(parent, n.Left)
            return nil
        }

        replacement, replParent := n.Left.findMax(n)

        n.Name = replacement.Name
        n.Phone = replacement.Phone
        n.Address = replacement.Address

        return replacement.deleteName(replacement.Name, replParent)
    }
}


func (n *Node) deletePhone(phone string, parent *Node) error {
    // Deletes Node with given phone number
    if n == nil {
        return errors.New("Entry to be deleted does not exist in tree")
    }

    switch {

    case phone < n.Phone:
        return n.Left.deletePhone(phone, n)

    case phone > n.Phone:
        return n.Right.deletePhone(phone, n)

    default:

        if n.Left == nil && n.Right == nil {
            n.replaceNode(parent, nil)
            return nil
        }

        if n.Left == nil {
            n.replaceNode(parent, n.Right)
            return nil
        }

        if n.Right == nil {
            n.replaceNode(parent, n.Left)
            return nil
        }

        replacement, replParent := n.Left.findMax(n)

        n.Name = replacement.Name
        n.Phone = replacement.Phone
        n.Address = replacement.Address

        return replacement.deletePhone(replacement.Phone, replParent)
    }
}


type Tree struct {
    // Tree struct with root attribute
    Root *Node
}


func (t *Tree) insertName(name, phone string, address string) error {
    // Function to insert Node into Tree based on name
    if t.Root == nil {
        t.Root = &Node{Name: name, Phone: phone, Address: address}
        return nil
    }

    return t.Root.insertName(name, phone, address)
}


func (t *Tree) insertPhone(name, phone string, address string) error {
    // Function to insert Node into Tree based on phone number
    if t.Root == nil {
        t.Root = &Node{Name: name, Phone: phone, Address: address}
        return nil
    }

    return t.Root.insertPhone(name, phone, address)
}


func (t *Tree) findName(name string) []string {
    // Find Node in Tree with given name
    if t.Root == nil {
        return []string{"", "", ""}
    }

    return t.Root.findName(name)
}


func (t *Tree) findPhone(phone string) []string {
    // Find Node in Tree with given phone number
    if t.Root == nil {
        return []string{"", "", ""}
    }

    return t.Root.findPhone(phone)
}


func (t *Tree) deleteName(name string) error {
    // Deletes Node from Tree with given name
    if t.Root == nil {
        return errors.New("Cannot delete from an empty tree")
    }

    fakeParent := &Node{Right: t.Root}
    err := t.Root.deleteName(name, fakeParent)

    if err != nil {
        return err
    }

    if fakeParent.Right == nil {
        t.Root = nil
    }

    return nil
}


func (t *Tree) deletePhone(phone string) error {
    // Deletes Node from Tree with given phone number
    if t.Root == nil {
        return errors.New("Cannot delete from an empty tree")
    }

    fakeParent := &Node{Right: t.Root}
    err := t.Root.deletePhone(phone, fakeParent)

    if err != nil {
        return err
    }

    if fakeParent.Right == nil {
        t.Root = nil
    }

    return nil
}


func (t *Tree) Traverse(n *Node, f func(*Node)) {
    // Traverses tree and calls given function on each node
    // Used to print each Node in Tree
    if n == nil {
        return
    }

    t.Traverse(n.Left, f)
    f(n)
    t.Traverse(n.Right, f)
}


func main () {
    // Main function that tests Tree functionality

    // Test data
    names := []string{"Cliodhna", "Zach", "Cory", "Betty", "Abraham", "Jordan", "Mary", "Joseph", "Zed"}
    phones := []string{"0855881892", "0884624315", "0850602678", "0868026665", "0887178084", "0858573472", "0856776227", "0873787608", "0890402726"}
    addresses := []string{"Apt 1", "Apt 2", "Apt 3", "Apt 4","Apt 5", "Apt 6", "Apt 7", "Apt 8", "Apt 9"}

    nameTree := &Tree{}
    phoneTree := &Tree{}

    // Demonstrates the insert functionality
    for i := 0; i < len(names); i++ {
        nameErr := nameTree.insertName(names[i], phones[i], addresses[i])
        phoneErr := phoneTree.insertPhone(names[i], phones[i], addresses[i])
        if nameErr != nil {
            log.Fatal("Error inserting name '", names[i], "': ", nameErr)
        }
        if phoneErr != nil {
            log.Fatal("Error inserting name '", names[i], "': ", phoneErr)
        }
    }

    // Demonstrates the find functionality
    nameResult := nameTree.findName("Joseph")
    fmt.Println("Name: ", nameResult[0], "\nPhone Number: ", nameResult[1], "\nAddress: ", nameResult[2], "\n")
    fmt.Println("-----------------")
    phoneResult := phoneTree.findPhone("0850602678")
    fmt.Println("Name: ", phoneResult[0], "\nPhone Number: ", phoneResult[1], "\nAddress: ", phoneResult[2], "\n")
    fmt.Println("-----------------")

    // Demonstrates the delete functionality
    nameTree.deleteName("Joseph")
    phoneTree.deletePhone("0850602678")
    nameTree.Traverse(nameTree.Root, func(n *Node) { fmt.Print("Name: ", n.Name, "\nPhone Number: ", n.Phone, "\nAddress: ", n.Address, "\n\n") })
    fmt.Println("-----------------")
    phoneTree.Traverse(phoneTree.Root, func(n *Node) { fmt.Print("Name: ", n.Name, "\nPhone Number: ", n.Phone, "\nAddress: ", n.Address, "\n\n") })
}
