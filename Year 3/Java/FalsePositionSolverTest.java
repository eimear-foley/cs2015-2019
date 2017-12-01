package A_01;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * False Position Solver testing with JUnit 5
 * @author Eimear Foley
 * @version 1 (29th November 2017)
 */
public class FalsePositionSolverTest {
    /**
     * Test function to check if arguments to 'solve' do not throw IAE
     */
    @Test
    public void shouldThrowIAEForGreaterThanOrEqualToZero(){
        FalsePositionSolver test = new FalsePositionSolver();
        assertThrows(IllegalArgumentException.class, () -> {
            test.solve(-3.0, -2.5);
        });
    }

    /**
     * Test function to check if the correct root has been found
     */
    @Test
    public void correctRootFound(){
        FalsePositionSolver test = new FalsePositionSolver();
        double root = test.solve(2,5);
        // Testing against 2 which is a root of x - 2.5 * sin(x) * sin(x)
        assertEquals(Math.round(root), 2);
    }
}
