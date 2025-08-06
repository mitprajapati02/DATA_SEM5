global front, rear, max_elements, queue
queue = []
front = -1
rear = -1

def main():
    global max_elements
    max_elements = int(input("Enter maximum number of elements for the queue\n"))
    
    while(True):
        print("---------Menu----------")
        print("1) Insert")
        print("2) Delete")
        print("3) Display")
        print("4) Exit")
        choice = int(input("Enter your choice (1-4)\t"))
        
        match choice:
            case 1: 
                insert()
            case 2: 
                delete()
            case 3: 
                display()
            case 4: 
                return
            case _: 
                print("Enter choice value between 1-4")

def insert():
    global front, rear, max_elements, queue

    # Check for overflow (when rear reaches the max_elements-1)
    if rear >= (max_elements - 1):  # Queue is full
        print("Queue overflow")
    else:
        if front == -1:  # Queue is initially empty
            front = 0
        item = input("Enter item to be pushed\t")
        rear = rear + 1  # Move rear pointer forward
        queue.append(item)  # Insert the item at the rear
        print("Item pushed successfully!!")
        print("Value of Rear:", rear, " Front:", front)

def delete():
    global front, rear, max_elements, queue
    
    # Check for underflow (when front is -1, meaning the queue is empty)
    if front == -1:  # Queue is empty
        print("Queue underflow")
    else:
        print("Value of Rear:", rear, " Front:", front)
        item = queue[front]  # Get the item at the front
        print(item, "deleted successfully")
        
        # If front == rear, the queue becomes empty
        if front == rear:
            front = -1
            rear = -1
        else:
            front = front + 1  # Move the front pointer forward

def display():
    global front, rear, max_elements, queue
    
    if front == -1:  # Queue is empty
        print("Queue is empty")
    else:
        print("Items in queue:")
        for i in range(front, rear + 1):  # Iterate from front to rear
            print(queue[i], end="\n")

main()
