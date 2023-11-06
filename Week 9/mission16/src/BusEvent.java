/**
 * Contains information about a bus-related event.
 */
public class BusEvent implements Comparable<BusEvent> {

    public AbstractBus bus;
    public int time;
    public EventType eventType;

    /**
     * Constructs a `BusEvent` with a given bus and time. This constructor (i.e. one that takes in a time and bus) MUST
     * EXIST, though the constructor body can be modified if other instance variables are added subsequently.
     */
    public BusEvent(AbstractBus bus, int time) {
        this.bus = bus;
        this.time = time;
        this.eventType = EventType.OPERATIONAL;
    }

    // Method that compares one `BusEvent` with another to determine the ordering. The BusEvent with an earlier
    // timing, i.e. smaller `time` value should go first.
    @Override
    public int compareTo(BusEvent o) {
        // TODO: Implement this (Task 1a)
        return time - o.time;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b / Task 4b
        return null;
    }

}