import jdk.jfr.Event;

import java.awt.*;
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
            while (!eventQueue.isEmpty()) {
                BusEvent latestevent = eventQueue.poll();
                String currStop = latestevent.bus.currentStopName;
                int currTime = latestevent.time;
                System.out.println(currTime + ": "+ latestevent.bus + " arrives at " + currStop + ".");

                int travelTime = latestevent.bus.moveToNextStop();
                if (travelTime != -1) {
                    currTime += travelTime;
                    BusEvent nextEvent = new BusEvent(latestevent.bus, currTime);
                    eventQueue.offer(nextEvent);
                }
                else if (eventQueue.isEmpty()) break;
            }
    }

    /**
     * Runs the simulator with a probability of bus breakdowns until the event queue has been emptied.
     * <p>
     * Uses the `random` initialised on top in `BusSimulator` for pseudorandom number generation.
     */
    public void runWithBreakdowns() {
        // TODO: Implement this (Task 4b)
        while (!eventQueue.isEmpty()) {

            BusEvent latestevent = eventQueue.poll();
            String currStop = latestevent.bus.currentStopName;
            int currTime = latestevent.time;

            if (latestevent.eventType == EventType.BROKEN_DOWN) {
                System.out.println(currTime + ": " + latestevent.bus + " has broken down at " + currStop + ".");
                currTime += 10;
                BusEvent nextEvent = new BusEvent(latestevent.bus, currTime);
                nextEvent.eventType = EventType.REPAIRED;
                eventQueue.offer(nextEvent);
            }
            else if (latestevent.eventType == EventType.OPERATIONAL) {
                System.out.println(currTime + ": " + latestevent.bus + " arrives at " + currStop + ".");

                if (latestevent.bus.didBreakdown(random)) {
                    currTime += 1;
                    BusEvent nextEvent = new BusEvent(latestevent.bus, currTime);
                    nextEvent.eventType = EventType.BROKEN_DOWN;
                    eventQueue.offer(nextEvent);
                    continue;
            }
                int travelTime = latestevent.bus.moveToNextStop();
                if (travelTime != -1) {
                    currTime += travelTime;
                    BusEvent nextEvent = new BusEvent(latestevent.bus, currTime);
                    eventQueue.offer(nextEvent);
                }
                else if (eventQueue.isEmpty()) break;
            }

            else if (latestevent.eventType == EventType.REPAIRED) {
                System.out.println(currTime + ": " + latestevent.bus + " has been repaired at " + currStop + ".");
                int travelTime = latestevent.bus.moveToNextStop();
                if (travelTime != -1) {
                    currTime += travelTime;
                    BusEvent nextEvent = new BusEvent(latestevent.bus, currTime);
                    eventQueue.offer(nextEvent);
                }
            }
        }
    }
    /**
     * Entry point to this program.
     */
    public static void main(String[] args) {
        List<BusEvent> busEvents = readBusEvents();
        BusSimulator simulator = new BusSimulator(busEvents);
        simulator.printStatus();
        simulator.runWithBreakdowns();
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

        return busEvents;
    }
}
