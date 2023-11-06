import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;

/**
 * `BusSimulator` drives event simulation, i.e. both event processing and generation.
 */
public class BusSimulator {

    // Priority queue of events for the simulator to process.
    private final Queue<BusEvent> eventQueue = new PriorityQueue<>();

    // Pseudorandom number generator - DO NOT MODIFY THE SEED VALUE OF 999.
    private final Random random = new Random(999);

    /**
     * Constructs a `BusSimulator` with an event queue populated using the `busEvents` given.
     *
     * @param busEvents Events to populate the event queue with.
     */
    public BusSimulator(List<BusEvent> busEvents) {
        eventQueue.addAll(busEvents);
    }

    /**
     * Prints some simple status information about the simulator.
     */
    public void printStatus() {
        System.out.println("Bus simulator is ready!");
        System.out.println("There are a total of " + eventQueue.size() + " events.");
    }

    /**
     * Runs the simulator until the event queue has been emptied.
     */
    public void run() {
        // TODO: Implement this (Task 3b)
    }

    /**
     * Runs the simulator with a probability of bus breakdowns until the event queue has been emptied.
     * <p>
     * Uses the `random` initialised on top in `BusSimulator` for pseudorandom number generation.
     */
    public void runWithBreakdowns() {
        // TODO: Implement this (Task 4b)
    }

    /**
     * Entry point to this program.
     */
    public static void main(String[] args) {
        List<BusEvent> busEvents = readBusEvents();
        BusSimulator simulator = new BusSimulator(busEvents);
        simulator.printStatus();
        simulator.run();
    }

    /**
     * Reads in input from the console and produces a list of `BusEvent`s. This method has been provided for you.
     *
     * @return List of `BusEvent`s.
     */
    public static List<BusEvent> readBusEvents() {
        Scanner sc = new Scanner(System.in);
        int numBuses = sc.nextInt();
        sc.nextLine();
        List<BusEvent> busEvents = new ArrayList<>();

        for (int i = 0; i < numBuses; i++) {
            String[] busLine = sc.nextLine().split(" ");
            AbstractBus bus;

            // NOTE: Do read up on switch statements if you're unsure of what they do!
            switch (busLine[0]) {
            case "A1":
                bus = new BusA1();
                break;
            case "B1":
                bus = new BusB1();
                break;
            case "C":
                bus = new BusC();
                break;
            case "D1":
                bus = new BusD1();
                break;
            default:
                continue;
            }

            BusEvent busEvent = new BusEvent(bus, Integer.parseInt(busLine[1]));
            busEvents.add(busEvent);
        }

        sc.close();
        return busEvents;
    }
}

/**
 * Class that manages the bus routes.
 */
class BusMap {

    /**
     * Returns a `Pair` containing the name of the next bus stop for this bus, as well as the time needed to reach that
     * next bus stop from the current stop.
     * <p>
     * IMPORTANT: If `currentStop == null`, return the first stop along the route. If `currentStop` is the final stop
     * for this bus, return `null`.
     *
     * @param busName     Number of the bus: "A1", "B1", "C" or "D1".
     * @param currentStop The current stop of the bus.
     */
    public static Pair getNextStopAndTimeTaken(String busName, String currentStop) {
        // TODO: Implement this (Task 1b)
        return new Pair("Placeholder", 0);
    }

    /**
     * Names of the bus stops along the routes for each of the buses: A1, B1, C, D1.
     */
    private static final String[] A1_STOPS = {"PGP (START)", "KR MRT", "LT 27", "UNIVERSITY HALL", "OPP UHC",
            "YIH", "CENTRAL LIBRARY", "LT 13", "AS 5", "COM 2", "BIZ 2", "OPP TCOMS", "PGP (END)"};
    private static final String[] B1_STOPS = {"KR BUS TERMINAL", "IT (OPP CLB)", "OPP YIH", "UNIVERSITY TOWN",
            "YIH", "CENTRAL LIBRARY", "LT 13", "AS 5", "BIZ 2"};
    private static final String[] C_STOPS = {"KR BUS TERMINAL (START)", "JAPANESE PRI SCH", "KENT VALE",
            "MUSEUM", "UNIVERSITY TOWN (FROM KR)", "UHC", "OPP UNIVERSITY HALL", "S 17 (OPP LT 27)", "LT 27",
            "UNIVERSITY HALL", "OPP UHC", "UNIVERSITY TOWN (TO KR)", "RAFFLES HALL", "EA", "KR BUS TERMINAL (END)"};
    private static final String[] D1_STOPS = {"OPP HSSML", "OPP NUSS", "COM 2 (FROM HSSML)", "VENTUS (OPP LT 13)",
            "IT (OPP CLB)", "OPP YIH", "MUSEUM", "UNIVERSITY TOWN", "YIH", "CENTRAL LIBRARY",
            "LT 13", "AS 5", "COM 2 (TO BIZ 2)", "BIZ 2"};

