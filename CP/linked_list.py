#Given two loked list of the same size, the task is to create a new linked list using linked list.The condition is that the greater node among the linked list will be added to the new linked list;
def removeduplicates(head):
    track ={}
    temp=head
    while(temp!=None):
        if temp.data  in track:
            print(temp.data,end="")
        track[temp.data]= None
        temp = temp.next