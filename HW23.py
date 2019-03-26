# -*- coding: utf-8 -*-
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            lastNode=self.head
            while lastNode.next != None:
                lastNode=lastNode.next
            lastNode.next=newNode
    def prepend(self, data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode
    def insertAfNode(self,prevNode,data):
        newNode=Node(data)
        newNode.next=prevNode.next
        prevNode.next=newNode
    def printList(self):
        if self.head==None:
            print("No! The list is empty")
        curNode=self.head
        while curNode!=None:
            print(curNode.data)
            curNode=curNode.next
    def deleteNode(self,data):
        if self.head==None:
            print("Don't waste my time")
            return
        if self.head.data==data:
            temp=self.head
            self.head=self.head.next
            temp=None
        else:
            prevNode=self.head
            curNode=self.head
            curNode=curNode.next
            if curNode==None:
                print("Data not found")
            while curNode!=None:
                if curNode.data==data:
                    prevNode.next=curNode.next
                    curNode=None
                    return
                curNode=curNode.next
            print("Data not found")
    def deleteAtPos(self, pos):
        curNode=self.head
        if pos==0:
            self.head=curNode.next
            curNode=None
            return
        else:
            cnt=0
            prev=None
            while curNode != None and cnt!=pos:
                prev=curNode
                curNode=curNode.next
                cnt+=1
            if curNode == None:
                print("The node does not exist")
                return
            else:
                prev.next=curNode.next
                curNode=None
    def len_iterative(self):
        curNode=self.head
        cnt=0
        while curNode != None:
            cnt+=1
            curNode=curNode.next
        return cnt
    def len_recursive(self, heady):
        if heady==None:
            return 0
        else:
            return 1+self.len_recursive(heady.next)
    def swapNode(self, key1, key2):
        if key1 == key2:
            print("These nodes are the same. Too bad.")
            return
        else:
            curNode1=self.head
            prev1=None
            while curNode1 != None and curNode1.data!=key1:
                prev1=curNode1
                curNode1=curNode1.next
            if curNode1==None:
                print("Key1 not found")
                return
            curNode2=self.head
            prev2=None
            while curNode2.data != key2 and curNode2 !=None:
                prev2=curNode2
                curNode2=curNode2.next
            if curNode2==None:
                print("Key2 not found")
                return
            if prev1==None:

                temp=curNode1.next
                self.head.next=curNode2.next
                curNode2.next=temp
                prev2.next=self.head
                self.head=curNode2
                return
            if prev2==None:
                temp=curNode2.next
                self.head.next=curNode1.next
                curNode1.next=temp
                prev1.next=self.head
                self.head=curNode1
                return
            if prev2!=None and prev1!=None: 
                prev1.next=curNode2
                prev2.next=curNode1
                temp=curNode1.next
                curNode1.next=curNode2.next
                curNode2.next=temp
    def reverse_iterative(self):
        prev=None
        curNode=self.head
        while curNode!=None:
            temp=curNode.next
            curNode.next=prev
            prev=curNode
            curNode=temp
        self.head=prev
"""
moss=linkedList()
moss.append("sparky")
moss.prepend('rose')
moss.append(125)
print("Testing prepend and append")
moss.printList()
moss.insertAfNode(moss.head,"hip")
print("Inserting hip after rose")
moss.printList()
moss.insertAfNode(moss.head.next.next, "the benevolent")
print("Inserting the benevolent after Sparky")
moss.printList()
moss.deleteNode('hip')
moss.deleteNode("rose")
moss.deleteNode("999999999999999")
moss.deleteNode("the benevolent")
moss.deleteNode("sparky")
moss.deleteNode(125)
print("testing the Delete function")
moss.printList()
"""
lst=linkedList()
lst.append('a')
lst.append('b')
lst.append('c')
lst.prepend('d')
#lst.deleteNode('a')
#lst.deleteAtPos(0)
print(lst.len_iterative())
print(lst.len_recursive(lst.head))
lst.printList()
lst.swapNode('a','c')
lst.printList()
lst.swapNode('a','a')
lst.swapNode('e','f')
lst.printList()
lst.swapNode('b','c')
lst.swapNode('a','b')
lst.swapNode('d','b')
lst.swapNode('d','b')
#lst.reverse_iterative()
lst.printList()
