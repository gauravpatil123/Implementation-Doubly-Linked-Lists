import java.util.NoSuchElementException;
import java.util.Iterator;

public class DoublyLinkedList<Item> implements Iterable<Item> {

    private Node first;
    private Node last;
    private int num;

    private class Node {

        Item item;
        Node next;
        Node prev;

    }
    // Initializes an empty Linked list
    public DoublyLinkedList() {

        this.first = new Node();
        this.last = new Node();
        this.num = 0;
        first.item = null;
        last.item = null;
        first.next = last;
        last.prev = first;

    }

    // true if list is empty else false
    public boolean isEmpty() {

        return (this.num == 0);

    }

    // returns number of elements
    public int size() {
 
        return num;

    }

    // prepends element to the collection
    public void addFirst(Item item) {

        if (item == null) throw new IllegalArgumentException("null argument found!");

        Node newNode = new Node();
        newNode.item = item;
        newNode.next = this.first.next;
        newNode.prev = this.first;
        this.first.next.prev = newNode;
        this.first.next = newNode;
        this.num++;

    }

    // appends element to the collection
    public void addLast(Item item) {

        if (item == null) throw new IllegalArgumentException("null argument found!");

        Node newNode = new Node();
        newNode.item = item;
        newNode.next = this.last;
        newNode.prev = this.last.prev;
        this.last.prev.next = newNode;
        this.last.prev = newNode;
        this.num++;

    }

    // Inserts Item at specified position
    public void add(int index, Item item) {

        if (index >= this.num || index < 0) {
            
            throw new IndexOutOfBoundsException("index is out of bounds!");

        }

        if (item == null) throw new IllegalArgumentException("null argument found!");

        int idx = 0;
        Node current = new Node();
        current.item = item;
        current.next = this.first.next;
        
        while (idx != index) {

            current.next = current.next.next;
            idx++;

        }

        current.prev = current.next.prev;
        current.prev.next.prev = current;
        current.prev.next = current;
        this.num++;

    }

    // appends element to the list
    public void add(Item item) {

        if (item == null) throw new IllegalArgumentException("null argument found!");
        addLast(item);

    }

    // removes first element of list
    public Item removeFirst() {

        if (this.num == 0) throw new NoSuchElementException("No element found");

        Node delNode = this.first.next;
        Item out = delNode.item;
        this.first.next = delNode.next;
        this.first.next.prev = this.first;
        this.num--;
        return out;

    }

    // removes last element of list
    public Item removeLast() {

        if (this.num == 0) throw new NoSuchElementException("No element found");
        Node delNode = this.last.prev;
        Item out = delNode.item;
        this.last.prev = delNode.prev;
        this.last.prev.next = this.last;
        this.num--;
        return out;

    }

    // clears all elements of list
    public void clear() {

        this.first = new Node();
        this.last = new Node();
        this.num = 0;
        first.item = null;
        last.item = null;
        first.next = last;
        last.prev = first;

    }

    // creates and retures a identical list
    public DoublyLinkedList<Item> clone() {

        DoublyLinkedList<Item> newLL = new DoublyLinkedList<Item>();
        int count = 0;
        Node current = new Node();
        current.next = this.first.next;
        
        while (count != this.num) {

            Item item = current.next.item;
            newLL.addLast(item);
            current.next = current.next.next;
            count++;
        }

        return newLL;

    }

    // checks if the list has the specified element
    public boolean contains(Item item) {

        if (item == null) throw new IllegalArgumentException("argument is null");

        Node current = this.first;
        int idx = 0;

        while (idx != this.num) {

            current = current.next;
            Item element = current.item;
            idx++;
            if (element.equals(item)) return true;

        }

        return false;

    }

    // returns the first element of the list without removing
    public Item element() {

        if (this.num == 0) throw new NoSuchElementException("List is Empty");
        return this.first.next.item;

    }

    // returns the element at the specified position
    public Item get(int index) {

        int idx = 0;
        Node current = this.first.next;

        while (idx != index) {

            current = current.next;
            idx++;

        }

        Item item = current.item;
        return item;

    }

    // returns first element
    public Item getFirst() {

        if (this.num == 0) throw new NoSuchElementException("List is empty");
        return this.first.next.item;

    }

    // returns last element
    public Item getLast() {

        if (this.num == 0) throw new NoSuchElementException("List is empty");
        return this.last.prev.item;

    }

    // returns the index of first occurence of specified element or -1 if no such element
    public int indexOf(Item item) {

        if (this.num == 0) return -1;
        int idx = 0;
        Node current = this.first.next;
        while (idx != this.num) {

            Item currItem = current.item;
            if (currItem.equals(item)) return idx;
            current = current.next;
            idx++;

        }

        return -1;

    }

    public Iterator<Item> iterator() {

        return new LinkedListIterator();

    }

    private class LinkedListIterator implements Iterator<Item> {

        private Node current = first;

        public boolean hasNext(){

            return current.next != last;

        }

        public Item next() {

            if (!hasNext()) throw new NoSuchElementException("no more elements");

            current = current.next;
            Item item = current.item;
            return item;

        }

        /*
        public void remove() {

        }
        */
    }

/*
    public static void main(String[] args) {

        // unit tests:
        DoublyLinkedList<String> words = new DoublyLinkedList<String>();
        System.out.println("Is the LL empty = "+words.isEmpty());
        System.out.println("LL size = "+words.size());
        words.addFirst("Ace");
        words.addLast("King");
        words.addLast("Queen");
        words.addFirst("Two");
        words.addFirst("One");
        words.addLast("Jack");
        System.out.println("LL size = "+words.size());
        System.out.println("Current List is : ");
        for (String s: words) { System.out.println(s); }
        words.removeFirst();
        words.removeLast();
        words.removeFirst();
        words.removeFirst();
        for (String s: words) { System.out.println(s); }
        System.out.println("LL size = "+words.size());
        words.add(1, "Ace");
        words.add("Five");
        for (String s: words) { System.out.println(s); }
        System.out.println("LL size = "+words.size());        
        
        DoublyLinkedList<String> newWords = words.clone();
        for (String s: newWords) { System.out.println(s); }
        newWords.clear();
        System.out.println("LL size = "+newWords.size());
        // for (String s: newWords) { System.out.println(s); }

        System.out.println(words.contains("Ace"));
        System.out.println(words.contains("Seven"));
        System.out.println(words.element());
        for (String s: words) { System.out.println(s); }
        System.out.println(words.get(3));
        System.out.println(words.get(2));
        System.out.println(words.getFirst());
        System.out.println(words.getLast());
        System.out.println(words.indexOf("Ace"));
        System.out.println(words.indexOf("Eight"));

    }
*/
}
