import java.util.Random;

/**
 * Represents the NUS Bus A1.
 */
public class BusA1 extends AbstractBus {

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
        int index = 0;
        int[] A1_TIMINGS = {0, 3, 3, 2, 2, 1, 2, 2, 5, 6, 3, 1, 1};
        String[] A1_STOPS = {"PGP (START)", "KR MRT", "LT 27", "UNIVERSITY HALL", "OPP UHC",
                "YIH", "CENTRAL LIBRARY", "LT 13", "AS 5", "COM 2", "BIZ 2", "OPP TCOMS", "PGP (END)"};
        for (int i=0; i < A1_STOPS.length; i++){
            if (currentStopName.equals(A1_STOPS[i])) {
                index = i;
                break;
            }
        }
        if (index == A1_STOPS.length - 1){
            return -1;
        }
        currentStopName = A1_STOPS[index + 1];
        return A1_TIMINGS[index+1];
    }

    // Bus A1 should breakdown with a probability of 0.1
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        boolean didOccur = random.nextDouble() < 0.1;
        return didOccur;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return "Bus A1";
    }

}
