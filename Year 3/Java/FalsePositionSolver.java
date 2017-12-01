package A_01;

/**
 * False Position Solver: extends RootSolver implements Univariate Function
 * @author Eimear Foley
 * @version 4 (29th November 2017)
 */
public class FalsePositionSolver extends RootSolver implements UnivariateFunction {
    /**
     * A function 'f'
     * @param x Double type
     * @return A univariate function
     */
    public static double f(double x){
        return x - 2.5 * Math.sin(x) * Math.sin(x);
    }

    /**
     * Gets convergence of solver
     * @return convergence
     */
    @Override
    public int getConvergence() {
        return convergence;
    }

    /**
     * Sets convergence of solver
     * @param convergence int
     */
    public void setConvergence(int convergence){
        this.convergence = convergence;
    }

    /**
     * Gets reliability of solver
     * @return boolean
     */
    @Override
    public boolean getReliability() {
        return true;
    }

    /**
     * {@code f(x0) * f(x1) < 0}
     * @param x0 First parameter of FalsePositionSolver
     * @param x1 Second parameter of FalsePositionSolver
     * @return root
     * @throws IllegalArgumentException if not a double type
     */
    @Override
    public double solve(double x0, double x1) throws IllegalArgumentException {
        double root = 0.0;
        int numberOfIterations = 0;

        if (f(x0) * f(x1) >= 0) {
            throw new IllegalArgumentException("f(" + x0 + ") x f(" + x1 + ") must be < 0");
        }

        boolean rootNotFound = true;

        do {
            numberOfIterations += 1;
            root = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0));
            rootNotFound = (Math.abs(root - x1) > EPSILON) && (Math.abs(root -x0) > EPSILON);

            if (rootNotFound){
                if (f(root) * f(x0) < 0) {
                    x1 = root;
                } else {
                    x0 = root;
                }
            }

        } while (rootNotFound && (numberOfIterations < MAX_ITERATIONS));

        setConvergence(numberOfIterations);

        return root;
    }

    /**
     * Main function
     * @param arg null
     * Creates instances of FalsePositionSolver
     * Prints a root, the convergence and reliability
     */
    public static void main(String[] arg){
        FalsePositionSolver toSolve = new FalsePositionSolver();
        double root = toSolve.solve(2, 5);
        System.out.println("Root = " + root);
        System.out.println("Convergence: " + toSolve.getConvergence());
        System.out.println("Reliable: " + toSolve.getReliability());
    }
}
