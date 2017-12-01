package A_01;

/**
 * Secant Solver: extends RootSolver implements Univariate Function
 * @author Eimear Foley
 * @version 4 (29th November 2017)
 */
public class SecantSolver extends RootSolver implements UnivariateFunction {
    /**
     * A function 'f'
     * @param x Double type
     * @return A univariate function
     */
    public static Double f(Double x){
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
        return false;
    }

    /**
     * 'solve' function
     * {@code f(x0) * f(x1) < 0}
     * @param x0 first param of SecantSolver's 'solve', Double type
     * @param x1 second param of SecantSolver's 'solve', Double type
     * @return root
     * @throws IllegalArgumentException if not a double type
     */
    @Override
    public double solve(double x0, double x1) {

        double c = (x0 + x1) / 2;
        int count = 0;

        do {
            c = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0));
            x0 = 1;
            x1 = c;
            count += 1;
            if (count == MAX_ITERATIONS) {
                break;
            }
        } while (Math.abs(f(c)) > EPSILON);

        setConvergence(count);
        return c;
    }

    /**
     * Main function
     * @param arg null
     * Creates instances of SecantSolver
     * Prints a root, the convergence and reliability
     */
    public static void main(String[] arg){
        SecantSolver toSolve = new SecantSolver();
        double root = toSolve.solve(-2, 6);
        System.out.println("Root = " + root);
        System.out.println("Convergence: " + toSolve.getConvergence());
        System.out.println("Reliable: " + toSolve.getReliability());
    }
}