    /**
     * Time taken to reach the i-th stop from the (i - 1)-th stop. The integer at the i-th index refers to that for the
     * i-th stop above.
     */
    private static final int[] A1_TIMINGS = {0, 3, 3, 2, 2, 1, 2, 2, 5, 6, 3, 1, 1};
    private static final int[] B1_TIMINGS = {0, 5, 1, 2, 2, 1, 2, 2, 1};
    private static final int[] C_TIMINGS = {0, 1, 10, 3, 1, 3, 1, 2, 1, 1, 1, 2, 2, 1, 2};
    private static final int[] D1_TIMINGS = {0, 4, 2, 2, 1, 1, 2, 1, 3, 1, 1, 7, 2, 4};

    /**
     * Helper class that associates a stop name and the time taken to reach that stop from the previous stop.
     */
    public static class Pair {
        String stopName;
        int timeTakenFromPreviousStop;

        public Pair(String stopName, int time) {
            this.stopName = stopName;
            timeTakenFromPreviousStop = time;
        }
    }
}

/**
 * Contains information about a bus-related event.
 */
class BusEvent implements Comparable<BusEvent> {

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
        return 0;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b / Task 4b
        return null;
    }

}

enum EventType {
    OPERATIONAL,
    BROKEN_DOWN,
    REPAIRED
}

abstract class AbstractBus {
    /**
     * The name of the current stop where the bus is at.
     */
    public String currentStopName;

    /**
     * Moves the bus to next stop and returns the amount of time spent moving. If the bus is already at its final stop,
     * return -1.
     *
     * @return The amount of time spent moving if the bus is not at its final stop; else, -1.
     */
    public abstract int moveToNextStop();

    /**
     * Takes in a pseudorandom generator and returns a boolean value denoting whether the bus broke down.
     */
    public abstract boolean didBreakdown(Random random);

    @Override
    public abstract String toString();
}

/**
 * Represents the NUS Bus A1.
 */
class BusA1 extends AbstractBus {

    public BusA1() {
        BusMap.Pair pair = BusMap.getNextStopAndTimeTaken("A1", null);
        assert pair != null;
        currentStopName = pair.stopName; // assigns to superclass' `stopName`
    }

    /**
     * Moves the bus to next stop and returns the amount of time spent moving. If the bus is already at its final stop,
     * return -1.
     *
     * @return The amount of time spent moving if the bus is not at its final stop; else, -1.
     */
    @Override
    public int moveToNextStop() {
        // TODO: Implement this (Task 2a)
        return -1;
    }

    // Bus A1 should breakdown with a probability of 0.1
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        return false;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return null;
    }

}

/**
 * Represents the NUS Bus B1.
 */
class BusB1 extends AbstractBus {

    public BusB1() {
        BusMap.Pair pair = BusMap.getNextStopAndTimeTaken("B1", null);
        assert pair != null;
        currentStopName = pair.stopName; // assigns to superclass' `stopName`
    }

    /**
     * Moves the bus to next stop and returns the amount of time spent moving. If the bus is already at its final stop,
     * return -1.
     *
     * @return The amount of time spent moving if the bus is not at its final stop; else, -1.
     */
    @Override
    public int moveToNextStop() {
        // TODO: Implement this (Task 2a)
        return -1;
    }

    // Bus B1 should breakdown with a probability of 0.2
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        return false;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return null;
    }

}

/**
 * Represents the NUS Bus C.
 */
class BusC extends AbstractBus {

    public BusC() {
        BusMap.Pair pair = BusMap.getNextStopAndTimeTaken("C", null);
        assert pair != null;
        currentStopName = pair.stopName; // assigns to superclass' `stopName`
    }

    /**
     * Moves the bus to next stop and returns the amount of time spent moving. If the bus is already at its final stop,
     * return -1.
     *
     * @return The amount of time spent moving if the bus is not at its final stop; else, -1.
     */
    @Override
    public int moveToNextStop() {
        // TODO: Implement this (Task 2a)
        return -1;
    }

    // Bus C should breakdown with a probability of 0.05
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        return false;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return null;
    }

}


/**
 * Represents the NUS Bus D1.
 */
class BusD1 extends AbstractBus {

    public BusD1() {
        BusMap.Pair pair = BusMap.getNextStopAndTimeTaken("D1", null);
        assert pair != null;
        currentStopName = pair.stopName; // assigns to superclass' `stopName`
    }

    /**
     * Moves the bus to next stop and returns the amount of time spent moving. If the bus is already at its final stop,
     * return -1.
     *
     * @return The amount of time spent moving if the bus is not at its final stop; else, -1.
     */
    @Override
    public int moveToNextStop() {
        // TODO: Implement this (Task 2a)
        return -1;
    }

    // Bus D1 should breakdown with a probability of 0.4
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        return false;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return null;
    }

}
