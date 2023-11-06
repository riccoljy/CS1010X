import java.util.Random;

/**
 * Represents the NUS Bus B1.
 */
public class BusB1 extends AbstractBus {

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


        int index = 0;
        int[] B1_TIMINGS = {0, 5, 1, 2, 2, 1, 2, 2, 1};
        String[] B1_STOPS = {"KR BUS TERMINAL", "IT (OPP CLB)", "OPP YIH", "UNIVERSITY TOWN",
                "YIH", "CENTRAL LIBRARY", "LT 13", "AS 5", "BIZ 2"};
        for (int i = 0; i < B1_STOPS.length; i++){
            if (currentStopName.equals(B1_STOPS[i])) {
                index = i;
                break;
            }
        }
        if (index == B1_STOPS.length - 1){
            return -1;
        }
        currentStopName = B1_STOPS[index + 1];
        return B1_TIMINGS[index+1];
    }

    // Bus B1 should breakdown with a probability of 0.2
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        boolean didOccur = random.nextDouble() < 0.2;
        return didOccur;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return "Bus B1";
    }

}
