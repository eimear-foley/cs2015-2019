package A_01;

/**
 * Abstract Class: RootSolver
 * @author Eimear Foley
 * @version 1 (29th November 2017)
 */
public abstract class RootSolver {
    protected static final double EPSILON = 1.0E-6;
    protected static final int MAX_ITERATIONS = 6;
    protected int convergence;

    /**
     * Specification of a solve function to find a root
     * @param x0 double
     * @param x1 double
     * @return double
     */
    abstract public double solve(double x0, double x1);

    /**
     * Specification of a function to return convergence of 'solve'
     * @return int
     */
    abstract public int getConvergence();

    /**
     * Specification of a function to return the reliability of 'solve'
     * @return boolean
     */
    abstract public boolean getReliability();
}
