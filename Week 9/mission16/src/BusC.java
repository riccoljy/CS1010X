import java.util.Random;

/**
 * Represents the NUS Bus C.
 */
public class BusC extends AbstractBus {

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
        int index = 0;
        int[] C_TIMINGS = {0, 1, 10, 3, 1, 3, 1, 2, 1, 1, 1, 2, 2, 1, 2};
        String[] C_STOPS = {"KR BUS TERMINAL (START)", "JAPANESE PRI SCH", "KENT VALE",
                "MUSEUM", "UNIVERSITY TOWN (FROM KR)", "UHC", "OPP UNIVERSITY HALL", "S 17 (OPP LT 27)", "LT 27",
                "UNIVERSITY HALL", "OPP UHC", "UNIVERSITY TOWN (TO KR)", "RAFFLES HALL", "EA", "KR BUS TERMINAL (END)"};
        for (int i = 0; i < C_STOPS.length; i++){
            if (currentStopName.equals(C_STOPS[i])) {
                index = i;
                break;
            }
        }
        if (index == C_STOPS.length - 1){
            return -1;
        }
        currentStopName = C_STOPS[index + 1];
        return C_TIMINGS[index+1];
    }

    // Bus C should breakdown with a probability of 0.05
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        boolean didOccur = random.nextDouble() < 0.05;
        return didOccur;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return "Bus C";
    }

}
