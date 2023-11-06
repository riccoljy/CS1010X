import java.util.Random;

/**
 * Represents the NUS Bus D1.
 */
public class BusD1 extends AbstractBus {

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
        int index = 0;
        int[] D1_TIMINGS = {0, 4, 2, 2, 1, 1, 2, 1, 3, 1, 1, 7, 2, 4};
        String[] D1_STOPS = {"OPP HSSML", "OPP NUSS", "COM 2 (FROM HSSML)", "VENTUS (OPP LT 13)",
                "IT (OPP CLB)", "OPP YIH", "MUSEUM", "UNIVERSITY TOWN", "YIH", "CENTRAL LIBRARY",
                "LT 13", "AS 5", "COM 2 (TO BIZ 2)", "BIZ 2"};
        for (int i = 0; i < D1_STOPS.length; i++){
            if (currentStopName.equals(D1_STOPS[i])) {
                index = i;
                break;
            }
        }
        if (index == D1_STOPS.length - 1){
            return -1;
        }
        currentStopName = D1_STOPS[index + 1];
        return D1_TIMINGS[index+1];
    }

    // Bus D1 should breakdown with a probability of 0.4
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        boolean didOccur = random.nextDouble() < 0.4;
        return didOccur;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return "Bus D1";
    }

}
