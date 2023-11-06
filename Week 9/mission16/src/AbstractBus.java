import java.util.Random;

public abstract class AbstractBus {
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
